
# ============================================
# translations_it.py - Dizionario italiano
# Completamente ordinato per categorie
# Commenti in tedesco per coerenza
# ============================================

def load_italian_strings():
    """Carica tutte le stringhe italiane"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View di BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Apri PDF",
        'btn_text_window': "Testo OCR",
        'btn_first': "Prima pagina",
        'btn_prev': "Pagina precedente",
        'btn_next': "Pagina successiva",
        'btn_last': "Ultima pagina",
        'btn_print': "Stampa",
        'btn_darkmode_light': "Modalità chiara",
        'btn_darkmode_dark': "Modalità scura",
        'btn_delete_pages': "Elimina pagine",
        'btn_extract_pages': "Estrai pagine",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Annulla",
        'btn_save': "Salva",
        'btn_close': "Chiudi",
        'btn_delete': "Elimina",
        'btn_delete_all': "Elimina tutto",
        'btn_copy': "Copia",
        'btn_export': "Esporta",
        'btn_show': "Mostra password",
        'btn_hide': "Nascondi password",
        'btn_authenticate': "Autentica",
        'btn_settings': "Impostazioni",
        'btn_protect': "Proteggi",
        'btn_remove_password': "Rimuovi password",
        'btn_manage': "Gestione password",
        'btn_retry': "Riprova",
        'btn_select_all': "Seleziona tutto",
        'btn_clear_selection': "Deseleziona",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Pagina {0} di {1}",
        'page_count': "di {0}",
        'goto_page': "Vai a pagina",
        'page_simple': "Pagina {0}",
        'full_view_page': "Vista intera pagina {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Inserisci termine + Invio",
        'search_results': "Risultati: {0} di {1}",
        'search_nav_hint': "Invio: successivo  (Maiusc+Invio: precedente)",
        'search_no_results': "Nessun risultato",
        'search_error': "Errore di ricerca",
        'search_active': "Campo di ricerca attivato",
        'search_closed': "Ricerca chiusa",
        'search_position': "Pagina {0} {1}",
        'search_pos_top': "in alto",
        'search_pos_upper': "in alto",
        'search_pos_middle': "centro",
        'search_pos_lower': "in basso",
        'search_pos_bottom': "in fondo",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Riconoscimento del testo completato con successo!",
        'ocr_success_title': "OCR riuscito",
        'ocr_success_message': "Il documento ora è ricercabile.",
        'ocr_failed': "OCR fallito",
        'ocr_in_progress': "OCR in corso",
        'ocr_preparing': "Preparazione PDF...",
        'ocr_analyzing': "Analisi PDF...",
        'ocr_optimizing': "Ottimizzazione immagine...",
        'ocr_recognizing': "Riconoscimento testo...",
        'ocr_embedding': "Incorporamento testo...",
        'ocr_finalizing': "Finalizzazione PDF...",
        'ocr_not_available': "OCR non disponibile",
        'ocr_install_message': "Strumenti OCR non trovati.\n\nInstallare:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR necessario",
        'ocr_question': "Il PDF non contiene testo ricercabile.\nEseguire l'OCR per consentire {0}?",
        'ocr_perform': "Esegui OCR",
        'ocr_later': "Più tardi",
        'ocr_starting': "Avvio OCR garantito...",
        'ocr_success_voice': "OCR riuscito. Il PDF ora è ricercabile.",
        'ocr_partial_success': "OCR eseguito, ma problemi durante la sostituzione.\n\nLa versione ricercabile è stata salvata in:\n{0}\n\nErrore: {1}",
        'ocr_partial_title': "OCR parzialmente riuscito",
        'ocr_partial_voice': "OCR eseguito, ma sostituzione fallita.",
        'original_file': "File originale:",
        'old_size': "Dimensione vecchia:    {0} byte",
        'new_size': "Dimensione nuova: {0} byte",
        'size_change': "Variazione: {0}{1} byte",
        'backup_created_file': "Backup creato:\n{0}",
        'backup_not_created': "Backup: non creato (impostazione disabilitata)",
        'page_header': "=== Pagina {0} ===\n{1}\n",
        'scanned_page_header': "=== Pagina {0} (scansionata) ===\n[Questa pagina contiene solo testo scannerizzato]\n[Eseguire OCR manualmente]\n",
        'scanned_warning': "⚠️ TESTO SCANSIONATO - OCR NECESSARIO",
        'guaranteed_title': "PDF ricercabile creato",
        'guaranteed_message': "<b>Versione garantita ricercabile creata!</b>\n\nPoiché l'OCR automatico è fallito, è stato creato un PDF alternativo ricercabile:\n\n{0}\n\n<b>Questo file contiene:</b>\n• Testo estratto (se disponibile)\n• Indicazioni per pagine scansionate\n• È completamente ricercabile",
        'guaranteed_voice': "PDF ricercabile garantito creato.",
        'instruction_title': "ISTRUZIONI PER OCR",
        'instruction_file': "File originale: {0}",
        'instruction_text': "Il riconoscimento automatico del testo (OCR) è fallito.\nEseguire OCR manualmente:\n\n1. CON OCRmyPDF (riga di comando):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. CON ADOBE ACROBAT (macOS/Windows):\n   • Aprire il PDF in Acrobat\n   • Strumenti > Modifica PDF\n   • Selezionare 'Riconosci testo'\n\n3. CON ANTEPRIMA (macOS):\n   • Aprire il PDF in Anteprima\n   • File > Esporta...\n   • Filtro Quartz: 'Riduci dimensione file'\n   • Abilitare 'Esegui OCR'\n\n4. SERVIZI ONLINE:\n   • smallpdf.com/it/ocr-pdf\n   • ilovepdf.com/it/ocr-pdf\n   • adobe.com/it/acrobat/online/pdf-to-word.html",
        'instruction_created': "Istruzioni OCR create",
        'instruction_created_message': "Sono state create istruzioni dettagliate:\n\n{0}\n\nSeguire i passaggi per l'OCR manuale.",
        'instruction_created_voice': "Istruzioni OCR create.",
        'ocr_impossible': "OCR impossibile",
        'ocr_impossible_message': "Impossibile eseguire l'OCR.\n\nElaborare '{0}' manualmente con software OCR.",
        'ocr_impossible_voice': "OCR impossibile. Elaborare manualmente.",
        'emergency_title': "OCR di emergenza",
        'emergency_message': "È stato creato un PDF di emergenza:\n\n{0}\n\nElaborare questo file manualmente con OCR.",
        'emergency_voice': "PDF di emergenza creato. Eseguire OCR manualmente.",
        'critical_error': "Errore critico",
        'critical_error_message': "Impossibile avviare l'OCR.\n\nRiavviare il programma e\nverificare l'installazione dell'OCR.",
        'critical_error_voice': "Errore OCR critico",
        'ocr_question_html': "<p>Il PDF non contiene testo ricercabile.<p>Eseguire l'OCR per consentire <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR necessario. Il PDF non contiene testo ricercabile. Eseguire l'OCR per consentire {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "nessun PDF caricato",
        'no_pdf_message': "Nessun PDF caricato",
        'pdf_not_found': "File PDF non trovato",
        'file_size': "Dimensione file",
        'bytes': "byte",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup creato",
        'backup_disabled': "Backup disabilitato",
        'backup_activated': "Creazione backup attivata",
        'backup_deactivated': "Creazione backup disattivata",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ attivato",
        'backup_off': "✘ disattivato",
        'close_pdf': "Chiusura PDF: {0}",
        'pdf_not_found_format': "File PDF non trovato: {0}",
        'error_pdf_load_format': "Errore nel caricamento del PDF: {0}",
        'load_failed_format': "Caricamento fallito:\n{0}",
        'decrypted_suffix': "(decifrato)",
        'decryption_failed': "Decifratura fallita.",
        'decryption_error': "Errore durante la decifratura",
        'decryption_success': "Decifratura riuscita",
        'decryption_success_message': "Il PDF è stato decifrato e salvato in:\n\n{0}",
        'decryption_success_voice': "PDF decifrato e salvato.",
        'password_remove_error': "Errore durante la rimozione della password",
        'save_unencrypted': "Salva PDF non cifrato come",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Salva con nome...",
        'save_copy': "Salva copia",
        'save_success': "PDF salvato in: {0}",
        'save_encrypted': "PDF protetto salvato in: {0}",
        'save_error': "Impossibile salvare il PDF",
        'encryption_question': "Proteggere il PDF con password?",
        'encryption_yes': "Sì",
        'encryption_no': "No",
        'encryption_cancel': "Annulla",
        'save_cancel': "Salvataggio annullato",
        'save_encrypted_voice': "File cifrato e salvato.",
        'save_success_voice': "Il file PDF è stato salvato non cifrato.",
        'save_error_format': "Impossibile salvare il PDF:\n{0}",
        'export_pages_success': "Esportazione in Pages riuscita",
        'export_pages_error': "Esportazione in Pages fallita",
        'export_pages_error_format': "Esportazione in Pages fallita: {0}",
        'export_word_success': "Esportazione in Word riuscita",
        'export_word_error': "Esportazione in Word fallita",
        'export_word_error_format': "Esportazione in Word fallita: {0}",
        'export_text_success': "Esportazione in testo riuscita",
        'export_text_error': "Esportazione in testo fallita",
        'export_text_error_format': "Esportazione in testo fallita: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Password richiesta",
        'password_enter': "Inserire la password",
        'password_confirm': "Conferma password",
        'password_new': "Nuova password",
        'password_current': "Password attuale",
        'password_save': "Salva password (cifrata)",
        'password_saved': "✓ Password per questo file salvata",
        'password_wrong': "Password errata",
        'password_mismatch': "Le password non coincidono",
        'password_too_short': "Password troppo corta",
        'password_min_length': "La password deve essere di almeno 4 caratteri",
        'password_strength': "Robustezza password",
        'password_strength_very_weak': "Molto debole",
        'password_strength_weak': "Debole",
        'password_strength_medium': "Media",
        'password_strength_strong': "Forte",
        'password_strength_very_strong': "Molto forte",
        'password_char_count': "({0} caratteri)",
        'password_match': "✓ Corrispondenza",
        'password_no_match': "✗ Le password non coincidono",
        'password_show': "Mostra",
        'password_hide': "Nascondi",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Gestione password",
        'password_table_filename': "Nome file",
        'password_table_password': "Password",
        'password_count': "{0} password salvata{1}",
        # Italienisch: 1 password salvata, 2 password salvate -> wir nutzen zwei Platzhalter.
        # Hier vereinfacht: {0} = Anzahl, {1} = "e" per singolare/plurale? – Wir lassen es erstmal.
        'password_count_singular': "",
        'password_count_plural': "e",
        'password_none': "Nessuna password salvata",
        'password_copied': "{0} password copiata{1}",
        'password_copied_singular': "",
        'password_copied_plural': "e",
        'password_delete_confirm': "Eliminare la password per '{0}'?",
        'password_delete_multiple': "Eliminare le {0} password selezionate?",
        'password_delete_all_confirm': "Eliminare tutte le {0} password salvate?",
        'password_deleted': "{0} password eliminata{1}",
        'password_deleted_singular': "",
        'password_deleted_plural': "e",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Tutte le password sono state eliminate",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generatore di password",
        'generator_generated': "Password generata:",
        'generator_regenerate': "Rigenera",
        'generator_copy': "Copia",
        'generator_use': "Usa",
        'generator_settings': "Impostazioni",
        'generator_length': "Lunghezza:",
        'generator_group_every': "Separatore ogni",
        'generator_group_chars': "caratteri.   Separatore:",
        'generator_uppercase': "Maiuscole (A-Z)",
        'generator_lowercase': "Minuscole (a-z)",
        'generator_digits': "Cifre (0-9)",
        'generator_symbols': "Simboli (!@#$%^&*)",
        'generator_exclude': "Esclusi:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Password master richiesta",
        'master_password_setup': "Imposta password master",
        'master_password_change': "Cambia password master",
        'master_password_enter': "Inserire la password master",
        'master_password_choose': "Scegliere una password master sicura (almeno 8 caratteri)",
        'master_password_new': "Inserire la nuova password master",
        'master_password_confirm': "Conferma password",
        'master_password_authenticate': "Autentica",
        'master_password_success': "Password master impostata con successo.",
        'master_password_changed': "Password master cambiata con successo.",
        'master_password_removed': "Password master e tutte le password eliminate.",
        'master_password_remove': "Rimuovi password master",
        'master_password_remove_confirm': "Siete SICURI di voler eliminare TUTTE le password?\n\nQuesta azione è IRREVERSIBILE!",
        'master_password_export_before': "Esportare prima una copia di backup?",
        'master_password_export_delete': "Esporta ed elimina",
        'master_password_delete_now': "Elimina ora",
        'master_password_for_signatures': "Per usare le firme, è necessario impostare una password master.\n\nImpostare ora una password master?",
        'master_password_for_private': "Per usare modelli di testo privati, è necessario impostare una password master.\n\nImpostare ora una password master?",
        'master_password_info': """
            <b>🔐 SENZA PASSWORD MASTER:</b><br>
            • Impossibile visualizzare, copiare o esportare password<br>
            • Eliminazione password sempre possibile (anche senza password master)<br><br>

            <b>🔐 CON PASSWORD MASTER:</b><br>
            • Tutte le funzioni disponibili dopo autenticazione<br>
            • Le password sono cifrate con la password master<br>
            • Lunghezza minima: 8 caratteri<br>
            • Archiviazione sicura con hash SHA-256<br><br>

            <b>IMPORTANTE:</b><br>
            • Se si perde la password master, le password non sono recuperabili<br>
            • Rimuovendo la password master, TUTTE le password vengono eliminate<br>
            • Opzione di esportazione disponibile prima dell'eliminazione<br>
            • La password master può essere cambiata in qualsiasi momento
        """,
        'signature_auth_disabled': "Disabilita richiesta password per le firme",
        'template_auth_disabled': "Disabilita richiesta password per modelli privati",
        'master_password_for_signatures_settings': "Per usare le firme, è necessario impostare una password master.\n\nAndare in Impostazioni - Gestione password",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Proteggi PDF",
        'protect_info': "Il file '{0}' sarà protetto da password.",
        'protect_instruction': "Inserire due volte la password desiderata per proteggere il documento, oppure usare il generatore di password a destra del campo di inserimento.",
        'protect_success': "PDF protetto con successo e salvato in:\n{0}\n\nPassword: {1}\n\nAprire ora il PDF protetto?",
        'protect_open': "Sì",
        'protect_skip': "No",
        'protect_error': "Errore durante la protezione del PDF",
        'protect_open_title': "apri PDF protetto",
        'protect_question': "Completato. Aprire ora il PDF protetto? Sì o No?",
        'password_cancel': "Dialogo password annullato",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Elimina pagine",
        'pages_extract': "Estrai pagine",
        'pages_insert': "Inserisci pagine",
        'pages_move': "Sposta pagine",
        'pages_delete_options': "Opzioni di eliminazione",
        'pages_delete_empty': "Elimina tutte le pagine vuote",
        'pages_delete_current': "Elimina pagina corrente",
        'pages_delete_range': "Elimina intervallo di pagine",
        'pages_extract_options': "Opzioni di estrazione",
        'pages_extract_current': "Estrai pagina corrente",
        'pages_extract_range': "Estrai intervallo di pagine",
        'pages_insert_position': "Posizione di inserimento",
        'pages_insert_before': "Inserisci prima della pagina:",
        'pages_insert_select': "Seleziona PDF",
        'pages_insert_none': "Nessun PDF selezionato",
        'pages_move_source': "Pagine da spostare",
        'pages_move_from': "Da pagina:",
        'pages_move_to': "A pagina:",
        'pages_move_target': "Posizione di destinazione",
        'pages_move_before': "Sposta prima della pagina:",
        'pages_move_hint': "Nota: pagina 1 = inizio, {0} = fine",
        'pages_range_invalid': "La pagina iniziale deve essere minore o uguale alla pagina finale.",
        'pages_position_invalid': "La posizione di destinazione non deve essere all'interno dell'intervallo da spostare.",
        'pages_no_pdf_selected': "Nessun PDF selezionato.",
        'pages_deleted': "{0} pagine sono state eliminate.",
        'pages_extracted': "Estratto: {0}\nSalvato in: {1}\nDimensione: {2:.1f} KB",
        'pages_inserted': "{0} pagine inserite",
        'pages_moved': "{0} pagine sono state spostate.",
        'pages_deleted_none': "Nessuna pagina eliminata.",
        'pages_delete_progress': "Eliminazione pagine...",
        'pages_deleted_with_backup': "{0} pagine eliminate.\n\nBackup: {1}",
        'pages_deleted_voice': "Backup creato e {0} pagine eliminate.",
        'info': "Informazione",
        'error_dialog_creation': "Impossibile creare la finestra di dialogo",
        'extract_page_single': "Estrai pagina {0}",
        'extract_page_range': "Estrai pagine {0}–{1}",
        'extract_success_voice': "Pagine estratte con successo",
        'extract_error_format': "Errore durante l'estrazione: {0}",
        'pages_inserted_voice': "{0} pagine inserite.",
        'insert_error_format': "Errore durante l'inserimento: {0}",
        'pages_move_progress': "Spostamento pagine...",
        'pages_moved_with_backup': "{0} pagine spostate.\n\nBackup: {1}",
        'move_success_title': "Spostamento riuscito",
        'pages_moved_voice': "{0} pagine spostate con successo",
        'mark_removed': "Marcatura rimossa dalla pagina {0}",
        'mark_empty': "Pagina {0} marcata come vuota",
        'mark_export_removed': "Marcatura esportazione rimossa dalla pagina {0}",
        'mark_export': "Pagina {0} marcata per esportazione",
        'no_empty_pages': "Nessuna pagina vuota marcata per eliminazione",
        'delete_empty_confirm': "Eliminare tutte le {0} pagine vuote marcate?",
        'delete_empty_confirm_voice': "Eliminare ora tutte le {0} pagine vuote marcate? Sì o No.",
        'empty_pages_deleted': "{0} pagine vuote eliminate",
        'no_export_pages': "Nessuna pagina marcata per esportazione",
        'overwrite_title': "Sovrascrivere file esistente",
        'overwrite_question': "Il file\n\n{0}\n\nesiste già.\nSovrascriverlo?",
        'overwrite_voice': "Sovrascrivere file esistente? Sì o No.",
        'page_skipped': "Pagina {0} saltata",
        'export_complete': "Esportazione completata.",
        'export_complete_voice': "L'esportazione è completata.",
        'no_pages_exported': "Nessuna pagina esportata",
        'export_cancelled': "Esportazione annullata",
        'pages_exported': "{0} pagine esportate in {1}",
        'export_page_title': "Esporta pagina",
        'page_exported': "Pagina {0} esportata in {1}",
        'export_error': "Errore durante l'esportazione",
        'export_marked_title': "Esporta pagine marcate",
        'rotate_all_title': "ruota tutte le pagine",
        'rotate_all_question': "Ruotare tutte le pagine di 90 gradi a destra?",
        'rotate_all_voice': "Ruotare tutte le pagine di 90 gradi a destra? Sì o No?",
        'all_pages_rotated': "Tutte le pagine ruotate",
        'page_rotated': "Pagina {0} ruotata",
        'rotate_error': "Impossibile ruotare la pagina",
        'delete_page_confirm': "Eliminare la pagina {0}?",
        'delete_page_confirm_voice': "Eliminare davvero la pagina {0}? Sì o No.",
        'page_deleted': "Pagina {0} eliminata",
        'delete_error': "Impossibile eliminare la pagina",
        'pages_deleted_voice': "{0} pagine eliminate",
        'pages_exported_split': "{0} pagine sono state esportate con successo.",
        'pages_skipped': "{0} pagine sono state saltate.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Estrai pagine (avanzato)",
        'pdf_splitter_title': "Dividi ed estrai PDF",
        'pdf_splitter_load': " Seleziona file PDF",
        'pdf_splitter_info': "Scegliere un'opzione per il documento PDF",
        'pdf_splitter_basic': "Operazioni di base",
        'pdf_splitter_single': "Dividi in singole pagine",
        'pdf_splitter_range': "Estrai pagine:",
        'pdf_splitter_range_placeholder': "es. 1-3,5,7-9",
        'pdf_splitter_clean': "Operazioni di pulizia",
        'pdf_splitter_remove_empty': "Rimuovi tutte le pagine vuote",
        'pdf_splitter_remove': "Elimina intervallo di pagine:",
        'pdf_splitter_remove_placeholder': "es. 2,4-6",
        'pdf_splitter_process': "Elabora PDF",
        'pdf_splitter_loaded': "PDF caricato. Scegliere un'opzione",
        'pdf_read_error': "Impossibile leggere il PDF",
        'pages': "Pagine",
        'pages_created': "Pagine create",
        'range_empty': "Inserire un intervallo di pagine",
        'range_invalid': "Intervallo di pagine non valido",
        'range_created': "Nuovo PDF con le pagine selezionate creato:\n{0}",
        'empty_removed': "{0} pagine vuote rimosse.\nOutput: {1}",
        'remove_empty': "Inserire le pagine da rimuovere",
        'remove_invalid': "Pagine da rimuovere non valide",
        'remove_done': "PDF pulito creato:\n{0}",
        'open_folder': "Apri cartella",
        'show_in_finder': "Mostra nel Finder",
        'pdf_splitter_no_pdf': "Caricare prima un file PDF.",
        'process_error': "Errore durante l'elaborazione del PDF",
        'pages_created_voice': "{0} pagine create",
        'range_created_voice': "PDF con le pagine selezionate creato",
        'empty_removed_voice': "{0} pagine vuote rimosse",
        'remove_done_voice': "PDF pulito creato",
        'pdf_splitter_split_groups': "Ogni gruppo contiguo in file separato",
        'range_created_single': "Nuovo PDF creato:\n{0}",
        'range_created_multiple': "{0} file PDF creati.",
        'range_created_voice_single': "Un PDF con le pagine selezionate è stato creato",
        'range_created_voice_multiple': "{0} file PDF creati",
        'empty_removed_none_left': "Nessuna pagina rimasta",
        'empty_removed_all_empty': "Tutte le pagine sono state riconosciute come vuote e verrebbero rimosse. Nessun file creato.",
        'preview_single': "Anteprima: {0}",
        'preview_enter_range': "Inserire un intervallo di pagine.",
        'preview_invalid_range': "Intervallo di pagine non valido.",
        'preview_file': "Anteprima: {0}",
        'preview_files': "Anteprima: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Avvio stampa",
        'print_sent': "Lavoro di stampa inviato",
        'print_now': "Stampa subito",
        'print_error': "Errore durante la stampa diretta",
        'print_limited': "Funzione di stampa limitata su questo sistema",
        'print_error_format': "Errore durante la stampa diretta: {0}",
        'warning': "Avviso",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Passa a modalità chiara",
        'mode_switch_to_dark': "Passa a modalità scura",
        'mode_dark_activated': "Modalità scura attivata",
        'mode_light_activated': "Modalità chiara attivata",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Pagina intera",
        'zoom_two_pages': "Due pagine affiancate",
        'zoom_overview': "Vista panoramica",
        'zoom_cannot_during_search': "Zoom non possibile durante la ricerca",
        'zoom_exit_first': "Uscire prima dallo zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & drop attivato",
        'drag_disabled': "Drag & drop disattivato",
        'drag_page_grab': "Afferra pagina {0}",
        'drag_page_dropped': "Pagina {0} inserita in posizione {1}",
        'drag_position_invalid': "Posizione non valida",
        'drag_same_position': "La pagina {0} rimane in posizione {0}",
        'drag_error': "Errore durante lo spostamento",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Inserimento testo con formattazione avanzata e gestione modelli",
        'text_templates': "Modelli di testo disponibili:",
        'text_name': "Nome",
        'text_preview': "Anteprima testo",
        'text_enter': "Testo:",
        'text_font_size': "Dimensione carattere:",
        'text_formatting': "Formattazione:",
        'text_bold': "Grassetto",
        'text_italic': "Corsivo",
        'text_underline': "Sottolineato",
        'text_alignment': "Allineamento:",
        'text_left': "Sinistra",
        'text_center': "Centrato",
        'text_right': "Destra",
        'text_color': "Colore testo:",
        'text_opacity': "Opacità:",
        'text_word_wrap': "A capo automatico:",
        'text_auto': "Automatico",
        'text_page_width_95': "Larghezza pagina (95%)",
        'text_page_width_85': "Molto largo (85%)",
        'text_page_width_75': "Più largo (75%)",
        'text_page_width_60': "Largo (60%)",
        'text_page_width_50': "Medio (50%)",
        'text_page_width_30': "Stretto (30%)",
        'text_page_width_20': "Più stretto (20%)",
        'text_page_width_10': "Molto stretto (10%)",
        'text_no_wrap': "Nessun a capo",
        'text_private': "Modello privato (richiede autenticazione)",
        'text_preview_label': "Anteprima:",
        'text_preview_placeholder': "Qui verrà mostrata un'anteprima del testo...",
        'text_no_text': "(Nessun testo)",
        'text_save_template': "💾 Salva come modello",
        'text_delete_template': "🗑 Elimina modello selezionato",
        'text_show_private': "Mostra privati",
        'text_hide_private': "Nascondi privati",
        'text_use': "✅ Usa testo",
        'text_saved': "Modello di testo salvato come:\n{0}",
        'text_saved_voice': "Modello di testo salvato",
        'text_deleted': "Modello di testo eliminato",
        'text_no_text_to_save': "Nessun testo da salvare.",
        'text_no_templates': "Nessun modello di testo trovato",
        'text_private_master_required': "I modelli privati possono essere usati solo se è impostata una password master.\n\nImpostare ora una password master?",
        'text_filename': "Nome file per il modello (senza 'Text_' e '.txt'):",
        'text_filename_hint': "Esempio: 'Telefono Casa' sarà salvato come 'Text_Telefono Casa.txt'",
        'text_save_hint': "Il modello di testo verrà automaticamente salvato con la formattazione.",
        'text_guide_title': "Inserimento testo - Guida",
        'text_delete_confirm': "Eliminare davvero il modello di testo?\n\nFile: {0}\nTesto: {1}...",
        'text_make_public': "Marca come pubblico",
        'text_make_private': "Marca come privato",
        'text_privacy_changed': "Stato di privacy cambiato",
        'text_private_always': "Privati sempre visibili (impostazione)",
        'text_mode_required': "Attivare prima la modalità testo",
        'text_continue_editing': "Continua modifica - cursore alla fine del testo",
        'text_no_input': "Nessun testo inserito - testo scartato",
        'save_dialog_question': "Come procedere?",
        'text_save_question': "Salvare tutti i testi e croci, regolare, continuare modifica o scartare?",
        'copy_cross': "Croce copiata",
        'paste_cross': "Croce incollata",
        'paste_text': "Testo incollato",
        'cross_discarded': "Croce scartata",
        'all_discarded': "Tutto scartato",
        'text_discarded': "Testo scartato",
        'no_texts_to_save': "Nessun testo da salvare",
        'no_valid_texts': "Nessun testo valido da salvare",
        'text_word_singular': "testo",
        'text_word_plural': "testi",
        'cross_word_singular': "croce",
        'cross_word_plural': "croci",
        'texts_saved_title': "Testi salvati",
        'texts_crosses_saved': "{0} {1} e {2} {3} sono stati inseriti nel PDF.\n\nPDF ricaricato...",
        'texts_crosses_saved_voice': "{0} {1} e {2} {3} salvati.",
        'texts_saved': "{0} {1} sono stati inseriti nel PDF.\n\nPDF ricaricato...",
        'texts_saved_voice': "{0} {1} salvati.",
        'crosses_saved': "{0} {1} sono stati inseriti nel PDF.\n\nPDF ricaricato...",
        'crosses_saved_voice': "{0} {1} salvati.",
        'elements_saved': "{0} elementi sono stati inseriti nel PDF.\n\nPDF ricaricato...",
        'elements_saved_voice': "{0} elementi salvati.",
        'text_window_load_error': "Impossibile caricare la finestra di testo",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Inserimento testo e modelli – Guida dettagliata**

        **1. Inserire e modificare testo**
        - Cliccare con il tasto destro nel punto desiderato del documento e selezionare "Inserisci testo".
        - Si apre una finestra in cui è possibile inserire e formattare il testo:
        • Dimensione carattere, Grassetto, Corsivo, Sottolineato
        • Colore del testo (libera scelta)
        • Trasparenza (opacità) tramite cursore
        • A capo automatico (varie larghezze, es. larghezza pagina, stretto, senza a capo)
        - Dopo la conferma, il testo appare nella posizione cliccata. È possibile spostarlo con il mouse o con i tasti freccia.
        - Doppio clic sul testo apre la modalità di modifica; Esc la chiude.

        **2. Gestire i modelli di testo**
        - Nella finestra di dialogo, a sinistra si vede un elenco di tutti i modelli salvati.
        - **Salvare un modello:** Inserire il testo, formattarlo e cliccare su "💾 Salva come modello". Inserire un nome file (senza estensione).
        - **Caricare un modello:** Cliccare sul nome desiderato nell'elenco. Il testo e la formattazione vengono applicati e possono essere modificati se necessario.
        - **Eliminare:** Cliccare con il tasto destro su un modello per eliminarlo o cambiarne lo stato privato/pubblico.

        **3. Modelli privati (password master)**
        - Se è stata impostata una password master (in Impostazioni → Gestione password), è possibile marcare i modelli come "privati".
        - Attivare la casella "Modello privato" nella finestra di dialogo prima di salvare.
        - I modelli privati vengono mostrati nell'elenco solo dopo aver inserito la password master una volta per sessione (autenticazione tramite l'icona del lucchetto o al primo accesso).
        - In questo modo si proteggono modelli riservati da accessi non autorizzati.

        **4. Inserire croci**
        - Tramite il menu contestuale è anche possibile inserire una croce grafica (ad esempio per caselle di controllo).
        - La dimensione, lo spessore della linea e il colore delle croci possono essere regolati globalmente nelle impostazioni (menu "Impostazioni" → "Impostazioni croci").
        - Cliccare con il tasto destro su una croce esistente per modificarla singolarmente.

        **5. Azioni collettive**
        - Se sono stati posizionati più testi o croci su una pagina, è possibile salvarli o scartarli tutti insieme tramite il menu contestuale (clic destro in modalità testo).
        - Durante il salvataggio, tutti gli elementi vengono incorporati nel PDF e rimangono come grafica vettoriale.

        **6. Scorciatoie da tastiera in modalità testo**
        - Tasti freccia: spostare elemento
        - Ctrl+Freccia: passi più grandi
        - Invio: aprire finestra di salvataggio (salva tutto / regola / scarta)
        - Esc: scartare elemento corrente
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Inserimento testo e modelli – Guida dettagliata</strong></p>

        <p><strong>1. Inserire e modificare testo</strong></p>
        <ul>
        <li>Cliccare con il tasto destro nel punto desiderato del documento e selezionare "Inserisci testo".</li>
        <li>Si apre una finestra in cui è possibile inserire e formattare il testo:<br/>
        • Dimensione carattere, Grassetto, Corsivo, Sottolineato<br/>
        • Colore del testo (libera scelta)<br/>
        • Trasparenza (opacità) tramite cursore<br/>
        • A capo automatico (varie larghezze, es. larghezza pagina, stretto, senza a capo)</li>
        <li>Dopo la conferma, il testo appare nella posizione cliccata. È possibile spostarlo con il mouse o con i tasti freccia.</li>
        <li>Doppio clic sul testo apre la modalità di modifica; Esc la chiude.</li>
        </ul>

        <p><strong>2. Gestire i modelli di testo</strong></p>
        <ul>
        <li>Nella finestra di dialogo, a sinistra si vede un elenco di tutti i modelli salvati.</li>
        <li><strong>Salvare un modello:</strong> Inserire il testo, formattarlo e cliccare su "💾 Salva come modello". Inserire un nome file (senza estensione).</li>
        <li><strong>Caricare un modello:</strong> Cliccare sul nome desiderato nell'elenco. Il testo e la formattazione vengono applicati e possono essere modificati se necessario.</li>
        <li><strong>Eliminare:</strong> Cliccare con il tasto destro su un modello per eliminarlo o cambiarne lo stato privato/pubblico.</li>
        </ul>

        <p><strong>3. Modelli privati (password master)</strong></p>
        <ul>
        <li>Se è stata impostata una password master (in Impostazioni → Gestione password), è possibile marcare i modelli come "privati".</li>
        <li>Attivare la casella "Modello privato" nella finestra di dialogo prima di salvare.</li>
        <li>I modelli privati vengono mostrati nell'elenco solo dopo aver inserito la password master una volta per sessione (autenticazione tramite l'icona del lucchetto o al primo accesso).</li>
        <li>In questo modo si proteggono modelli riservati da accessi non autorizzati.</li>
        </ul>

        <p><strong>4. Inserire croci</strong></p>
        <ul>
        <li>Tramite il menu contestuale è anche possibile inserire una croce grafica (ad esempio per caselle di controllo).</li>
        <li>La dimensione, lo spessore della linea e il colore delle croci possono essere regolati globalmente nelle impostazioni (menu "Impostazioni" → "Impostazioni croci").</li>
        <li>Cliccare con il tasto destro su una croce esistente per modificarla singolarmente.</li>
        </ul>

        <p><strong>5. Azioni collettive</strong></p>
        <ul>
        <li>Se sono stati posizionati più testi o croci su una pagina, è possibile salvarli o scartarli tutti insieme tramite il menu contestuale (clic destro in modalità testo).</li>
        <li>Durante il salvataggio, tutti gli elementi vengono incorporati nel PDF e rimangono come grafica vettoriale.</li>
        </ul>

        <p><strong>6. Scorciatoie da tastiera in modalità testo</strong></p>
        <ul>
        <li>Tasti freccia: spostare elemento</li>
        <li>Ctrl+Freccia: passi più grandi</li>
        <li>Invio: aprire finestra di salvataggio (salva tutto / regola / scarta)</li>
        <li>Esc: scartare elemento corrente</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Impostazioni croci",
        'cross_properties': "Proprietà croce",
        'cross_size': "Dimensione (px):",
        'cross_line_width': "Spessore linea:",
        'cross_color': "Colore:",
        'cross_choose_color': "Scegli",
        'cross_fine_tuning': "Regolazione fine al salvataggio (pixel)",
        'cross_offset_x': "Offset X:",
        'cross_offset_y': "Offset Y:",
        'cross_offset_x_tooltip': "Valori negativi spostano la croce a sinistra, positivi a destra",
        'cross_offset_y_tooltip': "Valori negativi spostano la croce in alto, positivi in basso",
        'cross_preview': "Anteprima",
        'cross_save': "Applica impostazioni",
        'cross_customized': "Croce personalizzata",
        'cross_settings_applied': "Impostazioni croce salvate.\nDimensione: {0}px, Spessore: {1}px\n{2}",
        'cross_updated_count': "{0} croci esistenti sono state aggiornate.",
        'cross_no_crosses': "Nessuna croce esistente trovata.",
        'cross_settings_applied_all': "Impostazioni croce applicate a tutte le {0} croci",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Impostazioni firme",
        'signature_1': "Firma 1",
        'signature_2': "Firma 2",
        'signature_select': "Seleziona firma",
        'signature_add': "➕ Aggiungi nuova firma...",
        'signature_size': "Dimensione per firma {0} (%):",
        'signature_common': "Impostazioni generali",
        'signature_timestamp': "Aggiungi automaticamente marca temporale",
        'signature_location': "Luogo predefinito:",
        'signature_timestamp_size': "Dimensione carattere marca temporale:",
        'signature_no_files': "-- Nessuna firma trovata --",
        'signature_insert': "Inserisci firma",
        'signature_insert_1': "Inserisci firma 1",
        'signature_insert_2': "Inserisci firma 2",
        'signature_customize': " Personalizza firma",
        'signature_discard': " Scarta questa firma",
        'signature_save_all': " Salva tutte le firme",
        'signature_discard_all': " Scarta tutte le firme",
        'signature_guide_title': "Firme - Guida",
        'signature_guide': """
📝 Firme - Guida rapida

- Impostare password master
- Configurare le firme nel menu Impostazioni
  (dimensione, marca temporale ...)
- Inserire con TASTO DESTRO nella posizione desiderata
  (richiede password master una volta per sessione)
- Spostare la firma con il mouse o tasti freccia
- È possibile inserire più firme in sequenza
- Ogni firma può essere personalizzata singolarmente
- Scartare una firma
- Salvare / scartare tutte le firme in una volta
- Si può anche usare la barra dei menu.
        """,
        'signature_placeholder': "Nessuna anteprima disponibile",
        'signature_info': "Firma {0}: {1}×{2} px ({3}% di {4}×{5})",
        'signature_info_placeholder': "Impostazioni per firma {0}",
        'signature_inserted': "Firma {0} inserita a pagina {1}",
        'signature_deleted': "Firma eliminata",
        'signature_copied': "Firma copiata",
        'signature_pasted': "Firma {0} incollata",
        'signature_saved': "{0} firme sono state inserite nel PDF.\n\nPDF ricaricato...",
        'signature_saved_voice': "{0} firme salvate",
        'mode_replace_signature_format': "Esci dalla modalità e inserisci firma {0}",
        'mode_conflict_voice_signature': "La modalità {0} è attiva. Uscire e inserire firma?",
        'signature_not_configured': "Firma {0} non configurata",
        'signature_file_not_found': "File firma non trovato",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nessuna firma copiata disponibile",
        'no_signatures_to_save': "Nessuna firma da salvare",
        'signature_save_question': "Salvare tutte le firme, regolare o scartare questa?",
        'signatures_saved_title': "Firme salvate",
        'signatures_saved': "{0} firme sono state inserite nel PDF.\n\nPDF ricaricato...",
        'signatures_saved_voice': "{0} firme salvate.",
        'all_signatures_discarded': "Tutte le firme scartate",
        'signature_settings_saved': "Impostazioni firma salvate",
        'signature_cancelled': "Firma scartata",
        'signature_active_title': "Firma attiva",
        'signature_replace_question': "Una firma è già attiva.\n\nSostituire la firma corrente?",
        'signature_replace': "Sostituisci firma",
        'signature_replace_voice': "Sostituire la firma corrente o annullare?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Impostazioni immagine",
        'image_common': "Impostazioni generali immagine",
        'image_keep_aspect': "Mantieni proporzioni durante il trascinamento",
        'image_default_size': "Dimensione predefinita (%):",
        'image_dark_invert': "Inverti immagini in modalità scura",
        'image_dark_invert_tooltip': "Attivato: le immagini vengono invertite per una migliore visibilità",
        'image_fine_tuning': "Regolazione fine (pixel)",
        'image_offset_x': "Offset X:",
        'image_offset_y': "Offset Y:",
        'image_offset_x_tooltip': "Valori negativi spostano l'immagine a sinistra, positivi a destra",
        'image_offset_y_tooltip': "Valori negativi spostano l'immagine in alto, positivi in basso",
        'image_select': "Seleziona immagine",
        'image_insert': "Inserisci immagine",
        'image_customize': " Personalizza immagine",
        'image_aspect': " Mantieni proporzioni",
        'image_discard': " Scarta questa immagine",
        'image_save_all': " Salva tutte le immagini",
        'image_discard_all': " Scarta tutte le immagini",
        'image_filter': "Immagini",
        'image_guide_title': "Inserisci immagine - Guida",
        'image_guide': """
📷 Inserisci immagine in PDF - Guida rapida:

1. Tasto destro nella posizione desiderata
2. "Inserisci immagine" → seleziona immagine
3. Posizionare l'immagine: trascinare con il mouse
4. Regolare dimensioni: trascinare gli angoli/lati
5. Mantieni proporzioni: tasto [A]
6. Altre regolazioni: tasto destro sull'immagine

Consiglio: è possibile regolare le impostazioni nel menu contestuale.
        """,
        'image_inserted': "Immagine {0} inserita a pagina {1}",
        'image_deleted': "Immagine scartata",
        'image_copied': "Immagine copiata",
        'image_pasted': "Immagine incollata",
        'image_saved': "{0} immagini sono state inserite nel PDF.\n\nPDF ricaricato...",
        'image_saved_voice': "{0} immagini salvate",
        'image_aspect_on': "attivato",
        'image_aspect_off': "disattivato",
        'image_aspect_toggle': "Mantieni proporzioni {0}",
        'image_reset': "Immagine ripristinata a dimensione originale",
        'image_replaced': "Immagine sostituita",
        'image_invalid': "Immagine non valida",
        'mode_replace_image': "Inserisci immagine",
        'mode_conflict_voice_image': "La modalità {0} è attiva. Uscire e inserire immagine?",
        'image_active_title': "Immagine attiva",
        'image_replace_question': "Un'immagine è già attiva.\n\nSostituire l'immagine corrente?",
        'image_replace': "Sostituisci immagine",
        'image_replace_voice': "Sostituire l'immagine corrente o annullare?",
        'image_filter_all': "Immagini (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Tutti i file (*.*)",
        'no_copied_image': "Nessuna immagine copiata disponibile",
        'image_discarded': "Immagine scartata",
        'image_save_question': "Salvare tutte le immagini, regolare o scartare questa?",
        'no_images_to_save': "Nessuna immagine da salvare",
        'no_valid_images': "Nessuna immagine valida da salvare",
        'images_saved_title': "Immagini salvate",
        'images_saved': "{0} immagini sono state inserite nel PDF.\n\nPDF ricaricato...",
        'images_saved_voice': "{0} immagini salvate.",
        'all_images_discarded': "Tutte le immagini scartate",
        'image_settings_updated': "Impostazioni immagine aggiornate",
        'image_replace_title': "Seleziona nuova immagine",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Impostazioni forme",
        'form_basic': "Impostazioni di base",
        'form_default_type': "Tipo forma predefinito:",
        'form_rectangle': "Rettangolo",
        'form_ellipse': "Ellisse",
        'form_line': "Linea",
        'form_arrow': "Freccia",
        'form_line_width': "Spessore linea:",
        'form_colors': "Colori",
        'form_line_color': "Colore linea:",
        'form_fill_color': "Colore di riempimento:",
        'form_choose_color': "Scegli",
        'form_transparent': "Sfondo trasparente (solo linea)",
        'form_filled': "riempito",
        'form_dark_mode': "Modalità scura",
        'form_dark_invert': "Inverti colori in modalità scura",
        'form_fine_tuning': "Regolazione fine (pixel)",
        'form_offset_x': "Offset X:",
        'form_offset_y': "Offset Y:",
        'form_offset_x_tooltip': "Valori negativi spostano la forma a sinistra, positivi a destra",
        'form_offset_y_tooltip': "Valori negativi spostano la forma in alto, positivi in basso",
        'form_preview': "Anteprima",
        'form_insert': "Inserisci forma",
        'form_rectangle_insert': "Rettangolo",
        'form_ellipse_insert': "Ellisse/Cerchio",
        'form_line_insert': "Linea (2 clic)",
        'form_arrow_insert': "Freccia (2 clic)",
        'form_customize': " Personalizza forma",
        'form_transparent_toggle': " Sfondo trasparente",
        'form_discard': " Scarta questa forma",
        'form_save_all': " Salva tutte le forme",
        'form_discard_all': " Scarta tutte le forme",
        'form_guide_title': "Inserisci forma - Guida",
        'form_guide': """
📐 Inserisci forma in PDF - Guida rapida:

1. Scegliere il tipo di forma (rettangolo, ellisse, linea, freccia)
2. Cliccare nella posizione desiderata
   - Per rettangolo/ellisse: un clic posiziona la forma
   - Per linea/freccia: due clic per punto iniziale e finale
3. Posizionare la forma: trascinare con il mouse
4. Regolare dimensioni: trascinare gli angoli/lati
5. Salvare la forma: Invio
6. Scartare la forma: Esc
7. Altre regolazioni: tasto destro sulla forma

Consiglio: è possibile regolare le impostazioni nel menu contestuale.
        """,
        'form_inserted': "{0} inserita a pagina {1}",
        'form_deleted': "Forma eliminata",
        'form_copied': "Forma copiata",
        'form_pasted': "Forma incollata",
        'form_saved': "{0} forme sono state inserite nel PDF.\n\nPDF ricaricato...",
        'form_saved_voice': "{0} forme salvate",
        'form_reset': "Forma ripristinata a dimensione predefinita",
        'form_transparent_on': "attivato",
        'form_transparent_off': "disattivato",
        'form_transparent_toggled': "Sfondo trasparente {0}",
        'form_line_cancel': "Disegno linea annullato",
        'form_second_click': "Ora fare clic sul punto finale per {0}",
        'mode_replace_form': "Inserisci forma",
        'mode_conflict_voice_form': "La modalità {0} è attiva. Uscire e inserire una forma?",
        'form_settings_updated': "Impostazioni forma aggiornate",
        'form_unknown': "Forma",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Fare clic sulla posizione iniziale",
        'form_line_guide_2': "2. Fare clic sulla posizione finale",
        'form_line_guide_3': "La linea verrà disegnata tra i due punti.",
        'form_line_status_1': "In attesa del primo clic...",
        'form_line_status_2': "Primo punto impostato: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Ora fare clic sul punto finale...",
        'form_line_status_4': "Entrambi i punti impostati.\nFare clic su 'Fine' per salvare.",
        'form_line_reset': "Reimposta",
        'form_line_finish': "Fine",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Copia (Cmd+C)",
        'paste': "Incolla (Cmd+V)",
        'copied': "Copiato: {0}",
        'no_element_to_copy': "Nessun elemento selezionato da copiare",
        'no_copied_data': "Nessun dato copiato disponibile",
        'no_valid_position': "Posizione non valida per incollare",
        'copy_text': "Testo copiato",
        'copy_image': "Immagine copiata",
        'copy_form': "Forma copiata",
        'copy_signature': "Firma copiata",
        'element_text': "testo",
        'element_image': "immagine",
        'element_form': "forma",
        'element_signature': "firma",
        'element_unknown': "elemento",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Conflitto di modalità",
        'mode_conflict_message': "La modalità '{0}' è già attiva.\n\nUscire da essa e {1}?",
        'mode_replace': "Esci dalla modalità e {0}",
        'mode_cancel': "Annulla",
        'mode_replace_text': "inserisci testo",
        'mode_replace_cross': "inserisci croce",
        'mode_replace_signature': "inserisci firma",
        'mode_replace_image': "inserisci immagine",
        'mode_replace_form': "inserisci forma",
        'mode_conflict_voice': "La modalità {0} è attiva. Uscire e inserire testo?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Inserimento testo",
        'active_mode_signature': "Firma",
        'active_mode_image': "Immagine",
        'active_mode_form': "Forma",
        'active_mode_and': " e ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Inserisci",                    # Hauptmenü
        'insert_another_text': "Inserisci testo",          # Vereinfacht
        'insert_another_cross': "Inserisci croce",        # Vereinfacht
        'insert_another_signature_1': "Firma 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Firma 2",      # Untermenü-Eintrag
        'insert_another_image': "Inserisci immagine",         # Vereinfacht
        'insert_another_form_rect': "Rettangolo",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellisse",        # Untermenü-Eintrag
        'insert_another_form_line': "Linea (2 clic)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Freccia (2 clic)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Salva {0}",
        'save_dialog_message': "{0} verrà salvato/a alla pagina {1}.\n\nCome procedere?",
        'save_all': "Salva tutti i {0}",
        'save_single': "Salva {0}",
        'save_customize': "Personalizza {0}",
        'save_discard': "Scarta {0}",
        'save_continue': "Continua modifica",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Vai a pagina {0}",
        'context_rotate': " Ruota pagina {0}",
        'context_delete': " Elimina pagina {0}",
        'context_export': " Esporta pagina {0}",
        'context_mark_as': " Marca pagina come...",
        'context_mark_empty': " Pagina vuota",
        'context_unmark_empty': " Non più vuota",
        'context_mark_export': " Marca per esportazione",
        'context_unmark_export': " Non esportare",
        'context_batch_actions': " Azioni collettive",
        'context_batch_delete_empty': " Elimina le {0} pagine vuote",
        'context_batch_export_single': " Tutte le {0} pagine (un file)",
        'context_batch_export_split': " Tutte le {0} pagine (separate)",
        'context_drag_start': " Attiva drag & drop",
        'context_drag_stop': " Disattiva drag & drop",
        'context_insert': " Inserisci",
        'context_insert_pages': " Inserisci pagine",
        'context_zoom': "Zoom",
        'discard_mixed': "Scarta {0} {1} e {2} {3}",
        'save_mixed': "Salva {0} {1} e {2} {3}",
        'discard_texts': "Scarta {0} testi",
        'discard_text_single': "Scarta 1 testo",
        'save_texts': "Salva {0} testi",
        'save_text_single': "Salva 1 testo",
        'discard_crosses': "Scarta {0} croci",
        'discard_cross_single': "Scarta 1 croce",
        'save_crosses': "Salva {0} croci",
        'save_cross_single': "Salva 1 croce",
        'discard_signatures': "Scarta {0} firme",
        'save_signature_single': "Salva 1 firma",
        'save_signatures': "Salva {0} firme",
        'discard_images': "Scarta {0} immagini",
        'save_image_single': "Salva 1 immagine",
        'save_images': "Salva {0} immagini",
        'discard_forms': "Scarta {0} forme",
        'save_form_single': "Salva 1 forma",
        'save_forms': "Salva {0} forme",
        'cross_discard': "Scarta questa croce",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informazioni esportazione/importazione",
        'export_what': "📋 Cosa viene esportato?",
        'export_general': "Impostazioni generali",
        'export_general_items': "• Sintesi vocale (on/off, velocità)\n• Modalità scura/chiara\n• Impostazioni backup\n• Impostazioni OCR",
        'export_image_form': "Impostazioni immagini e forme",
        'export_image_form_items': "• Impostazioni immagini (proporzioni, dimensione predefinita)\n• Impostazioni forme (spessore linea, colori)\n• Impostazioni firme (percorsi, dimensioni, marca temporale)",
        'export_passwords': "Database password",
        'export_passwords_items': "• Tutte le password PDF salvate\n• A scelta cifrate o decifrate",
        'export_master': "Impostazioni password master",
        'export_master_items': "• Hash password master\n• Impostazioni per firme/modelli di testo",
        'export_signatures': "Firme e modelli di testo",
        'export_signatures_items': "• Tutti i file immagine (firme)\n• Tutti i modelli di testo con formattazione\n• Marcature privato/pubblico",
        'export_import_warning': "⚠️ Note importanti",
        'export_import_note': "• Durante l'importazione, TUTTE le impostazioni attuali vengono sovrascritte\n• È necessario riavviare l'applicazione\n• Le firme/modelli esistenti verranno sostituiti",
        'export_master_note': "• Se è impostata una password master, è possibile scegliere:\n  - Decifrato (password in chiaro)\n  - Cifrato (leggibile solo con password master)",
        'export_security': "• Il file ZIP esportato contiene dati riservati\n• Conservarlo in un luogo sicuro (es. chiavetta USB cifrata)\n• In caso di perdita del file, le password sono irrecuperabili",
        'export_format': "📁 Formato di esportazione",
        'export_format_desc': "Le impostazioni vengono salvate in un unico file ZIP:",
        'export_filename': "PDFDarkView_Settings_AAAAMMGG_HHMMSS.zip",
        'export_success': "Impostazioni esportate con successo",
        'export_failed': "Esportazione fallita",
        'export_import_question': "Riavviare l'applicazione ora?",
        'export_password_question': "È impostata una password master.\n\nEsportare le password decifrate?\n(altrimenti verranno esportate cifrate)",
        'export_decrypt': "Esporta decifrate",
        'export_encrypt': "Esporta cifrate",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Informazioni su PDF Dark View",
        'info_version': "Versione",
        'info_author': "Sviluppato da Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Informazioni",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> è un visualizzatore PDF accessibile, sviluppato appositamente per persone con disabilità visiva.</p>

            <p><strong>Caratteristiche principali:</strong></p>
            <ul>
                <li>Interfaccia ad alto contrasto e personalizzabile</li>
                <li>Controllo completo tramite tastiera</li>
                <li>Sintesi vocale integrata</li>
                <li>OCR per documenti scannerizzati</li>
                <li>Strumenti di modifica completi</li>
            </ul>

            <p>Oltre 50 lingue sono supportate – per rendere i PDF accessibili a tutti.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funzionalità",
        'info_features_intro': "PDF Dark View vi offre le seguenti possibilità:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Visualizzazione e navigazione</strong> – Modalità scura/chiara, sfogliare le pagine, zoom, salta a pagina</li>
            <li><strong>OCR (riconoscimento testo)</strong> – Rendi i documenti scannerizzati ricercabili e copiabili</li>
            <li><strong>Modifica</strong> – Inserisci testo, croci, firme, immagini e forme</li>
            <li><strong>Gestione pagine</strong> – Elimina, estrai, inserisci, sposta tramite trascinamento</li>
            <li><strong>Esportazione</strong> – In Word, Pages o come testo</li>
            <li><strong>Sicurezza</strong> – Protezione e gestione tramite password</li>
            <li><strong>Accessibilità</strong> – Sintesi vocale, controllo tramite tastiera, alto contrasto</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Utilizzo",
        'info_accessibility': "♿ Accessibilità – controllo completo tramite tastiera",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Generale</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Apri PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Cerca</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Commuta modalità scura/chiara</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Stampa</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Esci</div>

        <div class="shortcut-cat">📖 Navigazione</div>
        <div class="shortcut-row"><kbd>Frecce</kbd> Sfoglia pagina per pagina</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Vai alla pagina</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Prima pagina</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Ultima pagina</div>

        <div class="shortcut-cat">✏️ Modifica</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Inserisci testo</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Elimina pagine</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Estrai pagine</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Inserisci pagine</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Sposta pagine</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Ruota pagina</div>

        <div class="shortcut-cat">🖼️ Spostare elementi</div>
        <div class="shortcut-row"><kbd>Frecce</kbd> Sposta testo/immagine/firma</div>
        <div class="shortcut-row"><kbd>Ctrl+Frecce</kbd> Passi più grandi</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Salva</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Annulla</div>

        <div class="shortcut-cat">🗣️ Sintesi vocale</div>
        <div class="shortcut-row"><kbd>F2</kbd> Attiva/disattiva sintesi vocale</div>
        """,
        'info_contextmenu': "📌 Importante: Tutte le funzioni sono disponibili anche tramite il menu contestuale (tasto destro del mouse)!",
        'info_accessibility_hint': "💡 Suggerimento: La sintesi vocale (F2) facilita l'orientamento e fornisce feedback su menu e finestre di dialogo.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licenza & Note legali",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 NOTE LEGALI</strong><br>
        Informazioni ai sensi del § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germania<br>
        E-mail: binhdiez64@gmail.com<br>
        Responsabile del contenuto: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Esclusione di responsabilità</strong><br>
        Il software è stato sviluppato con la massima cura. Non viene fornita alcuna garanzia per la correttezza, completezza e funzionalità. L'utilizzo avviene a proprio rischio.<br><br>

        <strong>📄 Licenza MIT (uso privato)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Consentito: uso gratuito, modifiche private, copie personali.<br>
        Non consentito: vendita, uso commerciale, rimozione delle note di copyright.<br><br>

        <strong>🔧 Componenti di terze parti</strong><br>
        Questo software contiene componenti sotto licenze GPL, AGPL, Apache 2.0, BSD e MIT.<br>
        In caso di ridistribuzione, è necessario rispettare i rispettivi termini di licenza.<br><br>

        <strong>🌐 Open Source</strong><br>
        Il codice sorgente è disponibile e può essere visualizzato, modificato e ridistribuito secondo i rispettivi termini di licenza.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Ringraziamenti",
        'info_credits': "Grazie alla comunità open source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Elaborazione PDF</li>
            <li><strong>PyQt5</strong> – Interfaccia grafica</li>
            <li><strong>Tesseract OCR</strong> – Riconoscimento testo</li>
            <li><strong>OCRmyPDF</strong> – Integrazione OCR</li>
            <li><strong>python-docx</strong> – Esportazione in Word</li>
            <li><strong>qtawesome</strong> – Icone</li>
            <li><strong>DeepSeek</strong> – Supporto per le traduzioni (50+ lingue)</li>
            <li><strong>Tutti gli utenti</strong> – Per il prezioso feedback</li>
            <li><strong>La comunità open source</strong> – Per le fantastiche librerie</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Lingue",
        'info_languages_header': "🌍 Supporto linguistico",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View supporta attualmente <strong>62 lingue</strong> – in modo che il software possa essere utilizzato in modo accessibile in tutto il mondo.</p>

            <p><strong>📖 Elenco completo delle lingue (Stato: marzo 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanese (Shqip)</li>
                    <li>🇩🇿 Arabo (العربية)</li>
                    <li>🇮🇩 Balinese (Basa Bali)</li>
                    <li>🇧🇩 Bengalese (বাংলা)</li>
                    <li>🇲🇲 Birmano (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosniaco (Bosanski)</li>
                    <li>🇧🇬 Bulgaro (Български)</li>
                    <li>🇨🇳 Cinese (中文)</li>
                    <li>🇩🇰 Danese (Dansk)</li>
                    <li>🇩🇪 Tedesco (Deutsch)</li>
                    <li>🇬🇧 Inglese (English)</li>
                    <li>🇪🇪 Estone (Eesti)</li>
                    <li>🇫🇮 Finlandese (Suomi)</li>
                    <li>🇫🇷 Francese (Français)</li>
                    <li>🇬🇷 Greco (Ελληνικά)</li>
                    <li>🇮🇱 Ebraico (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croato (Hrvatski)</li>
                    <li>🇭🇺 Ungherese (Magyar)</li>
                    <li>🇮🇩 Indonesiano (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandese (Gaeilge)</li>
                    <li>🇮🇸 Islandese (Íslenska)</li>
                    <li>🇮🇹 Italiano (Italiano)</li>
                    <li>🇯🇵 Giapponese (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Coreano (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Lettone (Latviešu)</li>
                    <li>🇱🇹 Lituano (Lietuvių)</li>
                    <li>🇱🇺 Lussemburghese (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malese (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolo (Монгол)</li>
                    <li>🇳🇵 Nepalese (नेपाली)</li>
                    <li>🇳🇱 Olandese (Nederlands)</li>
                    <li>🇳🇴 Norvegese (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persiano (فارسی)</li>
                    <li>🇵🇱 Polacco (Polski)</li>
                    <li>🇵🇹 Portoghese (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumeno (Română)</li>
                    <li>🇷🇺 Russo (Русский)</li>
                    <li>🇸🇪 Svedese (Svenska)</li>
                    <li>🇷🇸 Serbo (Српски)</li>
                    <li>🇸🇰 Slovacco (Slovenčina)</li>
                    <li>🇸🇮 Sloveno (Slovenščina)</li>
                    <li>🇪🇸 Spagnolo (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thailandese (ไทย)</li>
                    <li>🇨🇿 Ceco (Čeština)</li>
                    <li>🇹🇷 Turco (Türkçe)</li>
                    <li>🇺🇦 Ucraino (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamita (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Aggiungi le tue lingue:</strong><br>
                Desideri una lingua che non è ancora inclusa? Basta posizionare il tuo file del dizionario (<code>sprache_xx.py</code>) accanto all'applicazione – il software lo riconoscerà automaticamente. Se sei interessato a una traduzione specifica, contattami pure.
            </div>

            <p><strong>🙏 Ringraziamento speciale:</strong> A DeepSeek per il supporto nella traduzione di tutti i dizionari in 62 lingue.</p>

            <p>📧 Contatto per traduzioni: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Errore",
        'error_occurred': "Si è verificato un errore",
        'error_pdf_load': "Errore durante il caricamento del PDF",
        'error_pdf_save': "Errore durante il salvataggio del PDF",
        'error_ocr': "Errore durante il riconoscimento del testo",
        'error_no_pdf': "Nessun PDF caricato",
        'error_page_not_found': "Pagina non trovata",
        'error_invalid_range': "Intervallo di pagine non valido",
        'error_file_not_found': "File non trovato",
        'error_permission': "Permesso negato",
        'error_unknown': "Errore sconosciuto",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Successo",
        'success_operation': "Operazione completata con successo",
        'success_saved': "Salvato con successo",
        'success_exported': "Esportato con successo",
        'success_imported': "Importato con successo",
        'success_deleted': "Eliminato con successo",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Conferma",
        'confirm_yes': "Sì",
        'confirm_no': "No",
        'confirm_ok': "OK",
        'confirm_cancel': "Annulla",
        'confirm_delete': "Elimina",
        'confirm_overwrite': "Sovrascrivi",
        'confirm_continue': "Continua",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Caricamento PDF...",
        'progress_saving': "Salvataggio PDF...",
        'progress_exporting': "Esportazione PDF...",
        'progress_processing': "Elaborazione in corso...",
        'progress_wait': "Attendere prego...",
        'progress_preparing': "Preparazione...",
        'progress_finalizing': "Finalizzazione...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Bianco",
        'color_black': "Nero",
        'color_red': "Rosso",
        'color_green': "Verde",
        'color_blue': "Blu",
        'color_yellow': "Giallo",
        'color_magenta': "Magenta",
        'color_cyan': "Ciano",
        'color_orange': "Arancione",
        'color_gray': "Grigio",
        'color_custom': "Selettore colore",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&File",
        'menu_edit': "&Modifica",
        'menu_view': "&Visualizza",
        'menu_tools': "&Strumenti",
        'menu_settings': "&Impostazioni",
        'menu_help': "&Aiuto",
        'menu_language': "🌐 Lingua",
        'menu_guides': "&Guide",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Apri",
        'file_save_as': "&Salva con nome...",
        'file_protect': "&Proteggi documento...",
        'file_export': "&Esporta",
        'file_export_pages': "Esporta in Pages",
        'file_export_word': "Esporta in DOCX",
        'file_export_text': "Esporta in TXT",
        'file_print_now': "&Stampa subito",
        'file_print': "&Stampa",
        'file_close': "&Chiudi",
        'file_quit': "&Esci",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Cerca",
        'edit_ocr': " Esegui OCR",
        'edit_rotate': "&Ruota pagina",
        'edit_rotate_all': "&Ruota tutte le pagine",
        'edit_delete_pages': "&Elimina pagine",
        'edit_extract_pages': "&Estrai pagine",
        'edit_insert_pages': "&Inserisci pagine",
        'edit_move_pages': "&Sposta pagine",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Inserisci testo e croci",
        'text_insert': " Inserisci testo",
        'cross_insert': " Inserisci croce",
        'text_customize': " Personalizza testo",
        'cross_customize': " Personalizza questa croce",
        'cross_customize_all': " Personalizza tutte le croci",
        'text_discard': " Scarta questo testo / questa croce",
        'text_discard_all': " Scarta tutti i testi e croci",
        'text_save_all': " Salva tutti i testi e croci",
        'text_guide': " Inserimento testo / modelli - Guida",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Inserisci firma",
        'signature_settings_menu': " Impostazioni...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Inserisci immagine",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Inserisci forme",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Mostra finestra testo",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Larghezza pagina (predefinito)",
        'view_zoom_two': "&Due pagine",
        'view_zoom_overview': "&Panoramica (più pagine)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Accessibilità",
        'settings_voice': "Sintesi vocale",
        'settings_voice_tooltip': "integra la sintesi vocale degli screen reader con informazioni aggiuntive",
        'settings_signature': "&Impostazioni firma",
        'settings_password': "&Gestione password",
        'settings_backup': "Crea backup prima delle modifiche",
        'settings_export_import': "&Esporta / importa impostazioni",
        'settings_export': "&Esporta tutte le impostazioni...",
        'settings_import': "&Importa tutte le impostazioni...",
        'settings_export_info': "&Cosa viene esportato?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "attivata",
        'voice_off': "disattivata",
        'voice_toggle': "Sintesi vocale {0}",
        'voice_speed': "Velocità al {0} per cento",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Strumento non trovato:\n{0}\n\nBASE_DIR: {1}\nAssicurarsi che gli strumenti PDF siano installati nella directory {1}.",
        'tool_started': "{0} avviato",
        'tool_start_failed': "Impossibile avviare",
        'process_error_failed_to_start': "Impossibile avviare il processo. Il file esiste?",
        'process_error_crashed': "Il processo si è arrestato durante l'avvio.",
        'process_error_timeout': "Timeout del processo raggiunto.",
        'process_error_write': "Errore di scrittura nel processo.",
        'process_error_read': "Errore di lettura dal processo.",
        'process_error_unknown': "Errore di processo sconosciuto",
        'process_command': "Comando",
        'process_normal_exit': "terminato normalmente",
        'process_crashed': "arrestato",
        'process_nonzero_exit': "{0} terminato con codice di errore {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Annullamento in corso...",
        'move_cancelling': "Annullamento spostamento",
        'opening_pdf': "Apertura PDF...",
        'loading_document': "Caricamento documento...",
        'pdf_opened': "PDF aperto",
        'pages_found_moving': "{0} pagine trovate, {1} da spostare",
        'creating_backup': "Creazione backup...",
        'backup_description': "Backup file originale...",
        'backup_saved_as': "Backup salvato come: {0}",
        'error_format': "Errore: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Ricerca azzerata",
        'page_header_simple': "=== Pagina {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Gestione password – Guida",
        'password_guide_voice': "Guida alla gestione delle password. Si prega di leggere le note.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Gestione password – Guida dettagliata</strong></p>

        <p><strong>1. Protezione con password dei PDF</strong></p>
        <ul>
        <li>All'apertura di un PDF protetto da password, appare una finestra in cui inserire la password.</li>
        <li>È possibile salvare la password cifrata per non doverla reinserire ogni volta (casella "Salva password").</li>
        <li>Con il pulsante "Rimuovi password" è possibile creare una copia decifrata del PDF ed eliminare la password dal database.</li>
        </ul>

        <p><strong>2. Password master</strong></p>
        <ul>
        <li>La password master protegge l'accesso a tutte le password PDF salvate.</li>
        <li><strong>Impostazione:</strong> Vai su "Impostazioni → Gestione password → Impostazioni password master" e clicca "Imposta password master". Scegli una password sicura (almeno 8 caratteri).</li>
        <li><strong>Modifica:</strong> Dopo l'autenticazione riuscita, puoi cambiare la password master.</li>
        <li><strong>Rimozione:</strong> Se elimini la password master, TUTTE le password salvate vengono cancellate irreversibilmente. Puoi esportare un backup prima.</li>
        <li>Una volta per sessione devi autenticarti con la password master per accedere a funzioni protette (ad es. visualizzare le password).</li>
        </ul>

        <p><strong>3. Gestione password (elenco)</strong></p>
        <ul>
        <li>In "Impostazioni → Gestione password" si apre una tabella di tutti i PDF salvati con le loro password cifrate.</li>
        <li><strong>Senza password master:</strong> Puoi solo eliminare voci – le password rimangono nascoste.</li>
        <li><strong>Con password master (autenticato):</strong> Puoi visualizzare, copiare, esportare ed eliminare password.</li>
        <li><strong>Esportazione:</strong> Scegli un formato (JSON, CSV, TXT) e salva l'elenco. Se è impostata una password master, puoi decidere se esportare le password in chiaro o ancora cifrate.</li>
        <li><strong>Importazione:</strong> Un file ZIP esportato in precedenza con tutte le impostazioni (incluse password) può essere reimportato tramite "Impostazioni → Esporta/importa impostazioni". Attenzione: i dati esistenti verranno sovrascritti!</li>
        </ul>

        <p><strong>4. Generatore di password</strong></p>
        <ul>
        <li>Nella finestra di dialogo della password (ad esempio durante la protezione di un PDF) trovi un pulsante a forma di dado 🎲 a destra del campo di inserimento.</li>
        <li>Cliccalo per aprire il generatore di password. Puoi impostare lunghezza, set di caratteri (maiuscole, minuscole, cifre, simboli) e un separatore per una migliore leggibilità.</li>
        <li>La password generata può essere utilizzata direttamente e copiata se necessario.</li>
        </ul>

        <p><strong>5. Note di sicurezza importanti</strong></p>
        <ul>
        <li>Le password salvate vengono archiviate crittografate con AES-256. La chiave viene derivata dalla tua password master (se impostata) o da un valore fisso (senza password master).</li>
        <li>Senza password master, le password sono comunque crittografate, ma la chiave è incorporata nel programma – un aggressore con accesso ai tuoi file potrebbe decifrarle. Si consiglia vivamente di usare una password master.</li>
        <li>Il database delle password si trova nella directory `Data/passwords.json`. Esegui backup regolari, specialmente prima di rimuovere la password master.</li>
        <li>In caso di perdita della password master, tutte le password salvate sono irrecuperabili.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Modalità di inversione",
        'invert_mode_classic': "Classica (inverti tutti i colori)",
        'invert_mode_smart': "Intelligente (inverti solo la luminosità)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Soglia scala di grigi",
        'gray_threshold_10': "10% (rigoroso)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Predefinito)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (morbido)",
        'threshold_changed': "Soglia impostata su {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Soglia scala di grigi – Spiegazione",
        'threshold_guide_text': "La soglia della scala di grigi determina quali pixel nella modalità scura intelligente sono considerati 'grigi' e vengono invertiti.\n\n"
                                "• Un valore basso (10%) inverte solo tonalità di grigio quasi perfette – gli elementi colorati rimangono completamente preservati.\n"
                                "• Un valore alto (50%) inverte anche pixel leggermente colorati – questo aumenta il contrasto, ma può distorcere i colori.\n\n"
                                "Il valore ottimale dipende dal documento. Per documenti puramente testuali, 30–40% è spesso ideale, per grafiche colorate piuttosto 10–20%.\n\n"
                                "È possibile regolare il valore in qualsiasi momento tramite il menu 'Impostazioni' – il PDF verrà quindi ricaricato immediatamente.\n\n"
                                "Nota:\n* Foto e immagini possono essere visualizzate correttamente solo in modalità chiara!\n* Le impostazioni di inversione vengono visualizzate solo quando la modalità scura è attivata.",
        'threshold_guide_voice': "La soglia della scala di grigi determina quanto interviene la modalità scura intelligente. Un valore basso preserva i colori, un valore alto aumenta il contrasto.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Apertura PDF...",
        'progress_loading_document': "Caricamento documento...",
        'progress_pdf_opened': "PDF aperto",
        'progress_creating_backup': "Creazione backup...",
        'progress_backup_description': "Protezione file originale...",
        'progress_backup_created': "Backup creato",
        'progress_backup_saved_as': "Salvato come: {0}",
        'progress_analyzing_start': "Avvio analisi...",
        'progress_searching_empty': "Ricerca pagine vuote...",
        'progress_page_empty': "Pagina {0} è vuota",
        'progress_page_keep': "Mantieni pagina {0}",
        'progress_analysis_complete': "Analisi completata",
        'progress_empty_found': "Trovate {0} pagine vuote",
        'progress_current_page': "Pagina corrente",
        'progress_mark_delete': "Segnato per l'eliminazione",
        'progress_range_selected': "Intervallo pagine {0}-{1}",
        'progress_deleting_pages': "Eliminazione di {0} pagine",
        'progress_creating_new_pdf': "Creazione nuovo PDF...",
        'progress_transferring_pages': "Trasferimento pagine",
        'progress_keeping_page': "La pagina {0} verrà mantenuta ({1}/{2})",
        'progress_saving_pdf': "Salvataggio PDF...",
        'progress_optimizing': "Ottimizzazione dimensione file...",
        'progress_finalizing': "Finalizzazione...",
        'progress_new_size': "Nuova dimensione: {0:.2f} MB",
        'progress_cancelling': "Annullamento...",
        'progress_cancel_message': "{0} in fase di annullamento",
        'progress_pages_found_moving': "Trovate {0} pagine, {1} da spostare",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analisi PDF...",
        'ocr_status_optimizing': "Ottimizzazione immagine in corso...",
        'ocr_status_recognizing': "Riconoscimento testo in corso...",
        'ocr_status_embedding': "Incorporamento testo...",
        'ocr_status_finalizing': "Finalizzazione PDF...",

        # PDF-Laden
        'progress_preparing': "Preparazione...",
        'progress_loading': "Caricamento PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Eliminazione pagine...",
        'progress_moving_title': "Spostamento pagine...",
        'pages_found': "Pagine trovate",
        'progress_creating_new_order': "Creazione nuovo ordine...",
        'progress_sorting_pages': "Ordinamento pagine...",
        'progress_moving_to_begin': "Sposta {0} pagine all'inizio",
        'progress_transferring_count': "Trasferisci {0} pagine",
        'progress_transferring_before_target': "Trasferisci pagine prima della destinazione",
        'progress_moving_pages': "Sposta {0} pagine",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_protetto_",
        'filename_copy_suffix': "_Copia",
        'filename_page_single': "_Pagina_",
        'filename_page_range': "_Pagine_",
        'filename_export_page': "_Pagina_{0:03}",
        'filename_export_range': "_Pagine_{0}-{1}",
        'filename_export_multiple': "_Pagine_{0}",
        'filename_with_text': "_con_Testo",
        'filename_with_signature': "_con_Firma",
        'filename_with_image': "_con_Immagine",
        'filename_with_forms': "_con_Forme",
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
        'view_toggle_navbar': "Mostra barra pulsanti",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Impossibile eliminare tutte le pagine",
		'pages_cannot_delete_last_page': 'L\'ultima pagina non può essere eliminata!',
		'pages_cannot_delete_all_pages': 'Almeno una pagina deve rimanere nel documento!',
		'delete_pages_confirm': 'Sei sicuro di voler eliminare {0} pagine?',
		'delete_pages_confirm_voice': 'Sei sicuro di voler eliminare {0} pagine?',
		'pages_deleted': '{0} pagine sono state eliminate con successo.',
		'warning': 'Attenzione',
		'error': 'Errore',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nessun modulo selezionato",
        'form_customized': "Modulo personalizzato",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Seleziona",
        'btn_use': "Usa",
        'master_password_for_spasswords': "Per salvare e utilizzare le password, è necessario innanzitutto impostare una password master.\n\nVuoi impostare la password master ora?",
        'open_saved_dialog_title': "Apri file salvato",
        'open_saved_question': "Vuoi aprire il file salvato ora?",
        'password': "Password",
        'password_manager_master_required': "Il gestore password è disponibile solo se è stata impostata una password master.\n\nVuoi impostare la password master ora?",
        'password_master_required_for_select': "Per visualizzare e selezionare le password salvate, devi prima autenticarti con la tua password master.\n\nVuoi autenticarti ora?",
        'password_not_available': "La password selezionata non è disponibile o non può essere decrittografata.",
        'password_options_title': "Opzioni password",
        'password_save_choice_change': "Imposta nuova password",
        'password_save_choice_keep': "Usa password esistente",
        'password_save_choice_none': "Salva non crittografato",
        'password_save_hint': "Imposta prima una password master per salvare le password in modo sicuro.",
        'password_save_master_required': "Salva password (possibile solo con password master)",
        'password_save_question': "Il PDF corrente è protetto da password. Vuoi usare la password esistente, impostarne una nuova o salvare non crittografato?",
        'password_select': "Seleziona password",
        'password_select_none': "Nessuna password selezionata.\n\nSeleziona una password dall'elenco.",
        'password_select_one': "Seleziona esattamente una password.\n\nHai contrassegnato più password.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",
        'filename_insert_suffix': "_con_inserimento",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_pagine_eliminate",
        'filename_pages_moved': "_pagine_spostate",
        'filename_rotated_all_suffix': "_tutte_le_pagine_ruotate",
        'filename_rotated_suffix': "_pagina_ruotata",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configurazione dei nomi file durante le modifiche al PDF",
        'filename_keep_suffixes': "Mantieni le estensioni precedenti (es. _con_testo)",
        'filename_keep_suffixes_false': "Sostituisci",
        'filename_keep_suffixes_true': "Mantieni",
        'filename_preview_label': "Anteprima del nome file:",
        'filename_preview_overwrite_hint': "Anteprima non disponibile – l'originale verrà sovrascritto.",
        'filename_separator': "Separatore tra le parole",
        'filename_separator_none': "Nessun separatore",
        'filename_separator_space': "Spazio ( )",
        'filename_separator_underscore': "Trattino basso (_)",
        'filename_settings_saved': "Impostazioni nome file salvate",
        'filename_settings_title': "Formattazione nome file e backup",
        'filename_timestamp_position': "Posizione del timestamp",
        'filename_timestamp_position_after': "Dopo il nome base",
        'filename_timestamp_position_before': "Tutto davanti",
        'filename_timestamp_position_end': "Alla fine",
        'filename_use_timestamp': "Usa timestamp",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Comportamento in caso di modifiche:</b><ul><li>Eliminare e inserire pagine</li><li>Inserire testo, firma, immagine e forme</li><li>OCR</li></ul></html>",
        'backup_section': "Backup per operazioni sulle pagine (Elimina, Sposta)",
        'behavior_info': "Nota: Con 'Sovrascrivi originale' timestamp e suffissi vengono ignorati – il file mantiene il suo nome.",
        'behavior_new_file': "Crea sempre un nuovo file (con timestamp e suffisso)",
        'behavior_overwrite': "Sovrascrivi originale (nessun nuovo file)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Tutte le pagine sono state ruotate.\n\nL'originale è rimasto invariato.\nNuovo file: {0}",
        'all_pages_rotated_voice': "Tutte le pagine ruotate, nuovo file creato.",
        'empty_pages_deleted_new_file': "{0} pagine vuote sono state eliminate.\n\nL'originale è rimasto invariato.\nNuovo file: {1}",
        'empty_pages_deleted_voice': "{0} pagine vuote eliminate, nuovo file creato.",
        'ocr_keep_original': "Mantieni originale (apri manualmente più tardi)",
        'ocr_new_file_question': "Il nuovo PDF ricercabile è stato salvato in:\n{0}\n\nVuoi aprirlo ora?",
        'ocr_open_new': "Apri nuovo file OCR",
        'ocr_original_kept': "Il file originale rimane aperto. Il file OCR è stato salvato.",
        'page_deleted_new_file': "La pagina {0} è stata eliminata.\n\nL'originale è rimasto invariato.\nNuovo file: {1}",
        'page_deleted_voice': "Pagina {0} eliminata, nuovo file creato.",
        'page_rotated_new_file': "La pagina {0} è stata ruotata.\n\nL'originale è rimasto invariato.\nNuovo file: {1}",
        'page_rotated_voice': "Pagina {0} ruotata, nuovo file creato.",
        'pages_deleted_new_file': "Sono state eliminate {0} pagine.\n\nIl file originale è rimasto invariato.\nNuovo file: {1}",
        'pages_deleted_new_file_voice': "{0} pagine eliminate, nuovo file creato.",
        'pages_inserted_new_file': "Sono state inserite {0} pagine.\n\nIl file originale è rimasto invariato.\nNuovo file: {1}",
        'pages_inserted_new_file_ask': "Sono state inserite {0} pagine.\n\nL'originale è rimasto invariato.\nNuovo file: {1}\n\nVuoi aprirlo ora?",
        'pages_inserted_voice_new': "{0} pagine inserite, nuovo file creato.",
        'pages_moved_new_file': "Sono state spostate {0} pagine.\n\nIl file originale è rimasto invariato.\nNuovo file: {1}",
        'pages_moved_new_file_voice': "{0} pagine spostate, nuovo file creato.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Non mostrare più",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Impostazione backup</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup ATTIVO</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Per tutte le modifiche che sovrascrivono l'originale</strong> (testo, firma, immagine, forma, OCR, ruotare, inserire, eliminare/spostare pagine) viene <strong>automaticamente creato un backup con timestamp</strong> prima di applicare la modifica.</p>
                <p style="margin: 5px 0 5px 20px;">• Il backup si trova accanto al file originale (es. <code>Documento_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Se hai inoltre attivato l'opzione <strong>„Sovrascrivi originale“</strong>, viene creato anche un backup.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup DISATTIVATO</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nessun backup viene creato</strong> – né durante la sovrascrittura né durante le operazioni sulle pagine.</p>
                <p style="margin: 5px 0 5px 20px;">• Il file originale può essere perso irrevocabilmente durante la sovrascrittura.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Raccomandato solo per utenti esperti!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Suggerimento:</strong> L'impostazione del backup è indipendente dall'opzione „Sovrascrivi originale“. Puoi combinarle entrambe.<br>
                Puoi nascondere permanentemente questo messaggio.
            </div>
        </div>
        """,
        'backup_info_title': "Comportamento del backup",
        'backup_info_voice': "Avviso sul comportamento del backup durante le operazioni sulle pagine. Backup attivo sovrascrive l'originale, backup disattivo crea un nuovo file.",
        'show_backup_info': "Informazioni sull'impostazione del backup",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Non mostrare più",
        'overwrite_enable_backup': "Attiva backup (consigliato)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Sovrascrivi originale</p>
            <p>Se attivi questa opzione, le modifiche (testo, firma, immagine, forma, OCR, ruotare, inserire) vengono <strong>salvate direttamente nell'originale</strong> – <strong>nessun nuovo file viene creato</strong>.</p>
            <p>• Il nome del file rimane invariato.<br>
            • Timestamp e suffissi vengono ignorati.<br>
            • <strong>Senza backup, l'originale può essere perso irrevocabilmente.</strong></p>
            <p style="color: #FFD700;">Raccomandazione: Attiva inoltre l'opzione di backup per ottenere copie di sicurezza automatiche.</p>
        </div>
        """,
        'overwrite_info_title': "Sovrascrivi originale",
        'overwrite_info_voice': "Attenzione: Sovrascrivi originale – nessun nuovo file. Backup consigliato.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} pagine sono state inserite.\n\nIl file originale è stato sovrascritto.\nÈ stato creato un backup.",
        'pages_inserted_overwrite_no_backup': "{0} pagine sono state inserite.\n\nIl file originale è stato sovrascritto.\nNON è stato creato alcun backup.",
        'texts_saved_overwrite_with_backup': "Le modifiche sono state salvate nell'originale.\n\nÈ stato creato un backup.",
        'texts_saved_overwrite_no_backup': "Le modifiche sono state salvate nell'originale.\n\nNON è stato creato alcun backup.",
        'texts_crosses_saved_new_file': "{0} {1} e {2} {3} sono stati inseriti.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",
        'texts_saved_new_file': "{0} {1} sono stati inseriti.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",
        'crosses_saved_new_file': "{0} {1} sono stati inseriti.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",
        'elements_saved_new_file': "{0} elementi sono stati inseriti.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",
        'signatures_saved_overwrite_with_backup': "La/e firma/e è/sono stata/e salvata/e nell'originale.\n\nÈ stato creato un backup.",
        'signatures_saved_overwrite_no_backup': "La/e firma/e è/sono stata/e salvata/e nell'originale.\n\nNON è stato creato alcun backup.",
        'images_saved_overwrite_with_backup': "L'/Le immagine/i è/sono stata/e salvata/e nell'originale.\n\nÈ stato creato un backup.",
        'images_saved_overwrite_no_backup': "L'/Le immagine/i è/sono stata/e salvata/e nell'originale.\n\nNON è stato creato alcun backup.",
        'forms_saved_overwrite_with_backup': "La/Le forma/e è/sono stata/e salvata/e nell'originale.\n\nÈ stato creato un backup.",
        'forms_saved_overwrite_no_backup': "La/Le forma/e è/sono stata/e salvata/e nell'originale.\n\nNON è stato creato alcun backup.",
        'signatures_saved_new_file': "{0} firme sono state inserite.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",
        'images_saved_new_file': "{0} immagini sono state inserite.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",
        'forms_saved_new_file': "{0} forme sono state inserite.\n\nIl file originale è rimasto invariato.\nÈ stato creato un nuovo file.\n\nCaricamento del nuovo PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Attenzione: Questo PDF contiene pagine ruotate. Il posizionamento potrebbe essere diverso.",
        'page_rotated_warning_title': "Pagina ruotata rilevata",
        'page_rotated_warning_message': "La pagina corrente {0} è ruotata di {1}°.\n\nL'inserimento di elementi su pagine ruotate non è supportato.\n\nVuoi ruotare la pagina in posizione verticale ora?",
        'page_rotated_warning_voice': "Attenzione: La pagina è ruotata. Ruotala prima.",
        'paste_on_rotated_page_simple_warning': "Inserimento sulla pagina {0} non possibile!\n\nQuesta pagina è ruotata di {1}°.\n\nRuota prima la pagina a 0° (Menu: Modifica → Allinea pagina).\n\nAttenzione:\nL'elemento copiato in precedenza andrà perso se non salvi prima di ruotare la pagina.",
        'paste_on_rotated_page_voice': "Inserimento annullato. La pagina è ruotata. Allinea prima la pagina.",
        'page_rotated_cancel': "Annulla",
        'page_rotated_rotate_until_upright': "Ruota la pagina ripetutamente (finché non è verticale)",
        'page_rotated_now_upright': "La pagina è ora verticale. Ora puoi inserire.",
        'page_rotated_still_not_upright': "Impossibile ruotare la pagina in posizione verticale. Correggi manualmente.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Aiuto: Correggere pagine ruotate",
        'help_rotated_pages_voice': "Si apre l'aiuto per correggere le pagine ruotate.",
        'btn_help': "Aiuto",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problema: Pagina ruotata – L'inserimento non funziona correttamente</p>

            <p>Se l'inserimento di testi, firme o forme su una pagina ruotata non funziona correttamente, puoi correggere la pagina con un editor PDF esterno.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Soluzione con strumento esterno (es. Anteprima macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Esporta pagina</strong><br>
                &nbsp;&nbsp;Clicca nel menu su <strong>File → Esporta come pagine</strong> o utilizza un altro metodo per salvare la pagina desiderata come PDF singolo.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Apri pagina in programma esterno</strong><br>
                &nbsp;&nbsp;Apri il PDF esportato in un editor PDF (es. <strong>Anteprima macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Ruota pagina</strong><br>
                &nbsp;&nbsp;Ruota la pagina in modo che sia verticale (in Anteprima: <strong>Strumenti → Ruota</strong> o <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Salva</strong><br>
                &nbsp;&nbsp;Salva la pagina corretta (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Reinserisci la pagina nel documento originale</strong><br>
                &nbsp;&nbsp;Torna a PDFDarkView e inserisci la pagina corretta nella posizione desiderata:<br>
                &nbsp;&nbsp;<strong>Modifica → Inserisci pagine</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativa: Ruota pagina nell'originale</p>
                <p style="margin: 5px 0 5px 20px;">• Usa la funzione di rotazione integrata (<strong>Modifica → Ruota pagina</strong>) per correggere la pagina passo dopo passo.<br>
                • Dopo ogni rotazione puoi verificare se l'inserimento ora funziona.<br>
                • Questa è spesso la soluzione più veloce – provala prima!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Suggerimento:</strong> Se incontri spesso pagine ruotate, puoi nascondere permanentemente l'avviso nella finestra di inserimento.<br>
                Il posizionamento potrebbe allora essere diverso – usa questa opzione solo se conosci le conseguenze.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Allinea pagine",
        'menu_rotate_normalize_tooltip': "Ruota pagina o reimposta a 0°",
        'normalize_current_page': "Porta la pagina corrente in posizione verticale (imposta a 0°)",
        'normalize_all_pages': "Porta tutte le pagine in posizione verticale (imposta a 0°)",
        'page_normalized': "La pagina {0} è stata portata in posizione verticale.",
        'all_pages_normalized': "Tutte le pagine sono state portate in posizione verticale.",
        'page_already_upright': "La pagina {0} è già verticale.",
        'all_pages_already_upright': "Tutte le pagine sono già verticali.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>Il PDF non contiene testo ricercabile.</p><p>Vuoi eseguire l'OCR per esportare in {0}?</p>",
        'export_ocr_voice': "Il PDF non contiene testo. È richiesto l'OCR per l'esportazione in {0}.",
        'export_no_ocr_possible': "Esportazione senza OCR non possibile. Esegui l'OCR tramite il menu.",
        'ocr_failed_export_not_possible': "OCR fallito. Impossibile eseguire l'esportazione.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "Il PDF verrà aperto in Anteprima. Avvia lì il processo di stampa.",
        'print_preview_manual': "Il PDF è stato aperto. Esegui il comando di stampa manualmente (es. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Unisci PDF",
        'merge_pdfs': "Unisci PDF",
        'merge_progress_title': "Unione PDF in corso...",
        'merge_pdfs_list': "PDF in ordine (Trascina e rilascia per ordinare)",
        'merge_add_pdf': "Aggiungi PDF",
        'merge_remove': "Rimuovi",
        'merge_move_up': "Su",
        'merge_move_down': "Giù",
        'merge_pdfs_info': "💡 Suggerimento: Puoi modificare l'ordine trascinando e rilasciando",
        'merge_no_pdfs': "Nessun PDF selezionato. Clicca su 'Aggiungi PDF'.",
        'merge_info': "{0} PDF selezionati (circa {1} pagine)",
        'merge_open_file': "Apri file",
        'merge_merge': "Unisci",
        'merge_error': "Errore durante l'unione",
        'merge_min_two_pdfs_error': "Seleziona almeno due file PDF da unire.",
        'merge_select_pdfs': "Seleziona PDF da unire",
        'merge_error_file': "Errore durante l'elaborazione",
        'merge_cancelled': "L'unione è stata annullata",
        'merge_preparing': "Preparazione...",
        'merge_processing': "Elaborazione PDF {0} di {1}",
        'merge_saving': "Salvataggio PDF unito...",
        'merge_complete': "Completato!",
        'merge_success_title': "Unione riuscita",
        'merge_success_voice': "{0} PDF sono stati uniti con successo.",
        'merge_success_message': "{0} PDF sono stati uniti con successo.\n\nIl nuovo documento ora ha {1} pagine.\n\nNuovo file:\n{2}\n\nPosizione di salvataggio:\n{3}\n{2}\n\nVuoi aprire questo PDF?",
        'replace_file_title': "Sostituire file?",
        'replace_file_message': "Un PDF è già aperto. Vuoi sostituirlo con il nuovo file?",
        'btn_yes': "Sì",
        'btn_no': "No",
        'filename_merge_suffix': "unito",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Apertura {0}...",
        'progress_merge_reading': "Lettura {0}...",
        'progress_merge_adding': "Aggiunta di {0} pagine...",
        'progress_merge_optimizing': "Ottimizzazione PDF...",
        'progress_merge_writing': "Scrittura PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "chiudere il PDF",
        'action_close_window': "chiudere la finestra",
        'action_open_new_pdf': "aprire un nuovo PDF",
        'action_quit_app': "uscire dall'applicazione",
        'changes_saved': "Le modifiche sono state salvate.",
        'file_close_title': "Chiudi file PDF",
        'save_before_action': "Salvare le modifiche prima di {0}? Sì o No?",
        'save_before_action_voice': "Salvare le modifiche prima di {0}? Sì o No?",
        'save_before_close_question': "Salvare le modifiche prima di chiudere? Sì o No?",

        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF ricercabile creato:\n\n{0}\n\n<b>riprova se necessario",
        "ocr_rotate_title": "Allinea pagine prima dell'OCR",
        "ocr_rotate_question": "Il PDF contiene pagine ruotate.\nVuoi allineare tutte le pagine a 0° prima dell'OCR?\nQuesto migliora notevolmente il riconoscimento del testo.",
        "ocr_rotate_yes": "Sì, allinea",
        "ocr_rotate_no": "No, avvia OCR direttamente",
        "ocr_rotate_voice": "Il PDF contiene pagine ruotate. Tutte le pagine devono essere allineate prima dell'OCR?",
        "ocr_not_performed_message": "Nessun testo presente. Eseguire OCR (menu \"Modifica\" → \"Esegui OCR\" o tasto Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Impostazioni OCR",
        "ocr_language_btn": "Seleziona lingua OCR",
        "ocr_language": "Lingua(e) OCR",
        "ocr_language_current": "Lingua attuale:",
        "ocr_param_info": "Informazioni sul parametro",

        "ocr_force_ocr_label": "Forza OCR",
        "ocr_deskew_label": "Correggi inclinazione",
        "ocr_clean_label": "Pulisci immagine",
        "ocr_oversample_label": "Risoluzione (DPI)",
        "ocr_pagesegmode_label": "Segmentazione pagina",
        "ocr_oem_label": "Modalità motore OCR",
        "ocr_optimize_label": "Compressione PDF",
        "ocr_jobs_label": "Processi paralleli",
        "ocr_verbose_label": "Dettaglio log",

        "ocr_force_ocr_tooltip": "Forza OCR su ogni pagina, anche se il testo esiste già",
        "ocr_deskew_tooltip": "Allinea automaticamente scansioni inclinate",
        "ocr_clean_tooltip": "Rimuove rumore e artefatti dall'immagine",
        "ocr_oversample_tooltip": "Ingrandisci immagine prima dell'OCR a questo DPI",
        "ocr_pagesegmode_tooltip": "Determina come la pagina viene suddivisa in aree di testo",
        "ocr_oem_tooltip": "Seleziona il motore OCR di Tesseract",
        "ocr_optimize_tooltip": "Livello di compressione del PDF di output",
        "ocr_jobs_tooltip": "Numero di processi OCR paralleli",
        "ocr_verbose_tooltip": "Livello di dettaglio dell'output del log",
        "ocr_settings_explain_btn": "Spiegazione",

        "ocr_force_ocr_explain": "Forza il riconoscimento del testo su <b>ogni</b> pagina, anche se contiene già testo.\n\nRaccomandazione: <b>Attivo</b> per PDF scansionati, <b>Disattivo</b> per PDF nativi con testo già esistente.",

        "ocr_deskew_explain": "Corregge scansioni leggermente inclinate (fino a circa 5°).\n\nRaccomandazione: <b>Attivo</b> per documenti scansionati, <b>Disattivo</b> se le pagine sono già perfettamente diritte.",

        "ocr_clean_explain": "Rimuove rumore, punti e piccoli artefatti dall'immagine.\n<b>IMPORTANTE:</b> Per testi arabi, tailandesi o vietnamiti con segni diacritici (punti sopra/sotto le lettere) questa opzione dovrebbe essere <b>disattivata</b>, altrimenti potrebbero andare persi caratteri importanti.",

        "ocr_oversample_explain": "Ingrandisce l'immagine <b>prima</b> del riconoscimento del testo al DPI specificato.<br><br>• <b>72-150 DPI:</b> Molto veloce, ma basso tasso di riconoscimento<br>• <b>200-300 DPI:</b> Intervallo ottimale (Predefinito: 300)<br>• <b>400+ DPI:</b> Riconoscimento appena migliore, ma file notevolmente più grandi<br><br>Raccomandazione: 300 DPI per scritture complesse (arabo, cinese, giapponese), 200 DPI per lingue occidentali.",

        "ocr_pagesegmode_explain": "Determina come Tesseract divide la pagina in aree di testo.\n\n• <b>3 - Automatico (Predefinito):</b> Buono per layout misti\n• <b>4 - Colonna singola:</b> Per testi a colonna singola\n• <b>5 - Blocco verticale:</b> Per scritture verticali (giapponese, cinese)\n• <b>6 - Blocco di testo uniforme:</b> Ottimale per testo fluente senza colonne\n• <b>11 - Immagine grezza:</b> Per scansioni scadenti / scrittura a mano\n\nRaccomandazione: <b>6</b> per documenti di testo semplici, <b>3</b> per layout complessi.",

        "ocr_oem_explain": "Seleziona il motore OCR di Tesseract.\n\n• <b>0 - Legacy:</b> Vecchio motore (veloce, ma meno preciso)\n• <b>1 - LSTM:</b> Motore neurale (più lento, ma più preciso)\n• <b>2 - Legacy + LSTM:</b> Combina entrambi i risultati\n• <b>3 - Predefinito (LSTM preferito):</b> Migliore scelta per la maggior parte dei casi\n\nRaccomandazione: <b>3</b> per la massima precisione di riconoscimento.",

        "ocr_optimize_explain": "Comprime il PDF di output.\n\n• <b>0:</b> Nessuna ottimizzazione (elaborazione più veloce)\n• <b>1:</b> Ottimizzazione leggera (buon compromesso)\n• <b>2:</b> Ottimizzazione moderata\n• <b>3:</b> Ottimizzazione forte (file più piccolo, ma più lento)\n\nRaccomandazione: <b>1</b> per uso quotidiano.",

        "ocr_jobs_explain": "Numero di processi paralleli per l'OCR.\n\n• <b>1:</b> Lento, ma consumo di memoria più basso\n• <b>4-8:</b> Ottimale per processori multi-core moderni\n• <b>12+:</b> Elaborazione appena più veloce con alto consumo di memoria\n\nRaccomandazione: Numero di core della CPU (es. <b>4</b> su sistemi a 4 core).",

        "ocr_verbose_explain": "Livello di dettaglio dell'output del log nella console.\n\n• <b>0:</b> Nessun output\n• <b>1:</b> Avanzamento e messaggi di stato\n• <b>2:</b> Output dettagliato\n• <b>3:</b> Output di debug completo (molto esteso)\n\nRaccomandazione: <b>1</b> per il normale funzionamento.",

        "ocr_reset_title": "Impostazioni ripristinate",
        "ocr_reset_message": "Tutte le impostazioni OCR sono state ripristinate ai valori predefiniti.",
        "info_tooltip": "Ulteriori informazioni su questo parametro",
        "ocr_reset_defaults": "Ripristina predefiniti",

        "ocr_psm_0": "Automatico (motore Legacy)",
        "ocr_psm_1": "Rilevamento automatico colonne",
        "ocr_psm_3": "Automatico (Predefinito)",
        "ocr_psm_4": "Colonna singola",
        "ocr_psm_5": "Blocco verticale",
        "ocr_psm_6": "Blocco di testo uniforme",
        "ocr_psm_7": "Riga di testo singola",
        "ocr_psm_8": "Parola singola",
        "ocr_psm_11": "Immagine grezza (nessuna analisi layout)",

        "ocr_oem_0": "Motore Legacy (veloce)",
        "ocr_oem_1": "Motore LSTM (neurale, preciso)",
        "ocr_oem_2": "Legacy + LSTM combinato",
        "ocr_oem_3": "Predefinito (LSTM preferito)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Lingua(e) OCR...",
        "ocr_language_title": "Seleziona lingua(e) OCR",
        "ocr_language_instruction": "Seleziona la/e lingua/e per il riconoscimento del testo (OCR).\nAttenzione: Più lingue vanno a scapito delle prestazioni e della precisione!\nSi ottengono i migliori risultati se si seleziona una sola lingua.",
        "ocr_language_predefined": "Combinazioni predefinite",
        "ocr_language_custom": "Personalizzato...",
        "ocr_language_selected": "Lingue OCR selezionate",
        "ocr_language_changed": "Lingua OCR cambiata in {0}",
        "ocr_language_auto_detect": "Le lingue disponibili vengono rilevate automaticamente.",
        "ocr_language_none_found": "Nessun dato linguistico Tesseract trovato! Installare i pacchetti lingua (es. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Selezione lingua personalizzata",
        "ocr_language_available": "Lingue disponibili (installate):",
        "ocr_language_select_hint": "Seleziona una o più lingue:",
        "ocr_language_confirm": "Applica",
        "ocr_language_reset": "Ripristina predefinito (deu+eng+vie)",
        "ocr_language_priorities": "Lingue consigliate (preinstallate):",

        "select_all_languages": "Seleziona tutto",
        "clear_all_languages": "Cancella selezione",
        "install_language_packs": "Installa pacchetti lingua mancanti...",
        "install_hint": "💡 Suggerimento: Non tutte le lingue sono installate sul tuo sistema. Con questo pulsante riceverai aiuto per l'installazione.",
        "ocr_language_install_title": "Installazione dei pacchetti lingua Tesseract",

        "ocr_missing_languages": "Pacchetti lingua OCR mancanti",
        "ocr_missing_languages_message": "Le seguenti lingue selezionate non sono installate sul tuo sistema:\n\n{0}\n\nInstallare i pacchetti lingua mancanti (vedere aiuto in 'Aiuto installazione').\n\nVuoi aprire l'aiuto installazione ora?",
        "ocr_missing_languages_voice": "Pacchetti lingua mancanti. Installare le lingue mancanti.",
        "ocr_install_help_now": "Apri aiuto",
        "ocr_continue_anyway": "Prova comunque",
        "ocr_language_error_title": "Errore lingua OCR",
        "ocr_language_error_message": "Errore durante il riconoscimento del testo: {0}\n\nControllare le impostazioni della lingua OCR (Impostazioni → Lingua OCR).",
        "ocr_install_help_button": "Aiuto installazione",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Installare i pacchetti lingua Tesseract</p>

        <p>Affinché l'OCR funzioni in una lingua specifica, i corrispondenti dati linguistici devono essere installati sul tuo sistema. Seguire le istruzioni per il tuo sistema operativo:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Aprire il <strong>Terminale</strong> (Finder → Programmi → Utility → Terminale).</li>
        <li>Installare tutte le lingue disponibili con:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Potrebbe richiedere alcuni minuti.)</li>
        <li>Oppure solo lingue singole (es. vietnamita):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Con le versioni correnti di Homebrew, potrebbe essere necessario scaricare manualmente <code>*.traineddata</code> (vedere sotto).</li>
        <li>Dopo l'installazione: Chiudere questa finestra di dialogo e riaprire la selezione della lingua OCR – le nuove lingue appariranno automaticamente.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Aprire un terminale (Ctrl+Alt+T).</li>
        <li>Installare la lingua desiderata, ad esempio per il vietnamita:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Codici lingua importanti: <code>deu</code> (tedesco), <code>eng</code> (inglese), <code>vie</code> (vietnamita), <code>spa</code> (spagnolo), <code>fra</code> (francese), <code>ita</code> (italiano), <code>nld</code> (olandese), <code>fin</code> (finlandese), <code>swe</code> (svedese), <code>nor</code> (norvegese).</li>
        <li>Mostrare tutti i pacchetti disponibili:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuale)</p>
        <ol>
        <li>Scaricare i file <code>*.traineddata</code> desiderati da:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (es. <code>vie.traineddata</code> per il vietnamita).</li>
        <li>Copiare i file nella cartella delle lingue di Tesseract, di solito:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Adattare secondo l'installazione individuale.)</li>
        <li>Riavviare l'applicazione (o riaprire la selezione della lingua OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativa per tutti i sistemi</p>
        <ul>
        <li>Installare <strong>OCRmyPDF</strong> e <strong>Tesseract</strong> con un gestore di pacchetti a tua scelta. La maggior parte delle installazioni contiene già alcune lingue standard (inglese, tedesco, francese).</li>
        <li>Le lingue mancanti possono essere installate in qualsiasi momento – la selezione della lingua OCR elenca solo le lingue effettivamente esistenti.</li>
        </ul>

        <hr>
        <p><b>✅ Dopo l'installazione:</b> Non è necessario riavviare l'applicazione – le nuove lingue aggiunte appariranno immediatamente nell'elenco.</p>
        <p><b>📖 Aiuto per i codici lingua:</b> Un elenco completo è disponibile nella <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">documentazione di Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Font Noto Sans",
        "info_noto_font_voice": "Guida all'installazione dei font Noto Sans",
        "btn_info_noto_font_install": "Info font",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Come installare i font gratuiti Noto di Google</h2>

        <p>I <strong>font Noto</strong> sono una famiglia di font open source di Google. Il loro obiettivo è non vedere <em>"nessun tofu"</em> (cioè nessuna scatola vuota □) e visualizzare correttamente ogni carattere dello standard Unicode. Sono il complemento ideale per applicazioni che devono visualizzare testi in molte lingue diverse.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installazione su macOS</h3>

        <p><strong>Metodo 1: Con Homebrew (per utenti avanzati)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metodo 2: Tramite "Font Book" (Consigliato)</strong></p>

        <ol>
        <li>Scaricare il pacchetto font ufficiale:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Estrarre il file ZIP</li>
        <li>Copiare i file in <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installazione su Windows (10 & 11)</h3>

        <p><strong>Metodo 1: Microsoft Store (Consigliato)</strong><br>
        Cercare "Google Noto Fonts" o "Noto Sans" e fare clic su <strong>Installa</strong>.</p>

        <p><strong>Metodo 2: Installazione manuale</strong></p>

        <ol>
        <li>Scaricare:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Estrarre ZIP</li>
        <li>Selezionare i file .ttf / .otf</li>
        <li>Fare clic con il tasto destro → <strong>Installa</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        o<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nome\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installazione su Linux</h3>

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

        <p>Verifica:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Gestisci segnalibri",
        "bookmark_add": "Aggiungi segnalibro",
        "bookmark_add_tooltip": "Salva la pagina corrente come segnalibro",
        "bookmark_remove": "Rimuovi segnalibro",
        "bookmark_remove_tooltip": "Elimina il segnalibro contrassegnato",
        "bookmark_remove_all": "Rimuovi tutti",
        "bookmark_remove_all_tooltip": "Elimina tutti i segnalibri di questo PDF",
        "bookmark_jump": "Vai al segnalibro",
        "bookmark_jump_tooltip": "Vai alla pagina selezionata",
        "bookmark_name": "Nome",
        "bookmark_page": "Pagina",
        "bookmark_no_bookmarks": "Nessun segnalibro presente.\nFare clic su 'Aggiungi' per salvare la pagina corrente come segnalibro.",
        "bookmark_added": "Segnalibro per la pagina {0} aggiunto: {1}",
        "bookmark_removed": "Segnalibro rimosso: {0}",
        "bookmark_all_removed": "Tutti i segnalibri sono stati rimossi.",
        "bookmark_name_default": "Pagina {0}",
        "bookmark_name_prompt": "Nome per il segnalibro:\n(il testo lungo verrà abbreviato a 50 caratteri)",
        "bookmark_name_prompt_title": "Nome segnalibro",
        "bookmark_confirm_remove_all": "Sei sicuro di voler rimuovere tutti i {0} segnalibri?",
        "menu_bookmarks": "Segnalibri",
        "bookmark_manage": "Gestisci segnalibri",
        "bookmark_next": "Segnalibro successivo",
        "bookmark_prev": "Segnalibro precedente",
        "bookmark_page_display": "Pagina {0}",
        "bookmark_exists": "Esiste già un segnalibro per questa pagina con questo nome.",
        "bookmark_select_first": "Seleziona prima un segnalibro.",
        "bookmark_confirm_remove": "Sei sicuro di voler rimuovere il segnalibro 'Pagina {0}: {1}'?",
        "bookmark_jumped_to": "Saltato al segnalibro '{0}' a pagina {1}.",
        "bookmark_jumped_to_voice": "Segnalibro {0}, pagina {1}",
        "btn_close": "Chiudi",

        "bookmark_list": "I tuoi segnalibri",
        "bookmark_rename": "Rinomina segnalibro",
        "bookmark_rename_tooltip": "Cambia il nome del segnalibro selezionato",
        "bookmark_rename_title": "Rinomina segnalibro",
        "bookmark_rename_prompt": "Nuovo nome per il segnalibro a pagina {0}:\n(max. 50 caratteri)",
        "bookmark_renamed": "Il segnalibro '{0}' è stato rinominato in '{1}'.",
        "bookmark_item_tooltip": "Pagina {0}: {1}\nDoppio clic per saltare",
        "bookmark_name_exists_question": "Esiste già un segnalibro con nome '{0}' in questa pagina.\nRinominare comunque?",

        "context_bookmarks": "Segnalibri",
        "context_bookmark_add_here": "Aggiungi segnalibro per questa pagina",
        "context_bookmarks_existing": "Segnalibri esistenti:",
        "context_bookmarks_jump": "Vai al segnalibro:",
        "context_bookmarks_none": "Nessun segnalibro presente",
        "context_bookmarks_clear_all": "Rimuovi tutti i {0} segnalibri",

        "bookmark_search_placeholder": "Cerca segnalibri... (nome o pagina)",
        "bookmark_search_results": "Trovati %d segnalibri per \"%s\"",
        "bookmark_no_search_results": "Nessun segnalibro trovato per \"%s\"",
        "bookmark_no_search_results_label": "Nessun risultato per \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Modifica metadati PDF",
        "metadata_title": "Titolo",
        "metadata_title_placeholder": "Titolo del documento",
        "metadata_title_tooltip": "Il titolo del documento (visualizzato nella barra del titolo)",
        "metadata_author": "Autore",
        "metadata_author_placeholder": "Nome dell'autore",
        "metadata_author_tooltip": "Il creatore del documento",
        "metadata_subject": "Oggetto",
        "metadata_subject_placeholder": "Oggetto del documento",
        "metadata_subject_tooltip": "Una breve descrizione del contenuto",
        "metadata_keywords": "Parole chiave",
        "metadata_keywords_placeholder": "Parole chiave separate da virgole",
        "metadata_keywords_tooltip": "Parole chiave per categorizzare il documento",
        "metadata_creator": "Creatore",
        "metadata_creator_placeholder": "Applicazione che ha creato il PDF",
        "metadata_creator_tooltip": "Il software con cui è stato creato il documento",
        "metadata_producer": "Produttore",
        "metadata_producer_placeholder": "Applicazione che ha convertito il PDF",
        "metadata_producer_tooltip": "Il software che ha convertito il PDF",
        "metadata_creation_date": "Data di creazione",
        "metadata_creation_date_tooltip": "La data di creazione del documento",
        "metadata_mod_date": "Data di modifica",
        "metadata_mod_date_tooltip": "La data dell'ultima modifica",
        "metadata_pdf_info": "📄 Informazioni PDF",
        "metadata_pages": "Numero di pagine",
        "metadata_file_size": "Dimensione file",
        "metadata_pdf_version": "Versione PDF",
        "metadata_encrypted": "Crittografato",
        "metadata_encrypted_yes": "Sì (protetto da password)",
        "metadata_encrypted_no": "No",
        "metadata_reload": "📂 Ricarica da PDF",
        "metadata_reset": "Annulla modifiche",
        "metadata_reloaded": "I metadati sono stati ricaricati dal PDF.",
        "metadata_reset_done": "Tutti i campi dei metadati sono stati ripristinati.",
        "metadata_no_file": "Nessun file PDF caricato.",
        "metadata_save_error": "Errore durante il salvataggio dei metadati",
        "metadata_saved": "I metadati sono stati salvati con successo.",
        "metadata_pdf_version_unknown": "PDF (sconosciuto)",
        "metadata_saved_message": "I metadati sono stati salvati con successo.",
        "metadata_saved_voice": "Metadati salvati.",

        "metadata_custom": "🔧 Metadati personalizzati",
        "metadata_custom_placeholder": "{\n  \"mio_campo\": \"mio_valore\",\n  \"altro_campo\": 123\n}",
        "metadata_custom_tooltip": "Formato JSON per metadati personalizzati (opzionale)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Modello \"{0}\" selezionato - Doppio clic per inserire",
        "text_use_template": "Utilizza blocco di testo",
        "text_type": "Tipo",
        "text_search_templates": "Cerca blocchi di testo...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informazioni esportazione / importazione",
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

        <h3>📦 Cosa viene esportato? (Panoramica)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Impostazioni generali dell'applicazione</span></li>
            <li class="detail">• Modalità scura/chiara</li>
            <li class="detail">• Inversione modalità scura per immagini</li>
            <li class="detail">• Valore soglia grigio</li>
            <li class="detail">• Lingua</li>
            <li class="detail">• Geometria finestra</li>
            <li class="detail">• Modalità zoom</li>
            <li class="detail">• Navigazione (Barra di navigazione visibile)</li>
            <li class="detail">• Uscita vocale (attivo/disattivo)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Impostazioni di backup</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Denominazione file (Timestamp, Separatore, Suffissi)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Impostazioni per inserimenti di</span></li>
            <li class="detail">• Firme</li>
            <li class="detail">• Testo &amp; blocchi di testo</li>
            <li class="detail">• Croci, immagini e forme</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Impostazioni OCR</span></li>
            <li class="detail">• Lingua</li>
            <li class="detail">• Forza OCR · Modalità pagina</li>
            <li class="detail">• Pre-elaborazione immagine: Correggi inclinazione, Pulisci, Sovracampionamento</li>
            <li class="detail">• Numero di lavori paralleli</li>
            <li class="detail">• Modalità inversione</li>
            <li class="detail">• Valore soglia grigio</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Segnalibri</span></li>
            <li class="detail">• Tutti i segnalibri per file PDF (Pagina, Nome, Ora di creazione)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Database password</span></li>
            <li class="detail">• Password PDF salvate (opzionalmente crittografate o testo semplice)</li>
            <li class="detail">• Hash password master (se impostata)</li>
            <li class="detail">• Dati di verifica</li>
        </ul>

        <h4>⚠️ Note importanti</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Durante l'importazione:</strong>
            <ul>
                <li><span class="warning">➜ TUTTE le impostazioni correnti verranno completamente sovrascritte</span></li>
                <li>• È obbligatorio riavviare l'applicazione</li>
                <li>• Firme, blocchi di testo e segnalibri esistenti verranno sostituiti</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Password master e modalità di esportazione:</strong>
            <ul>
                <li>• Quando la password master è attiva, puoi scegliere:</li>
                <li>  - <span style="color: #98FB98;"><strong>Decifrato</strong></span> (le password sono in testo semplice nello ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Crittografato</strong></span> (leggibile solo con la password master sul sistema di destinazione)</li>
                <li>• L'hash della password master viene <strong>sempre</strong> memorizzato crittografato</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Avviso di sicurezza:</strong>
            <ul>
                <li>• Il file ZIP esportato contiene dati sensibili (<strong>password, segnalibri, firme</strong>)</li>
                <li>• Conservarlo in un luogo sicuro (es. chiavetta USB crittografata, gestore di password)</li>
                <li>• Se il file viene perso, le password PDF salvate sono irrimediabilmente perse</li>
            </ul>
        </div>

        <h4>📁 Formato di esportazione</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Le impostazioni vengono salvate in un unico file ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Questo ZIP contiene il file <code>settings.json</code> completo (dalla tua configurazione) nonché eventuali file immagine di firma incorporati e password crittografate.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Firme - Guida",
        'signature_guide_html': """
        📝 <strong>Firme - Guida rapida</strong><br>
        <ul>
        <li>Imposta password master</li>
        <li>Configura le firme nel menu <em>Impostazioni</em> (dimensioni, timestamp, …)</li>
        <li>Inserisci con <strong>CLIC DESTRO</strong> nella posizione desiderata (password master richiesta una volta per sessione)</li>
        <li>Sposta la firma con il mouse o i tasti freccia</li>
        <li>Inserisci più firme consecutive</li>
        <li>Personalizza ogni firma individualmente</li>
        <li>Scarta singola firma</li>
        <li>Salva / scarta tutte le firme contemporaneamente</li>
        <li>In alternativa, è possibile utilizzare anche la barra dei menu.</li>
        </ul>
        """,
        'signature_guide_voice': "Guida rapida per le firme. Imposta password master. Configura le firme nelle impostazioni. Inserisci con clic destro.",

        'image_guide_title': "Inserire immagini - Guida",
        'image_guide_html': """
        📷 <strong>Inserire immagini in PDF - Guida rapida</strong><br>
        <ol>
        <li>Clic destro sulla posizione desiderata</li>
        <li><em>„Inserisci immagine“</em> → Seleziona immagine</li>
        <li>Posiziona l'immagine: Trascina con il mouse</li>
        <li>Regola le dimensioni: Trascina dagli angoli/bordi</li>
        <li>Mantieni le proporzioni: Tasto <strong>[A]</strong></li>
        <li>Ulteriori regolazioni: Clic destro sull'immagine</li>
        </ol>
        <p><strong>Suggerimento:</strong> Nel menu contestuale è possibile regolare le impostazioni.</p>
        """,
        'image_guide_voice': "Guida rapida per le immagini. Clic destro, inserisci immagine, seleziona. Posiziona con il mouse, regola le dimensioni dagli angoli. Proporzioni con tasto A.",

        'form_guide_title': "Inserire forme - Guida",
        'form_guide_html': """
        📐 <strong>Inserire forme in PDF - Guida rapida</strong><br>
        <ol>
        <li>Seleziona il tipo di forma (rettangolo, ellisse, linea, freccia)</li>
        <li>Clicca sulla posizione:
            <ul>
            <li>Per rettangolo/ellisse: Un clic posiziona la forma</li>
            <li>Per linea/freccia: Due clic per punto iniziale e finale</li>
            </ul>
        </li>
        <li>Posiziona la forma: Trascina con il mouse</li>
        <li>Regola le dimensioni: Trascina dagli angoli/bordi</li>
        <li>Salva la forma: <strong>Invio</strong></li>
        <li>Scarta la forma: <strong>ESC</strong></li>
        <li>Ulteriori regolazioni: Clic destro sulla forma</li>
        </ol>
        <p><strong>Suggerimento:</strong> Nel menu contestuale è possibile regolare le impostazioni.</p>
        """,
        'form_guide_voice': "Guida rapida per le forme. Seleziona il tipo di forma. Per rettangolo o ellisse clicca una volta, per linea o freccia due volte. Posiziona con il mouse, regola le dimensioni dagli angoli. Salva con Invio, scarta con Esc.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "precedente",
        "btn_next_result": "successivo",
        "ocr_text_window": "Finestra di testo OCR",
        "bookmark_existing": "Segnalibri esistenti",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Confronto OCR Mac - Windows",
        'ocr_method_mac_win_title': "Differenze OCR tra Mac e Windows",
        'ocr_method_mac_win_voice': "Mac è migliore",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Differenze tra macOS e Windows</strong></p>

        <p><strong>macOS (consigliato)</strong></p>
        <p>Strumento:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Risultato:</p>
        <ul>
        <li>Un PDF ricercabile con testo incorporato che preserva ampiamente il layout originale.</li>
        </ul>
        <p>Vantaggi:</p>
        <ul>
        <li>Qualità eccellente del riconoscimento del testo (anche su pagine storte).</li>
        <li>Conservazione di grafica vettoriale e caratteri.</li>
        <li>Barra di avanzamento GUI tramite valutazione del sottoprocesso.</li>
        <li>Controllo completo su tutti i parametri OCR (Deskew, Clean, Oversample, ottimizzazione).</li>
        <li>La ricerca del testo è direttamente disponibile nella finestra principale (visualizzazione PDF).</li>
        </ul>
        <p>Svantaggi:</p>
        <ul>
        <li>Richiede strumenti di sistema aggiuntivi (ocrmypdf, Ghostscript, unpaper, pngquant – inclusi nel bundle dell'app).</li>
        <li>Gestione degli errori più complessa (deadlock, timeout).</li>
        </ul>

        <p><strong>Windows (alternativa stabile)</strong></p>
        <p>Strumento:</p>
        <ul>
        <li>pytesseract (collegamento diretto a Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Risultato:</p>
        <ul>
        <li>Un PDF ricercabile che visivamente corrisponde a un PDF immagine, ma è ricercabile attraverso il testo trasparente.</li>
        </ul>
        <p>Vantaggi:</p>
        <ul>
        <li>Non me ne vengono in mente al momento.</li>
        </ul>
        <p>Svantaggi:</p>
        <ul>
        <li>Il PDF è essenzialmente un'immagine con testo invisibile; il layout può discostarsi leggermente per documenti complessi (colonne, tabelle).</li>
        <li>Nessuna correzione automatica dell'inclinazione (--deskew) o pulizia dell'immagine (--clean).</li>
        <li>La barra di avanzamento GUI viene aggiornata solo in modo approssimativo in base al numero di pagine elaborate.</li>
        <li>La velocità OCR è leggermente più lenta (poiché ogni pagina viene elaborata singolarmente).</li>
        <li>La ricerca del testo viene reindirizzata alla finestra di testo OCR.</li>
        </ul>

        <p><strong>Punti in comune</strong></p>
        <ul>
        <li>Entrambi i metodi creano un PDF ricercabile nella stessa directory del file sorgente.</li>
        <li>Le impostazioni OCR (lingua, DPI, modalità di segmentazione della pagina, modalità del motore OCR) possono essere configurate tramite OCRSettingsDialog e sono valide in entrambe le implementazioni.</li>
        </ul>

        <p><strong>Raccomandazione:</strong></p>
        <ul>
        <li>macOS: Il binario ocrmypdf fornisce i migliori risultati – Acquista un Mac e usa la versione (PDFDarkView per Mac con chip Apple Silicon o Intel). I risultati OCR sono migliori che su Windows!</li>
        <li>Windows: Utilizza la soluzione pytesseract. È stabile e fornisce una qualità completamente sufficiente per la maggior parte dei documenti.</li>
        </ul>

        <p><strong>Nota importante:</strong></p>
        <ul>
        <li>Entrambe le versioni sono completamente integrate nell'interfaccia utente – l'utente non nota alcuna differenza.</li>
        <li>Il programma decide automaticamente quale motore OCR utilizzare in base al sistema operativo.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Crea firma (da scansione)",
        "signature_create_title": "Seleziona firma scansionata (PDF/immagine)",
        "image_pdf_filter": "Immagini e PDF",
        "signature_pdf_empty": "Il PDF non contiene pagine.",
        "signature_created_success": "Firma creata con successo: {0}",
        "signature_create_error": "Errore durante la creazione della firma:\n{0}",
        "rembg_missing": "rembg non è installato.\nSi prega di installare: pip install rembg\nErrore: {0}",
        "signature_name_title": "Nome file per la firma",
        "signature_name_message": "Inserisci un nome file per la nuova firma (verrà salvata come PNG con sfondo trasparente):",
        "signature_name_label": "Nome file:",
        "signature_name_voice": "Inserisci il nome file per la firma",
        "signature_processing": "Elaborazione in corso...",
        "signature_creation_title": "Creazione firma in corso",
        "signature_overwrite_warning": "Il file '{0}' esiste già. Sovrascrivere?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Prepara PDF per la firma",
        "signature_prepare_instruction":"Seleziona un PDF che contiene una firma scansionata su una singola pagina.\n\nPer un riconoscimento ottimale, assicurarsi che:\n• La firma sia scritta con inchiostro nero (penna a sfera o pennarello fine) su carta bianca.\n• La firma si trovi nel terzo superiore di una pagina A4 altrimenti vuota.\n• Il PDF sia stato scansionato con almeno 300 dpi.\n• La firma sia chiara e non troppo sottile.\n• Non siano presenti motivi di sfondo o linee fastidiose.",
        "signature_prepare_voice":"Seleziona un PDF con una firma scansionata. Presta attenzione alla buona qualità e al contrasto.",
        "sig_thickness_label":"Spessore linea:",
        "sig_thickness_normal":"Normale (sottile)",
        "sig_thickness_bold":"Grassetto (consigliato)",
        "sig_thickness_very_bold":"Molto grassetto",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Aggiungere lingue GUI e OCR - Guida",
        'language_guide_title': "Aggiungere lingue GUI e OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Scarica il file di traduzione desiderato <code>translations_xy.py</code> da<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        e posizionalo nella seguente directory:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Apri il tuo browser web.</li>
        <li>Vai a: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Cerca sul bordo destro dello schermo "Releases" e seleziona quello contrassegnato con <strong>"latest"</strong>.</li>
        <li>Nella successiva pagina di rilascio, scarica il file <code>Source Code.zip</code> in fondo.</li>
        <li>Decomprimi il file ZIP.</li>
        <li>Cerca nella cartella decompressa tutti i file lingua di cui hai bisogno e copiali nella directory:<br/>
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
        "menu_watermark":"Inserisci filigrana",
        "fullpage_text_watermark_title":"Testo come filigrana",
        "fullpage_image_watermark_title":"Immagine come filigrana",
        "filename_with_watermark":"_con_filigrana",
        "watermark_text":"Testo:",
        "watermark_text_placeholder":"Il tuo testo della filigrana...",
        "watermark_font_family":"Carattere:",
        "watermark_font_size":"Dimensione carattere:",
        "watermark_format":"Formattazione:",
        "watermark_bold":"Grassetto",
        "watermark_italic":"Corsivo",
        "watermark_color":"Colore:",
        "watermark_choose_color":"Scegli colore...",
        "watermark_opacity":"Opacità / Trasparenza:",
        "watermark_direction":"Direzione di lettura:",
        "watermark_direction_l_r":"Sinistra → Destra",
        "watermark_direction_bl_tr":"In basso a sinistra → In alto a destra",
        "watermark_direction_tl_br":"In alto a sinistra → In basso",
        "watermark_direction_b_t":"In basso → In alto",
        "watermark_direction_t_b":"In alto → In basso",
        "watermark_preview":"Anteprima:",
        "watermark_preview_sample":"Testo di esempio",
        "watermark_empty_text":"Inserisci un testo.",
        "watermark_applied":"La filigrana è stata applicata a tutte le pagine.",
        "watermark_saved":"Filigrana salvata.",
        "image_scale":"Dimensione:",
        "image_preview":"Anteprima immagine:",
        "no_image_selected":"Nessuna immagine selezionata",
        "browse":"Sfoglia...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Oscuramenti",
        "redact_add_black": "Oscuramento (nero)",
        "redact_add_white": "Oscuramento (bianco / cancella)",
        "redact_added_black": "Oscuramento nero aggiunto",
        "redact_added_white": "Oscuramento bianco aggiunto",
        "redact_apply_all": "Applica tutti gli oscuramenti e salva",
        "redact_discard_all": "Annulla tutti gli oscuramenti",
        "redact_discard": "Annulla questo oscuramento",
        "no_redactions": "Nessun oscuramento",
        "redact_confirm_title": "Applica oscuramenti in modo permanente",
        "redact_confirm_message": "Attenzione: Le aree contrassegnate verranno eliminate definitivamente (nero o bianco).\nVerrà creato un backup (se abilitato).\n\nContinuare?",
        "redact_apply": "Sì, oscura ora",
        "redact_saved": "{0} oscuramento(i) applicato/i e salvato/i con successo.",
        "redact_saved_voice": "{0} oscuramento(i) applicato/i",
        "redact_error": "Errore durante l'oscuramento",
        "filename_redacted":"_oscuramento",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Inserisci numeri di pagina',
        'page_numbers_format': 'Formato numero:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabo)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romano minuscolo)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romano maiuscolo)',
        'page_numbers_format_letter': 'A, B, C ... (lettere)',
        'page_numbers_format_custom': 'Personalizzato',
        'page_numbers_custom_pattern': 'Modello:',
        'page_numbers_custom_placeholder': 'es. "Pagina {nummer}" o "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Usa {nummer} per il numero di pagina corrente e {total} per il totale',
        'page_numbers_position': 'Posizione:',
        'page_numbers_pos_tl': 'In alto a sinistra',
        'page_numbers_pos_tc': 'In alto al centro',
        'page_numbers_pos_tr': 'In alto a destra',
        'page_numbers_pos_ml': 'A sinistra al centro',
        'page_numbers_pos_mc': 'Centrato',
        'page_numbers_pos_mr': 'A destra al centro',
        'page_numbers_pos_bl': 'In basso a sinistra',
        'page_numbers_pos_bc': 'In basso al centro',
        'page_numbers_pos_br': 'In basso a destra',
        'page_numbers_margins': 'Margini:',
        'page_numbers_margin_x': 'Distanza orizzontale:',
        'page_numbers_margin_y': 'Distanza verticale:',
        'page_numbers_range': 'Intervallo di pagine:',
        'page_numbers_all_pages': 'Tutte le pagine',
        'page_numbers_custom_range': 'Intervallo personalizzato',
        'page_numbers_from': 'Da:',
        'page_numbers_to': 'A:',
        'page_numbers_progress': 'Inserimento numeri di pagina...',
        'page_numbers_start': 'Avvio inserimento numeri di pagina...',
        'page_numbers_cancel': 'Inserimento numeri di pagina annullato',
        'page_numbers_success': 'I numeri di pagina sono stati aggiunti con successo.\n\nVuoi aprire il nuovo PDF?\n\n{0}',
        'page_numbers_complete': 'Numeri di pagina aggiunti',
        'page_numbers_error_format': 'Errore durante'
        'inserimento dei numeri di pagina: {0}',
        'page_numbers_content_type': 'Tipo di contenuto:',
        'page_numbers_tab_simple': 'Numero semplice',
        'page_numbers_tab_range': 'Pagina X di Y',
        'page_numbers_tab_date': 'Data',
        'page_numbers_tab_custom': 'Testo libero',
        'page_numbers_range_format': 'Formato:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Pagina {aktuell} di {gesamt}',
        'page_numbers_range_custom': 'Personalizzato',
        'page_numbers_range_placeholder': 'es. "Pagina {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formato data:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 gennaio 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Personalizzato',
        'page_numbers_date_placeholder': 'es. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posizione:',
        'page_numbers_date_before': 'Data prima del numero di pagina',
        'page_numbers_date_after': 'Data dopo il numero di pagina',
        'page_numbers_date_only': 'Solo data (senza numero di pagina)',
        'page_numbers_custom_text': 'Testo personalizzato:',
        'page_numbers_custom_placeholder_text': 'Usa {seite} per il numero di pagina e {gesamt} per il totale\nes. "Riservato - Pagina {seite}" o "{seite} di {gesamt}"',
        "filename_with_page_number":"_con_numero_pagina",
        "filename_with_page_declaration":"_con_dichiarazione_pagina",
        "filename_with_pagenumber":"_con_numero_pagina",
        "filename_with_date":"_con_data",
        "filename_with_my_page_declaration":"_con_dichiarazione_personalizzata",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Modifiche non salvate",
        "unsaved_changes_message_darkmode": "Ci sono inserimenti non salvati.\nVuoi salvarli prima di cambiare?",
        "save_and_switch": "Salva e cambia",
        "discard_and_switch": "Cambia ora",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Esporta pagine come immagini',
        'export_images_menu': 'Esporta come immagini (PNG/JPEG)',
        'export_images_format': 'Formato immagine:',
        'export_images_dpi': 'Risoluzione (DPI):',
        'export_images_quality': 'Qualità JPEG:',
        'export_images_range': 'Intervallo di pagine:',
        'export_images_all_pages': 'Tutte le pagine',
        'export_images_custom_range': 'Intervallo personalizzato',
        'export_images_from': 'Da:',
        'export_images_to': 'A:',
        'export_images_options': 'Opzioni:',
        'export_images_single_files': 'Ogni pagina come file separato',
        'export_images_subfolder': 'Esporta in sottocartella',
        'export_images_subfolder_info': 'Nella sottocartella "nomePDF_immagini"',
        'export_images_same_folder': 'Nella stessa cartella del PDF',
        'export_images_apply_darkmode': 'Applica impostazioni PDFDarkView (Modalità scura)',
        'export_images_target_folder': 'Cartella di destinazione:',
        'export_images_browse': 'Sfoglia...',
        'export_images_preview': 'Anteprima:',
        'export_images_preview_info': 'Seleziona le impostazioni per l\'esportazione',
        'export_images_preview_info_detail': '{0} pagine come {1}\nRisoluzione: {2} DPI\nNome file: {3}\n{4}',
        'export_images_select_folder': 'Seleziona la cartella di destinazione',
        'export_images_start': 'Avvio esportazione immagini...',
        'export_images_progress': 'Esportazione immagini...',
        'export_images_saving': 'Salvataggio pagina {0} di {1}...',
        'export_images_success': 'Esportazione riuscita!\n\n{0} immagini sono state salvate in:\n{1}',
        'export_images_complete': 'Esportazione immagini completata',
        'export_images_open_folder': '📁 Apri cartella',
        'export_images_cancel': 'Esportazione immagini annullata',
        'export_images_error_format': 'Errore durante l\'esportazione delle immagini: {0}',
        'export_images_pdf2image_missing': 'La libreria "pdf2image" non è installata.\n\nInstallala con:\npip install pdf2image\n\nPer Windows è necessario anche Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Conversione PDF/A per l\'archiviazione a lungo termine',
        'pdfa_menu': 'Conversione PDF/A (idoneo all\'archiviazione)',
        'pdfa_info': 'Converte il PDF in formato PDF/A.\n\nIl PDF/A è progettato specificamente per l\'archiviazione a lungo termine e garantisce che il documento venga visualizzato correttamente in futuro.',
        'pdfa_standard': 'Standard PDF/A:',
        'pdfa_standard_select': 'Versione:',
        'pdfa_1': 'PDF/A-1 (semplice, ampiamente compatibile)',
        'pdfa_2': 'PDF/A-2 (moderno, migliore compressione)',
        'pdfa_3': 'PDF/A-3 (versione più recente, consente allegati)',
        'pdfa_standards_explanation': '📖 Spiegazione degli standard:\n\n'
            '• PDF/A-1: Base, compatibile con sistemi più vecchi (circa 2005)\n'
            '• PDF/A-2: Più moderno, migliore compressione, supporto della trasparenza (circa 2011)\n'
            '• PDF/A-3: Versione più recente, consente l\'incorporamento di allegati (circa 2013)\n\n'
            'Raccomandazione: PDF/A-2 è un buon compromesso tra compatibilità e funzionalità moderne.',
        'pdfa_options': 'Opzioni:',
        'pdfa_compress_enable': 'Comprimi PDF (file più piccolo)',
        'pdfa_metadata_preserve': 'Conserva metadati (titolo, autore, ecc.)',
        'pdfa_target_folder': 'Cartella di destinazione:',
        'pdfa_browse': 'Sfoglia...',
        'pdfa_select_folder': 'Seleziona la cartella di destinazione',
        'pdfa_ocr_info_unknown': '🔍 Impossibile verificare il contenuto del testo.',
        'pdfa_ocr_info_not_needed': '✅ Testo disponibile - OCR non richiesto.\nPDF/A può essere creato direttamente.',
        'pdfa_ocr_info_recommended': '⚠️ Testo sufficiente non trovato.\n\nPer PDF ricercabili, si consiglia di eseguire prima l\'OCR.\nNota: PDF/A funziona anche senza OCR - ma il testo non sarà ricercabile.',
        'pdfa_ocr_info_error': '❌ Errore durante la verifica: {0}',
        'pdfa_start': 'Avvio conversione PDF/A...',
        'pdfa_progress': 'Conversione PDF/A in corso...',
        'pdfa_success': 'Conversione PDF/A riuscita!\n\nSalvato come:\n{0}\n\nVuoi aprire il nuovo PDF?',
        'pdfa_complete': 'Conversione PDF/A completata',
        'pdfa_cancel': 'Conversione PDF/A annullata',
        'pdfa_error_format': 'Errore durante la conversione PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'La libreria "ocrmypdf" non è installata.\n\nInstallala con:\npip install ocrmypdf',
        'btn_convert': 'Converti',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Ottimizza PDF (riduci dimensione file)',
        'optimize_menu': 'Ottimizza PDF (dimensione file)',
        'optimize_info': 'Riduce la dimensione del file PDF attraverso vari metodi di ottimizzazione.\n\nPiù alto è il livello di compressione, più piccolo diventa il file - con possibile perdita di qualità nelle immagini.',
        'optimize_level': 'Livello di compressione:',
        'optimize_level_low': 'Basso (veloce, piccolo risparmio)',
        'optimize_level_medium': 'Medio (buon compromesso)',
        'optimize_level_high': 'Alto (grande risparmio)',
        'optimize_level_maximum': 'Massimo (risparmio massimo, lento)',
        'optimize_level_explanation': 'Raccomandazione: "Medio" è un buon compromesso tra velocità e dimensione del file.',
        'optimize_options': 'Opzioni:',
        'optimize_compress_images': 'Comprimi immagini (riduci qualità JPEG)',
        'optimize_clean_objects': 'Rimuovi oggetti inutilizzati',
        'optimize_preserve_metadata': 'Conserva metadati (titolo, autore, ecc.)',
        'optimize_image_quality': 'Qualità immagine:',
        'optimize_range': 'Intervallo di pagine:',
        'optimize_all_pages': 'Tutte le pagine',
        'optimize_custom_range': 'Intervallo personalizzato',
        'optimize_from': 'Da:',
        'optimize_to': 'A:',
        'optimize_target_folder': 'Cartella di destinazione:',
        'optimize_browse': 'Sfoglia...',
        'optimize_select_folder': 'Seleziona la cartella di destinazione',
        'optimize_info_box': 'Informazioni',
        'optimize_info_text': 'L\'ottimizzazione può richiedere diversi minuti per PDF di grandi dimensioni.\n\nLe immagini vengono salvate con qualità ridotta, il che può ridurre significativamente la dimensione del file.',
        'optimize_start': 'Avvio ottimizzazione PDF...',
        'optimize_progress': 'Ottimizzazione PDF...',
        'optimize_cancel': 'Ottimizzazione PDF annullata',
        'optimize_complete': 'Ottimizzazione PDF completata',
        'optimize_error_format': 'Errore durante l\'ottimizzazione PDF:\n\n{0}',
        'optimize_success_message': 'Ottimizzazione PDF riuscita!\n\nSalvato come:\n{0}\n\nPrima: {1}\nDopo: {2}\nRisparmio: {3:.1f}%\n\n{4}\n\nVuoi aprire il PDF ottimizzato?',
        'optimize_success_message_no_size': 'Ottimizzazione PDF riuscita!\n\nSalvato come:\n{0}\n\nInformazioni sulla dimensione non disponibili.\n\nVuoi aprire il PDF ottimizzato?',
        'optimize_result_positive': 'Il file è stato ridotto del {0:.1f}%.',
        'optimize_result_zero': 'Nessuna modifica della dimensione del file.',
        'optimize_result_negative': 'Il file è aumentato del {0:.1f}%.\nL\'ottimizzazione è stata saltata, il file originale è stato conservato.',
        'btn_optimize': 'Avvia ottimizzazione',
        'filename_optimize_low_suffix': '_ottimizzato_basso',
        'filename_optimize_medium_suffix': '_ottimizzato',
        'filename_optimize_high_suffix': '_ottimizzato_alto',
        'filename_optimize_maximum_suffix': '_ottimizzato_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Ritaglia PDF',
        'crop_menu': 'Ritaglia PDF (Crop)',
        'crop_range': 'Applica a:',
        'crop_all_pages': 'Tutte le pagine',
        'crop_current_page': 'Solo pagina corrente',
        'crop_values': 'Valori di ritaglio (in punti):',
        'crop_left': 'Sinistra:',
        'crop_right': 'Destra:',
        'crop_top': 'Superiore:',
        'crop_bottom': 'Inferiore:',
        'crop_presets': 'Preimpostazioni:',
        'crop_preset_white': 'Rileva margini bianchi',
        'crop_reset': 'Reimposta',
        'crop_mouse_hint': '🖱️ Trascina un rettangolo per selezionare approssimativamente l\'area.\nSuccessivamente puoi regolare i valori con precisione nei SpinBox.\nLa regolazione manuale con il mouse non è possibile.',
        'crop_apply': 'Ritaglia',
        'crop_scope_all': 'Tutte le pagine',
        'crop_scope_current': 'Pagina corrente',
        'crop_new_size': 'Nuova dimensione: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nessun PDF caricato',
        'crop_preview_error': 'Errore durante il caricamento dell\'anteprima',
        'crop_start': 'Avvio ritaglio...',
        'crop_progress': 'Ritaglio PDF...',
        'crop_success': 'PDF ritagliato con successo!\n\nSalvato come:\n{0}\n\nVuoi aprire il PDF ritagliato?',
        'crop_complete': 'Ritaglio completato',
        'crop_cancel': 'Ritaglio annullato',
        'crop_error_format': 'Errore durante il ritaglio:\n\n{0}',
        'filename_crop_suffix': '_ritagliato',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Appiattisci PDF (Flatten)',
        'flatten_menu': 'Appiattisci PDF (Flatten)',
        'flatten_info': 'Appiattire un PDF "brucia" tutti gli elementi modificabili nel contenuto della pagina.\n\nSuccessivamente, i campi del modulo, le annotazioni, i testi, le croci, le firme, le immagini e le forme non sono più modificabili singolarmente.',
        'flatten_explanation_title': '📖 A cosa serve?',
        'flatten_explanation_text': 'L\'appiattimento è necessario nelle seguenti situazioni:\n\n'
            '• 📄 Si desidera preparare il documento per la stampa\n'
            '• 🔒 Si desidera impedire a qualcuno di modificare i campi del modulo\n'
            '• 📎 Si desidera "incorporare" definitivamente annotazioni e commenti nel documento\n'
            '• 🖼️ Si desidera ancorare definitivamente testi, croci, firme, immagini e forme nel documento\n'
            '• 📦 Si desidera preparare il file per l\'archiviazione\n\n'
            'L\'appiattimento rende il PDF più piccolo e impedisce lo spostamento o l\'eliminazione accidentale degli elementi.',
        'flatten_what_title': 'Cosa viene appiattito?',
        'flatten_what_list': '• ✅ Campi del modulo (campi di testo, caselle di controllo, pulsanti)\n'
            '• ✅ Annotazioni (commenti, evidenziazioni, note)\n'
            '• ✅ Sovrapposizioni (testi, croci, firme, immagini, forme)',
        'flatten_options': 'Opzioni:',
        'flatten_forms': 'Appiattisci campi del modulo',
        'flatten_annotations': 'Appiattisci annotazioni',
        'flatten_overlays': 'Appiattisci sovrapposizioni (testi, croci, firme, immagini, forme)',
        'flatten_target_folder': 'Cartella di destinazione:',
        'flatten_browse': 'Sfoglia...',
        'flatten_select_folder': 'Seleziona la cartella di destinazione',
        'flatten_warning': '⚠️ Importante: L\'appiattimento è un processo irreversibile!\n\nDopo l\'appiattimento, gli elementi modificabili non possono più essere modificati o eliminati singolarmente.\nCreare un backup preventivo se necessario.',
        'flatten_apply': 'Appiattisci',
        'flatten_start': 'Avvio appiattimento...',
        'flatten_progress': 'Appiattimento PDF...',
        'flatten_success': 'PDF appiattito con successo!\n\nSalvato come:\n{0}\n\nVuoi aprire il PDF appiattito?',
        'flatten_complete': 'Appiattimento completato',
        'flatten_cancel': 'Appiattimento annullato',
        'flatten_error_format': 'Errore durante l\'appiattimento:\n\n{0}',
        'filename_flatten_suffix': '_appiattito',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Sovrapposizione PDF (Overlay)',
        'overlay_menu': 'Sovrapposizione PDF (Overlay)',
        'overlay_info': 'Posiziona un PDF (sovrapposizione) sopra un altro PDF.\n\nIl PDF di sovrapposizione viene posizionato sul PDF di base. Questo è utile per filigrane, loghi, intestazioni o timbri.',
        'overlay_explanation_title': '📖 A cosa serve?',
        'overlay_explanation_text': 'La sovrapposizione è necessaria nelle seguenti situazioni:\n\n'
            '• 🏢 Posizionare un logo aziendale come filigrana su ogni pagina\n'
            '• 📄 Posizionare un\'intestazione su un PDF vuoto\n'
            '• 🖊️ Posizionare una sovrapposizione di timbro su un documento\n'
            '• 🔖 Posizionare una filigrana su tutte le pagine\n'
            '• 📑 Posizionare una sovrapposizione di modulo su un modello',
        'overlay_type': 'Tipo di sovrapposizione:',
        'overlay_type_fullpage': 'Pagina intera (coprente)',
        'overlay_type_transparent': 'Pagina intera (trasparente - consigliato)',
        'overlay_type_stamp': 'Timbro (posizionabile)',
        'overlay_type_info_fullpage': '📄 Il PDF di sovrapposizione viene posizionato esattamente su tutta la pagina.\nLo sfondo bianco può essere rimosso in modo che solo il contenuto rimanga visibile.',
        'overlay_type_info_transparent': '🔍 Il PDF di sovrapposizione viene posizionato su tutta la pagina con sfondo trasparente.\nLo sfondo bianco viene rimosso automaticamente - ideale per filigrane e loghi!',
        'overlay_type_info_stamp': '🖊️ Il PDF di sovrapposizione viene posizionato e ridimensionato come timbro.\nPerfetto per loghi, timbri o firme in posizioni specifiche.',
        'overlay_remove_background': 'Rimuovi sfondo bianco:',
        'overlay_remove_background_enable': 'Rimuovi lo sfondo bianco dal PDF di sovrapposizione (rende la sovrapposizione trasparente)',
        'overlay_remove_background_tooltip': 'Rimuove le aree bianche dal PDF di sovrapposizione in modo che il testo sottostante diventi visibile.',
        'overlay_threshold': 'Valore soglia:',
        'overlay_threshold_hint': '(1-254, più alto = più bianco viene rimosso)',
        'overlay_select_file': 'Seleziona PDF di sovrapposizione:',
        'overlay_file_placeholder': 'Seleziona un file PDF per la sovrapposizione',
        'overlay_browse': 'Sfoglia...',
        'overlay_select_overlay': 'Seleziona PDF di sovrapposizione',
        'overlay_range': 'Intervallo di pagine:',
        'overlay_all_pages': 'Tutte le pagine',
        'overlay_custom_range': 'Intervallo personalizzato',
        'overlay_from': 'Da:',
        'overlay_to': 'A:',
        'overlay_position': 'Posizione:',
        'overlay_position_center': 'Centro',
        'overlay_position_top_left': 'In alto a sinistra',
        'overlay_position_top_right': 'In alto a destra',
        'overlay_position_bottom_left': 'In basso a sinistra',
        'overlay_position_bottom_right': 'In basso a destra',
        'overlay_size': 'Dimensione:',
        'overlay_size_original': 'Dimensione originale',
        'overlay_size_fit_page': 'Adatta alla pagina',
        'overlay_size_custom': 'Personalizzato (%)',
        'overlay_opacity': 'Trasparenza:',
        'overlay_target_folder': 'Cartella di destinazione:',
        'overlay_browse_folder': 'Sfoglia...',
        'overlay_select_folder': 'Seleziona la cartella di destinazione',
        'overlay_warning': '⚠️ Nota: Il PDF di sovrapposizione viene posizionato sul PDF di base e "bruciato" al suo interno.\n\nGli elementi del PDF di sovrapposizione non possono più essere modificati singolarmente dopo il salvataggio.',
        'overlay_apply': 'Sovrapponi',
        'overlay_start': 'Avvio sovrapposizione...',
        'overlay_progress': 'Sovrapposizione PDF...',
        'overlay_success': 'PDF sovrapposto con successo!\n\nSalvato come:\n{0}\n\nVuoi aprire il PDF sovrapposto?',
        'overlay_complete': 'Sovrapposizione completata',
        'overlay_cancel': 'Sovrapposizione annullata',
        'overlay_error_format': 'Errore durante la sovrapposizione:\n\n{0}',
        'overlay_no_file': 'Nessun PDF di sovrapposizione selezionato.\n\nSeleziona un file PDF da sovrapporre.',
        'filename_overlay_suffix': '_sovrapposto',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Estrai immagini dal PDF',
        'extract_images_menu': 'Estrai tutte le immagini',
        'extract_images_info': 'Estrae tutte le immagini dal PDF e le salva come file separati.\n\nLe immagini vengono salvate nel loro formato originale o convertite in un formato selezionato.',
        'extract_images_format': 'Formato immagine:',
        'extract_images_quality': 'Qualità JPEG:',
        'extract_images_options': 'Opzioni:',
        'extract_images_subfolder': 'Estrai in sottocartella ("nomePDF_immagini")',
        'extract_images_unique': 'Solo immagini uniche (evita duplicati)',
        'extract_images_range': 'Intervallo di pagine:',
        'extract_images_all_pages': 'Tutte le pagine',
        'extract_images_custom_range': 'Intervallo personalizzato',
        'extract_images_from': 'Da:',
        'extract_images_to': 'A:',
        'extract_images_target_folder': 'Cartella di destinazione:',
        'extract_images_browse': 'Sfoglia...',
        'extract_images_select_folder': 'Seleziona la cartella di destinazione',
        'extract_images_info_box': 'Informazioni',
        'extract_images_info_text': 'L\'estrazione può richiedere diversi minuti per PDF di grandi dimensioni.\n\nLe immagini vengono salvate con il loro nome originale (pagina_immagine).',
        'extract_images_extract': 'Estrai',
        'extract_images_start': 'Avvio estrazione...',
        'extract_images_progress': 'Estrazione immagini...',
        'extract_images_success': '✅ Immagini estratte con successo!\n\n{0} immagini sono state salvate in:\n{1}',
        'extract_images_complete': 'Estrazione immagini completata',
        'extract_images_cancel': 'Estrazione annullata',
        'extract_images_error_format': 'Errore durante l\'estrazione delle immagini:\n\n{0}',
        'extract_images_open_folder': '📁 Apri cartella',
        'extract_images_no_images': 'Nessuna immagine trovata nel PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Più pagine su una pagina (N-Up)',
        'nup_menu': 'Più pagine su una pagina (N-Up)',
        'nup_info': 'Dispone più pagine PDF su una pagina.\n\nIdeale per stampe compatte, panoramiche o dispense.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Anteprima:',
        'nup_preview_info': '{0} pagine → {1} pagine per foglio → {2} fogli\nLayout: {3}',
        'nup_order': 'Ordine:',
        'nup_order_horizontal': 'Orizzontale (riga per riga)',
        'nup_order_vertical': 'Verticale (colonna per colonna)',
        'nup_order_horizontal_reverse': 'Orizzontale inverso',
        'nup_order_vertical_reverse': 'Verticale inverso',
        'nup_range': 'Intervallo di pagine:',
        'nup_all_pages': 'Tutte le pagine',
        'nup_custom_range': 'Intervallo personalizzato',
        'nup_from': 'Da:',
        'nup_to': 'A:',
        'nup_options': 'Opzioni:',
        'nup_margins': 'Margini:',
        'nup_margin_between': 'Spaziatura tra le pagine:',
        'nup_page_numbers': 'Inserisci numeri di pagina',
        'nup_target_folder': 'Cartella di destinazione:',
        'nup_browse': 'Sfoglia...',
        'nup_select_folder': 'Seleziona la cartella di destinazione',
        'nup_create': 'Crea',
        'nup_start': 'Avvio N-Up...',
        'nup_progress': 'Creazione N-Up...',
        'nup_success': 'N-Up creato con successo!\n\nSalvato come:\n{0}\n\nVuoi aprire il nuovo PDF?',
        'nup_complete': 'N-Up completato',
        'nup_cancel': 'N-Up annullato',
        'nup_error_format': 'Errore durante N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Modifica dimensione pagina',
        'pagesize_menu': 'Modifica dimensione pagina',
        'pagesize_info': 'Modifica la dimensione della pagina del PDF.\n\nIl contenuto viene automaticamente adattato alla nuova dimensione.',
        'pagesize_format': 'Formato:',
        'pagesize_select': 'Seleziona un formato standard:',
        'pagesize_custom': 'Dimensione personalizzata:',
        'pagesize_width': 'Larghezza:',
        'pagesize_height': 'Altezza:',
        'pagesize_orientation': 'Orientamento:',
        'pagesize_portrait': 'Ritratto',
        'pagesize_landscape': 'Paesaggio',
        'pagesize_scale_options': 'Opzioni di scala:',
        'pagesize_fit': 'Adatta (mantieni proporzioni)',
        'pagesize_stretch': 'Allunga (distorci)',
        'pagesize_center': 'Centra (dimensione originale)',
        'pagesize_range': 'Intervallo di pagine:',
        'pagesize_all_pages': 'Tutte le pagine',
        'pagesize_custom_range': 'Intervallo personalizzato',
        'pagesize_from': 'Da:',
        'pagesize_to': 'A:',
        'pagesize_target_folder': 'Cartella di destinazione:',
        'pagesize_browse': 'Sfoglia...',
        'pagesize_select_folder': 'Seleziona la cartella di destinazione',
        'pagesize_apply': 'Applica',
        'pagesize_start': 'Avvio modifica dimensione pagina...',
        'pagesize_progress': 'Modifica dimensione pagina...',
        'pagesize_success': 'Dimensione pagina modificata con successo!\n\nSalvato come:\n{0}\n\nVuoi aprire il nuovo PDF?',
        'pagesize_complete': 'Modifica dimensione pagina completata',
        'pagesize_cancel': 'Modifica dimensione pagina annullata',
        'pagesize_error_format': 'Errore durante la modifica della dimensione pagina:\n\n{0}',
        'pagesize_preview_info': 'Nuova dimensione: {0} x {1} pt',
        'filename_pagesize_suffix': '_nuova_dimensione',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informazioni PDF',
        'pdf_info_menu': 'Mostra informazioni PDF',
        'pdf_info_voice': 'Visualizzazione informazioni PDF',
        'pdf_info_error': 'Errore durante la visualizzazione delle informazioni PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Mostra scorciatoie da tastiera",
        "shortcuts_dialog_title": "Scorciatoie da tastiera",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FILE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Apri PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Chiudi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Salva con nome...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Proteggi documento</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Stampa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Stampa immediata (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Esci dall'applicazione</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 ESPORTA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Esporta come Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Esporta come DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Esporta come TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Esporta come immagini (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Estrai immagini</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ELABORAZIONE DOCUMENTI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Pagine multiple)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Conversione PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Appiattisci PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Sovrapponi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Ottimizza PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ MODIFICA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Cerca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Aggiungi segnalibro</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Gestisci segnalibri</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Segnalibro successivo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Segnalibro precedente</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Esegui OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 GESTIONE PAGINE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Ruota pagina corrente</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Ruota tutte le pagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizza pagina corrente</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizza tutte le pagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Elimina pagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Estrai pagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Inserisci pagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Sposta pagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Unisci PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Modifica dimensione pagina</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INSERISCI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Inserisci testo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Inserisci croce</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Inserisci firma 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Inserisci firma 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Inserisci immagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Inserisci rettangolo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Inserisci ellisse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Inserisci linea</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Inserisci freccia</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Inserisci numeri di pagina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Filigrana testo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Filigrana immagine</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ OSCURAMENTI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Oscuramento (nero)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Oscuramento (bianco)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Applica tutti gli oscuramenti</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANZATO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Ritaglia PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Modifica metadati</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VISUALIZZA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Alterna modalità Scura/Chiara</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Mostra finestra testo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Larghezza pagina (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Due pagine (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Panoramica (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ IMPOSTAZIONI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Gestione password</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Impostazioni OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Impostazioni firma</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formattazione nomi file</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Esporta impostazioni</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importa impostazioni</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Mostra informazioni PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Attiva/disattiva uscita vocale</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Focalizza barra dei menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nuova versione disponibile",
        "update_available_message": "È disponibile una nuova versione <b>{0}</b>.\n\nVisita la pagina delle release per scaricare l'aggiornamento:\n{1}",
        "update_available_voice": "Nuova versione {0} disponibile. Scarica l'aggiornamento dalla pagina GitHub.",
        "update_open_release": "Apri pagina delle release",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Scarica tutte le traduzioni",
        "ask_download_all_translations": """Oltre a tedesco, inglese e vietnamita, sono disponibili {total_languages} altre lingue dell'interfaccia.\n\nDevono essere fornite / aggiornate?\n\nNota:\nLe lingue non necessarie possono essere eliminate manualmente in seguito nella directory:\n{translations_path}
        \nSe annulli, puoi scaricare le lingue dell'interfaccia in seguito tramite il menu 'Strumenti → Aggiorna traduzioni'.""",
        "menu_update_translations": "Aggiorna traduzioni",
        "translations_updated": "Traduzioni aggiornate",
        "translations_update_success": "{} traduzioni sono state aggiornate con successo ({} nuove, {} aggiornate).",
        "translations_update_error": "Errore durante l'aggiornamento delle traduzioni",
        "translations_update_no_changes": "Tutte le traduzioni sono già aggiornate.",
        "translations_update_offline": "Nessuna connessione Internet. Le traduzioni non possono essere aggiornate.",
        "translations_update_in_progress": "Le traduzioni vengono aggiornate in background...",
        "translations_downloading": "Download delle traduzioni in corso...",
        "translations_path_hint": "Directory utente per le traduzioni",
        "translations_update_not_available_title": "Aggiornamento non disponibile",
        "translations_update_not_available_message": """L'aggiornamento delle traduzioni è disponibile solo nella versione installata.\n\nIn modalità sviluppo, le traduzioni sono già aggiornate.""",
        "translations_update_no_internet_title": "Nessuna connessione Internet",
        "translations_update_no_internet_message": """Impossibile stabilire una connessione Internet.\n\nLe traduzioni non possono essere scaricate da GitHub.\n\nPossibili soluzioni:
        • Controlla la tua connessione Internet
        • Disabilita temporaneamente eventuali firewall
        • Riprova più tardi
        \nPuoi anche scaricare le traduzioni manualmente da GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "L'aggiornamento è già in corso",
        "btn_retry": "Riprova",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Benvenuto in PDF Dark View",
        "welcome_title_not_supported": "Benvenuto in PDF Dark View",
        "welcome_message": "Benvenuto in PDF Dark View!\n\nLa lingua del tuo sistema è stata riconosciuta come '{language}'.\nVuoi usare questa lingua per l'interfaccia utente?\n\nPuoi cambiare lingua in qualsiasi momento tramite 'Impostazioni → Lingua'.",
        "welcome_message_language_not_available": "Benvenuto in PDF Dark View!\n\nLa lingua del tuo sistema è stata riconosciuta come '{language}'.\nQuesta lingua non è ancora installata.\n\nVuoi scaricare ora le traduzioni per {language} da GitHub?\n\n(La lingua verrà quindi utilizzata automaticamente per l'interfaccia utente.)",
        "welcome_message_language_not_supported": "Benvenuto in PDF Dark View!\n\nLa lingua del tuo sistema è stata riconosciuta come '{language}'.\nSfortunatamente, non ci sono ancora traduzioni per questa lingua.\n\nL'interfaccia utente sarà visualizzata in {fallback_language}.\n\nPuoi cambiare lingua in qualsiasi momento tramite 'Impostazioni → Lingua'.\nSe vuoi, puoi anche contribuire con una traduzione per la tua lingua:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Sì, usa la lingua di sistema",
        "welcome_keep_english": "No, mantieni l'inglese",
        "welcome_download_language": "Sì, scarica {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Il programma si sta chiudendo",

    }
