
# ============================================
# translations_es.py - Diccionario español
# Completamente ordenado por categorías
# Comentarios en alemán para coherencia
# ============================================

def load_spanish_strings():
    """Carga todas las cadenas en español"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View por BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Abrir PDF",
        'btn_text_window': "Texto OCR",
        'btn_first': "Primera página",
        'btn_prev': "Página anterior",
        'btn_next': "Página siguiente",
        'btn_last': "Última página",
        'btn_print': "Imprimir",
        'btn_darkmode_light': "Modo claro",
        'btn_darkmode_dark': "Modo oscuro",
        'btn_delete_pages': "Eliminar páginas",
        'btn_extract_pages': "Extraer páginas",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "Aceptar",
        'btn_cancel': "Cancelar",
        'btn_save': "Guardar",
        'btn_close': "Cerrar",
        'btn_delete': "Eliminar",
        'btn_delete_all': "Eliminar todo",
        'btn_copy': "Copiar",
        'btn_export': "Exportar",
        'btn_show': "Mostrar contr.",
        'btn_hide': "Ocultar contr.",
        'btn_authenticate': "Autenticar",
        'btn_settings': "Configuración",
        'btn_protect': "Proteger",
        'btn_remove_password': "Quitar contraseña",
        'btn_manage': "Gestor contraseñas",
        'btn_retry': "Reintentar",
        'btn_select_all': "Seleccionar todo",
        'btn_clear_selection': "Deseleccionar",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Página {0} de {1}",
        'page_count': "de {0}",
        'goto_page': "Ir a la página",
        'page_simple': "Página {0}",
        'full_view_page': "Vista completa página {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Introducir término + Intro",
        'search_results': "Resultados: {0} de {1}",
        'search_nav_hint': "Intro: siguiente  (Mayús+Intro: anterior)",
        'search_no_results': "Sin resultados",
        'search_error': "Error de búsqueda",
        'search_active': "Campo de búsqueda activado",
        'search_closed': "Búsqueda finalizada",
        'search_position': "Página {0} {1}",
        'search_pos_top': "arriba del todo",
        'search_pos_upper': "arriba",
        'search_pos_middle': "medio",
        'search_pos_lower': "abajo",
        'search_pos_bottom': "abajo del todo",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "¡Reconocimiento de texto completado con éxito!",
        'ocr_success_title': "OCR exitoso",
        'ocr_success_message': "El documento ahora es buscable.",
        'ocr_failed': "OCR falló",
        'ocr_in_progress': "OCR en curso",
        'ocr_preparing': "Preparando PDF...",
        'ocr_analyzing': "Analizando PDF...",
        'ocr_optimizing': "Optimizando imagen...",
        'ocr_recognizing': "Reconociendo texto...",
        'ocr_embedding': "Incrustando texto...",
        'ocr_finalizing': "Finalizando PDF...",
        'ocr_not_available': "OCR no disponible",
        'ocr_install_message': "No se encontraron herramientas OCR.\n\nPor favor, instale:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR necesario",
        'ocr_question': "El PDF no contiene texto buscable.\n¿Desea ejecutar OCR para permitir {0}?",
        'ocr_perform': "Ejecutar OCR",
        'ocr_later': "Más tarde",
        'ocr_starting': "Iniciando OCR garantizado...",
        'ocr_success_voice': "OCR exitoso. El PDF ahora es buscable.",
        'ocr_partial_success': "Se realizó OCR, pero hubo problemas al reemplazar.\n\nLa versión buscable se guardó en:\n{0}\n\nError: {1}",
        'ocr_partial_title': "OCR parcialmente exitoso",
        'ocr_partial_voice': "OCR realizado, pero el reemplazo falló.",
        'original_file': "Archivo original:",
        'old_size': "Tamaño antiguo:    {0} bytes",
        'new_size': "Tamaño nuevo: {0} bytes",
        'size_change': "Cambio: {0}{1} bytes",
        'backup_created_file': "Copia de seguridad creada:\n{0}",
        'backup_not_created': "Copia de seguridad: no creada (ajuste desactivado)",
        'page_header': "=== Página {0} ===\n{1}\n",
        'scanned_page_header': "=== Página {0} (escaneada) ===\n[Esta página solo contiene texto escaneado]\n[Por favor, ejecute OCR manualmente]\n",
        'scanned_warning': "⚠️ TEXTO ESCANEADO - OCR NECESARIO",
        'guaranteed_title': "PDF buscable creado",
        'guaranteed_message': "<b>¡Versión buscable garantizada creada!</b>\n\nDado que el OCR automático falló, se creó un PDF alternativo buscable:\n\n{0}\n\n<b>Este archivo contiene:</b>\n• Texto extraído (si disponible)\n• Indicaciones para páginas escaneadas\n• Es totalmente buscable",
        'guaranteed_voice': "PDF buscable garantizado creado.",
        'instruction_title': "INSTRUCCIÓN PARA OCR",
        'instruction_file': "Archivo original: {0}",
        'instruction_text': "El reconocimiento automático de texto (OCR) ha fallado.\nPor favor, realice OCR manualmente:\n\n1. CON OCRmyPDF (línea de comandos):\n   ocrmypdf --force-ocr \"[ARCHIVO]\" \"salida.pdf\"\n\n2. CON ADOBE ACROBAT (macOS/Windows):\n   • Abrir el PDF en Acrobat\n   • Herramientas > Editar PDF\n   • Seleccionar 'Reconocer texto'\n\n3. CON VISTA PREVIA (macOS):\n   • Abrir el PDF en Vista Previa\n   • Archivo > Exportar...\n   • Filtro Quartz: 'Reduce File Size'\n   • Activar 'Realizar OCR'\n\n4. SERVICIOS EN LÍNEA:\n   • smallpdf.com/es/ocr-pdf\n   • ilovepdf.com/es/ocr-pdf\n   • adobe.com/es/acrobat/online/pdf-to-word.html",
        'instruction_created': "Instrucción OCR creada",
        'instruction_created_message': "Se creó una instrucción detallada:\n\n{0}\n\nPor favor, siga los pasos para OCR manual.",
        'instruction_created_voice': "Instrucción OCR creada.",
        'ocr_impossible': "OCR imposible",
        'ocr_impossible_message': "No se pudo realizar OCR.\n\nPor favor, procese '{0}' manualmente con software OCR.",
        'ocr_impossible_voice': "OCR imposible. Procese manualmente.",
        'emergency_title': "OCR de emergencia",
        'emergency_message': "Se creó un PDF de emergencia:\n\n{0}\n\nPor favor, procese este archivo manualmente con OCR.",
        'emergency_voice': "PDF de emergencia creado. Ejecute OCR manualmente.",
        'critical_error': "Error crítico",
        'critical_error_message': "No se pudo iniciar OCR.\n\nPor favor, reinicie el programa y\nverifique la instalación de OCR.",
        'critical_error_voice': "Error crítico de OCR",
        'ocr_question_html': "<p>El PDF no contiene texto buscable.<p>¿Desea ejecutar OCR para permitir <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR necesario. El PDF no contiene texto buscable. ¿Desea ejecutar OCR para permitir {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ningún PDF cargado",
        'no_pdf_message': "No hay ningún PDF cargado",
        'pdf_not_found': "Archivo PDF no encontrado",
        'file_size': "Tamaño del archivo",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Copia de seguridad creada",
        'backup_disabled': "Copia de seguridad desactivada",
        'backup_activated': "Creación de copia de seguridad activada",
        'backup_deactivated': "Creación de copia de seguridad desactivada",
        'backup_status': "Copia de seguridad: {0}",
        'backup_on': "✔ activada",
        'backup_off': "✘ desactivada",
        'close_pdf': "Cerrando PDF: {0}",
        'pdf_not_found_format': "Archivo PDF no encontrado: {0}",
        'error_pdf_load_format': "Error al cargar el PDF: {0}",
        'load_failed_format': "Carga fallida:\n{0}",
        'decrypted_suffix': "(descifrado)",
        'decryption_failed': "Descifrado fallido.",
        'decryption_error': "Error al descifrar",
        'decryption_success': "Descifrado exitoso",
        'decryption_success_message': "El PDF se descifró y guardó en:\n\n{0}",
        'decryption_success_voice': "PDF descifrado y guardado.",
        'password_remove_error': "Error al quitar la contraseña",
        'save_unencrypted': "Guardar PDF sin cifrar como",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Guardar como...",
        'save_copy': "Guardar copia",
        'save_success': "PDF guardado en: {0}",
        'save_encrypted': "PDF protegido guardado en: {0}",
        'save_error': "No se pudo guardar el PDF",
        'encryption_question': "¿Desea proteger el PDF con una contraseña?",
        'encryption_yes': "Sí",
        'encryption_no': "No",
        'encryption_cancel': "Cancelar",
        'save_cancel': "Guardado cancelado",
        'save_encrypted_voice': "Archivo cifrado y guardado.",
        'save_success_voice': "El archivo PDF se guardó sin cifrar.",
        'save_error_format': "No se pudo guardar el PDF:\n{0}",
        'export_pages_success': "Exportación a Pages exitosa",
        'export_pages_error': "Error al exportar a Pages",
        'export_pages_error_format': "Error al exportar a Pages: {0}",
        'export_word_success': "Exportación a Word exitosa",
        'export_word_error': "Error al exportar a Word",
        'export_word_error_format': "Error al exportar a Word: {0}",
        'export_text_success': "Exportación a texto exitosa",
        'export_text_error': "Error al exportar a texto",
        'export_text_error_format': "Error al exportar a texto: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Contraseña requerida",
        'password_enter': "Por favor, introduzca la contraseña",
        'password_confirm': "Confirmar contraseña",
        'password_new': "Nueva contraseña",
        'password_current': "Contraseña actual",
        'password_save': "Guardar contraseña (cifrada)",
        'password_saved': "✓ Contraseña para este archivo guardada",
        'password_wrong': "Contraseña incorrecta",
        'password_mismatch': "Las contraseñas no coinciden",
        'password_too_short': "Contraseña demasiado corta",
        'password_min_length': "La contraseña debe tener al menos 4 caracteres",
        'password_strength': "Fortaleza de la contraseña",
        'password_strength_very_weak': "Muy débil",
        'password_strength_weak': "Débil",
        'password_strength_medium': "Media",
        'password_strength_strong': "Fuerte",
        'password_strength_very_strong': "Muy fuerte",
        'password_char_count': "({0} caracteres)",
        'password_match': "✓ Coinciden",
        'password_no_match': "✗ Las contraseñas no coinciden",
        'password_show': "Mostrar",
        'password_hide': "Ocultar",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Gestor de contraseñas",
        'password_table_filename': "Nombre de archivo",
        'password_table_password': "Contraseña",
        'password_count': "{0} contraseña{1} guardada{2}",
        # Para español: {0} número, {1} "s" para plural, {2} "s" para concordancia.
        # Ejemplo: 1 contraseña guardada, 2 contraseñas guardadas.
        'password_count_singular': "",
        'password_count_plural': "s",
        'password_none': "No hay contraseñas guardadas",
        'password_copied': "{0} contraseña{1} copiada{2}",
        'password_copied_singular': "",
        'password_copied_plural': "s",
        'password_delete_confirm': "¿Realmente desea eliminar la contraseña para '{0}'?",
        'password_delete_multiple': "¿Realmente desea eliminar las {0} contraseñas seleccionadas?",
        'password_delete_all_confirm': "¿Realmente desea eliminar las {0} contraseñas guardadas?",
        'password_deleted': "{0} contraseña{1} eliminada{2}",
        'password_deleted_singular': "",
        'password_deleted_plural': "s",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "s",
        'password_all_deleted': "Todas las contraseñas han sido eliminadas",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generador de contraseñas",
        'generator_generated': "Contraseña generada:",
        'generator_regenerate': "Regenerar",
        'generator_copy': "Copiar",
        'generator_use': "Usar",
        'generator_settings': "Ajustes",
        'generator_length': "Longitud:",
        'generator_group_every': "Separador cada",
        'generator_group_chars': "caracteres.   Separador:",
        'generator_uppercase': "Mayúsculas (A-Z)",
        'generator_lowercase': "Minúsculas (a-z)",
        'generator_digits': "Dígitos (0-9)",
        'generator_symbols': "Símbolos (!@#$%^&*)",
        'generator_exclude': "Excluidos:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Contraseña maestra requerida",
        'master_password_setup': "Configurar contraseña maestra",
        'master_password_change': "Cambiar contraseña maestra",
        'master_password_enter': "Por favor, introduzca su contraseña maestra",
        'master_password_choose': "Elija una contraseña maestra segura (al menos 8 caracteres)",
        'master_password_new': "Por favor, introduzca su nueva contraseña maestra",
        'master_password_confirm': "Confirmar contraseña",
        'master_password_authenticate': "Autenticar",
        'master_password_success': "Contraseña maestra configurada con éxito.",
        'master_password_changed': "Contraseña maestra cambiada con éxito.",
        'master_password_removed': "Contraseña maestra y todas las contraseñas eliminadas.",
        'master_password_remove': "Eliminar contraseña maestra",
        'master_password_remove_confirm': "¿Está SEGURO de que desea eliminar TODAS las contraseñas?\n\n¡Esta acción es IRREVERSIBLE!",
        'master_password_export_before': "¿Desea exportar una copia de seguridad antes?",
        'master_password_export_delete': "Exportar y eliminar",
        'master_password_delete_now': "Eliminar ahora",
        'master_password_for_signatures': "Para usar firmas, debe configurar una contraseña maestra.\n\n¿Desea configurar una contraseña maestra ahora?",
        'master_password_for_private': "Para usar plantillas de texto privadas, debe configurar una contraseña maestra.\n\n¿Desea configurar una contraseña maestra ahora?",
        'master_password_info': """
            <b>🔐 SIN CONTRASEÑA MAESTRA:</b><br>
            • No es posible ver, copiar ni exportar contraseñas<br>
            • Siempre se pueden eliminar contraseñas (incluso sin contraseña maestra)<br><br>

            <b>🔐 CON CONTRASEÑA MAESTRA:</b><br>
            • Todas las funciones disponibles tras autenticación<br>
            • Las contraseñas se cifran con la contraseña maestra<br>
            • Longitud mínima: 8 caracteres<br>
            • Almacenamiento seguro mediante hash SHA-256<br><br>

            <b>IMPORTANTE:</b><br>
            • Si pierde la contraseña maestra, las contraseñas no se pueden recuperar<br>
            • Al eliminar la contraseña maestra, se borran TODAS las contraseñas<br>
            • Opción de exportación disponible antes del borrado<br>
            • La contraseña maestra se puede cambiar en cualquier momento
        """,
        'signature_auth_disabled': "Desactivar solicitud de contraseña para firmas",
        'template_auth_disabled': "Desactivar solicitud de contraseña para plantillas privadas",
        'master_password_for_signatures_settings': "Para usar firmas, debe configurar una contraseña maestra.\n\nVaya a Configuración - Gestor de contraseñas",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Proteger PDF",
        'protect_info': "El archivo '{0}' será protegido con contraseña.",
        'protect_instruction': "Por favor, introduzca dos veces la contraseña deseada para proteger el documento, o use el generador de contraseñas a la derecha del campo de entrada.",
        'protect_success': "El PDF se protegió con éxito y se guardó en:\n{0}\n\nContraseña: {1}\n\n¿Desea abrir el PDF protegido ahora?",
        'protect_open': "Sí",
        'protect_skip': "No",
        'protect_error': "Error al proteger el PDF",
        'protect_open_title': "abrir PDF protegido",
        'protect_question': "Completado. ¿Desea abrir el PDF protegido ahora? ¿Sí o No?",
        'password_cancel': "Diálogo de contraseña cancelado",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Eliminar páginas",
        'pages_extract': "Extraer páginas",
        'pages_insert': "Insertar páginas",
        'pages_move': "Mover páginas",
        'pages_delete_options': "Opciones de eliminación",
        'pages_delete_empty': "Eliminar todas las páginas vacías",
        'pages_delete_current': "Eliminar página actual",
        'pages_delete_range': "Eliminar rango de páginas",
        'pages_extract_options': "Opciones de extracción",
        'pages_extract_current': "Extraer página actual",
        'pages_extract_range': "Extraer rango de páginas",
        'pages_insert_position': "Posición de inserción",
        'pages_insert_before': "Insertar antes de la página:",
        'pages_insert_select': "Seleccionar PDF",
        'pages_insert_none': "Ningún PDF seleccionado",
        'pages_move_source': "Páginas a mover",
        'pages_move_from': "Desde página:",
        'pages_move_to': "Hasta página:",
        'pages_move_target': "Posición destino",
        'pages_move_before': "Mover antes de la página:",
        'pages_move_hint': "Nota: página 1 = inicio, {0} = fin",
        'pages_range_invalid': "La página de inicio debe ser menor o igual que la página de fin.",
        'pages_position_invalid': "La posición destino no debe estar dentro del rango a mover.",
        'pages_no_pdf_selected': "No hay ningún PDF seleccionado.",
        'pages_deleted': "Se eliminaron {0} páginas.",
        'pages_extracted': "Extraído: {0}\nGuardado en: {1}\nTamaño: {2:.1f} KB",
        'pages_inserted': "{0} páginas insertadas",
        'pages_moved': "Se movieron {0} páginas.",
        'pages_deleted_none': "No se eliminó ninguna página.",
        'pages_delete_progress': "Eliminando páginas...",
        'pages_deleted_with_backup': "Se eliminaron {0} páginas.\n\nCopia de seguridad: {1}",
        'pages_deleted_voice': "Se creó una copia de seguridad y se eliminaron {0} páginas.",
        'info': "Información",
        'error_dialog_creation': "No se pudo crear el diálogo",
        'extract_page_single': "Extraer página {0}",
        'extract_page_range': "Extraer páginas {0}–{1}",
        'extract_success_voice': "Páginas extraídas con éxito",
        'extract_error_format': "Error al extraer: {0}",
        'pages_inserted_voice': "{0} páginas insertadas.",
        'insert_error_format': "Error al insertar: {0}",
        'pages_move_progress': "Moviendo páginas...",
        'pages_moved_with_backup': "Se movieron {0} páginas.\n\nCopia de seguridad: {1}",
        'move_success_title': "Movimiento exitoso",
        'pages_moved_voice': "{0} páginas movidas con éxito",
        'mark_removed': "Marcado eliminado de la página {0}",
        'mark_empty': "Página {0} marcada como vacía",
        'mark_export_removed': "Marcado de exportación eliminado de la página {0}",
        'mark_export': "Página {0} marcada para exportar",
        'no_empty_pages': "No hay páginas vacías marcadas para eliminar",
        'delete_empty_confirm': "¿Desea eliminar las {0} páginas vacías marcadas?",
        'delete_empty_confirm_voice': "¿Eliminar ahora las {0} páginas vacías marcadas? Sí o No.",
        'empty_pages_deleted': "{0} páginas vacías eliminadas",
        'no_export_pages': "No hay páginas marcadas para exportar",
        'overwrite_title': "Sobrescribir archivo existente",
        'overwrite_question': "El archivo\n\n{0}\n\nya existe.\n¿Desea sobrescribirlo?",
        'overwrite_voice': "¿Sobrescribir archivo existente? Sí o No.",
        'page_skipped': "Página {0} omitida",
        'export_complete': "Exportación completada.",
        'export_complete_voice': "La exportación ha finalizado.",
        'no_pages_exported': "Ninguna página exportada",
        'export_cancelled': "Exportación cancelada",
        'pages_exported': "{0} páginas exportadas a {1}",
        'export_page_title': "Exportar página",
        'page_exported': "Página {0} exportada a {1}",
        'export_error': "Error al exportar",
        'export_marked_title': "Exportar páginas marcadas",
        'rotate_all_title': "rotar todas las páginas",
        'rotate_all_question': "¿Desea rotar todas las páginas 90 grados a la derecha?",
        'rotate_all_voice': "¿Desea rotar todas las páginas 90 grados a la derecha? ¿Sí o No?",
        'all_pages_rotated': "Todas las páginas rotadas",
        'page_rotated': "Página {0} rotada",
        'rotate_error': "No se pudo rotar la página",
        'delete_page_confirm': "¿Desea eliminar la página {0}?",
        'delete_page_confirm_voice': "¿Realmente desea eliminar la página {0}? Sí o No.",
        'page_deleted': "Página {0} eliminada",
        'delete_error': "No se pudo eliminar la página",
        'pages_deleted_voice': "{0} páginas eliminadas",
        'pages_exported_split': "{0} páginas se exportaron con éxito.",
        'pages_skipped': "{0} páginas se omitieron.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extraer páginas (avanzado)",
        'pdf_splitter_title': "Divisor y extractor PDF",
        'pdf_splitter_load': " Seleccionar archivo PDF",
        'pdf_splitter_info': "Por favor, elija una opción para su documento PDF",
        'pdf_splitter_basic': "Operaciones básicas",
        'pdf_splitter_single': "Dividir en páginas individuales",
        'pdf_splitter_range': "Extraer páginas:",
        'pdf_splitter_range_placeholder': "ej. 1-3,5,7-9",
        'pdf_splitter_clean': "Operaciones de limpieza",
        'pdf_splitter_remove_empty': "Eliminar todas las páginas vacías",
        'pdf_splitter_remove': "Eliminar rango de páginas:",
        'pdf_splitter_remove_placeholder': "ej. 2,4-6",
        'pdf_splitter_process': "Procesar PDF",
        'pdf_splitter_loaded': "PDF cargado. Por favor, elija una opción",
        'pdf_read_error': "No se pudo leer el PDF",
        'pages': "Páginas",
        'pages_created': "Páginas creadas",
        'range_empty': "Por favor, introduzca un rango de páginas",
        'range_invalid': "Rango de páginas inválido",
        'range_created': "Nuevo PDF con las páginas seleccionadas creado:\n{0}",
        'empty_removed': "{0} páginas vacías eliminadas.\nSalida: {1}",
        'remove_empty': "Por favor, introduzca páginas a eliminar",
        'remove_invalid': "Páginas a eliminar inválidas",
        'remove_done': "PDF limpio creado:\n{0}",
        'open_folder': "Abrir carpeta",
        'show_in_finder': "Mostrar en Finder",
        'pdf_splitter_no_pdf': "Por favor, cargue primero un archivo PDF.",
        'process_error': "Error al procesar el PDF",
        'pages_created_voice': "Se crearon {0} páginas",
        'range_created_voice': "Se creó un PDF con las páginas seleccionadas",
        'empty_removed_voice': "Se eliminaron {0} páginas vacías",
        'remove_done_voice': "Se creó un PDF limpio",
        'pdf_splitter_split_groups': "Cada grupo contiguo en archivo separado",
        'range_created_single': "Nuevo PDF creado:\n{0}",
        'range_created_multiple': "Se crearon {0} archivos PDF.",
        'range_created_voice_single': "Se creó un PDF con las páginas seleccionadas",
        'range_created_voice_multiple': "Se crearon {0} archivos PDF",
        'empty_removed_none_left': "No quedan páginas",
        'empty_removed_all_empty': "Todas las páginas fueron reconocidas como vacías y se eliminarían. No se creó ningún archivo.",
        'preview_single': "Vista previa: {0}",
        'preview_enter_range': "Por favor, introduzca un rango de páginas.",
        'preview_invalid_range': "Rango de páginas inválido.",
        'preview_file': "Vista previa: {0}",
        'preview_files': "Vista previa: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Iniciando impresión",
        'print_sent': "Trabajo de impresión enviado",
        'print_now': "Imprimir ahora",
        'print_error': "Error al imprimir directamente",
        'print_limited': "Función de impresión limitada en este sistema",
        'print_error_format': "Error al imprimir directamente: {0}",
        'warning': "Aviso",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Cambiar a modo claro",
        'mode_switch_to_dark': "Cambiar a modo oscuro",
        'mode_dark_activated': "Modo oscuro activado",
        'mode_light_activated': "Modo claro activado",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Página completa",
        'zoom_two_pages': "Dos páginas lado a lado",
        'zoom_overview': "Vista general",
        'zoom_cannot_during_search': "No se puede hacer zoom durante la búsqueda",
        'zoom_exit_first': "Por favor, salga primero del zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Arrastrar y soltar activado",
        'drag_disabled': "Arrastrar y soltar desactivado",
        'drag_page_grab': "Arrastrando página {0}",
        'drag_page_dropped': "Página {0} insertada en posición {1}",
        'drag_position_invalid': "Posición inválida",
        'drag_same_position': "La página {0} permanece en posición {0}",
        'drag_error': "Error al mover",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Entrada de texto con formato avanzado y gestor de plantillas",
        'text_templates': "Plantillas de texto disponibles:",
        'text_name': "Nombre",
        'text_preview': "Vista previa del texto",
        'text_enter': "Texto:",
        'text_font_size': "Tamaño de letra:",
        'text_formatting': "Formato:",
        'text_bold': "Negrita",
        'text_italic': "Cursiva",
        'text_underline': "Subrayado",
        'text_alignment': "Alineación:",
        'text_left': "Izquierda",
        'text_center': "Centrado",
        'text_right': "Derecha",
        'text_color': "Color del texto:",
        'text_opacity': "Opacidad:",
        'text_word_wrap': "Ajuste de línea:",
        'text_auto': "Automático",
        'text_page_width_95': "Ancho de página (95%)",
        'text_page_width_85': "Muy ancho (85%)",
        'text_page_width_75': "Más ancho (75%)",
        'text_page_width_60': "Ancho (60%)",
        'text_page_width_50': "Medio (50%)",
        'text_page_width_30': "Estrecho (30%)",
        'text_page_width_20': "Más estrecho (20%)",
        'text_page_width_10': "Muy estrecho (10%)",
        'text_no_wrap': "Sin ajuste",
        'text_private': "Plantilla privada (requiere autenticación)",
        'text_preview_label': "Vista previa:",
        'text_preview_placeholder': "Aquí se mostrará una vista previa del texto...",
        'text_no_text': "(Sin texto)",
        'text_save_template': "💾 Guardar como plantilla",
        'text_delete_template': "🗑 Eliminar plantilla seleccionada",
        'text_show_private': "Mostrar privadas",
        'text_hide_private': "Ocultar privadas",
        'text_use': "✅ Usar texto",
        'text_saved': "Plantilla de texto guardada como:\n{0}",
        'text_saved_voice': "Plantilla de texto guardada",
        'text_deleted': "Plantilla de texto eliminada",
        'text_no_text_to_save': "No hay texto para guardar.",
        'text_no_templates': "No se encontraron plantillas de texto",
        'text_private_master_required': "Las plantillas privadas solo pueden usarse si hay una contraseña maestra configurada.\n\n¿Desea configurar una contraseña maestra ahora?",
        'text_filename': "Nombre de archivo para la plantilla (sin 'Text_' ni '.txt'):",
        'text_filename_hint': "Ejemplo: 'Teléfono Casa' se guardará como 'Text_Teléfono Casa.txt'",
        'text_save_hint': "La plantilla se guardará automáticamente con su formato.",
        'text_guide_title': "Entrada de texto - Guía",
        'text_delete_confirm': "¿Realmente desea eliminar la plantilla de texto?\n\nArchivo: {0}\nTexto: {1}...",
        'text_make_public': "Marcar como pública",
        'text_make_private': "Marcar como privada",
        'text_privacy_changed': "Estado de privacidad cambiado",
        'text_private_always': "Privadas siempre visibles (ajuste)",
        'text_mode_required': "Por favor, active primero el modo texto",
        'text_continue_editing': "Continuar editando - cursor al final del texto",
        'text_no_input': "No se introdujo texto - texto descartado",
        'save_dialog_question': "¿Cómo desea proceder?",
        'text_save_question': "¿Guardar todos los textos y cruces, ajustar, seguir editando o descartar?",
        'copy_cross': "Cruz copiada",
        'paste_cross': "Cruz pegada",
        'paste_text': "Texto pegado",
        'cross_discarded': "Cruz descartada",
        'all_discarded': "Todo descartado",
        'text_discarded': "Texto descartado",
        'no_texts_to_save': "No hay textos para guardar",
        'no_valid_texts': "No hay textos válidos para guardar",
        'text_word_singular': "texto",
        'text_word_plural': "textos",
        'cross_word_singular': "cruz",
        'cross_word_plural': "cruces",
        'texts_saved_title': "Textos guardados",
        'texts_crosses_saved': "{0} {1} y {2} {3} se insertaron en el PDF.\n\nPDF recargado...",
        'texts_crosses_saved_voice': "{0} {1} y {2} {3} guardados.",
        'texts_saved': "{0} {1} se insertaron en el PDF.\n\nPDF recargado...",
        'texts_saved_voice': "{0} {1} guardados.",
        'crosses_saved': "{0} {1} se insertaron en el PDF.\n\nPDF recargado...",
        'crosses_saved_voice': "{0} {1} guardados.",
        'elements_saved': "{0} elementos se insertaron en el PDF.\n\nPDF recargado...",
        'elements_saved_voice': "{0} elementos guardados.",
        'text_window_load_error': "No se pudo cargar la ventana de texto",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Entrada de texto y plantillas – Guía detallada**

        **1. Insertar y editar texto**
        - Haga clic derecho en la posición deseada del documento y seleccione "Insertar texto".
        - Se abrirá un diálogo donde puede introducir y formatear su texto:
        • Tamaño de letra, Negrita, Cursiva, Subrayado
        • Color del texto (libre elección)
        • Transparencia (opacidad) mediante control deslizante
        • Ajuste de línea (diferentes anchos, ej. ancho de página, estrecho, sin ajuste)
        - Tras confirmar, el texto aparece en la posición del clic. Puede moverlo con el ratón o las teclas de flecha.
        - Doble clic sobre el texto abre el modo edición; Esc lo cierra.

        **2. Gestionar plantillas de texto**
        - En el diálogo de texto, a la izquierda ve una lista de todas las plantillas guardadas.
        - **Guardar una plantilla:** Introduzca su texto, déle formato y haga clic en "💾 Guardar como plantilla". Introduzca un nombre de archivo (sin extensión).
        - **Cargar una plantilla:** Haga clic en el nombre deseado de la lista. El texto y el formato se aplican y pueden ajustarse si es necesario.
        - **Eliminar:** Haga clic derecho sobre una plantilla para eliminarla o cambiar su estado privado/público.

        **3. Plantillas privadas (contraseña maestra)**
        - Si ha configurado una contraseña maestra (en Configuración → Gestor de contraseñas), puede marcar plantillas como "privadas".
        - Active la casilla "Plantilla privada" en el diálogo antes de guardar.
        - Las plantillas privadas solo se muestran en la lista si ha introducido su contraseña maestra una vez por sesión (autenticación mediante el icono de candado o al primer acceso).
        - Así protege plantillas confidenciales del acceso no autorizado.

        **4. Insertar cruces**
        - A través del menú contextual también puede insertar una cruz gráfica (por ejemplo, para casillas de verificación).
        - El tamaño, grosor de línea y color de las cruces pueden ajustarse globalmente en los ajustes (menú "Configuración" → "Ajustes de cruces").
        - Haga clic derecho sobre una cruz existente para modificarla individualmente.

        **5. Acciones por lotes**
        - Si ha colocado varios textos o cruces en una página, puede guardarlos o descartarlos todos juntos mediante el menú contextual (clic derecho en modo texto).
        - Al guardar, todos los elementos se incrustan en el PDF y permanecen como gráficos vectoriales.

        **6. Atajos de teclado en modo texto**
        - Teclas de flecha: mover elemento
        - Ctrl+Flechas: pasos más grandes
        - Intro: abrir diálogo de guardado (guardar todo / ajustar / descartar)
        - Esc: descartar elemento actual
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Entrada de texto y plantillas – Guía detallada</strong></p>

        <p><strong>1. Insertar y editar texto</strong></p>
        <ul>
        <li>Haga clic derecho en la posición deseada del documento y seleccione "Insertar texto".</li>
        <li>Se abrirá un diálogo donde puede introducir y formatear su texto:<br/>
        • Tamaño de letra, Negrita, Cursiva, Subrayado<br/>
        • Color del texto (libre elección)<br/>
        • Transparencia (opacidad) mediante control deslizante<br/>
        • Ajuste de línea (diferentes anchos, ej. ancho de página, estrecho, sin ajuste)</li>
        <li>Tras confirmar, el texto aparece en la posición del clic. Puede moverlo con el ratón o las teclas de flecha.</li>
        <li>Doble clic sobre el texto abre el modo edición; Esc lo cierra.</li>
        </ul>

        <p><strong>2. Gestionar plantillas de texto</strong></p>
        <ul>
        <li>En el diálogo de texto, a la izquierda ve una lista de todas las plantillas guardadas.</li>
        <li><strong>Guardar una plantilla:</strong> Introduzca su texto, déle formato y haga clic en "💾 Guardar como plantilla". Introduzca un nombre de archivo (sin extensión).</li>
        <li><strong>Cargar una plantilla:</strong> Haga clic en el nombre deseado de la lista. El texto y el formato se aplican y pueden ajustarse si es necesario.</li>
        <li><strong>Eliminar:</strong> Haga clic derecho sobre una plantilla para eliminarla o cambiar su estado privado/público.</li>
        </ul>

        <p><strong>3. Plantillas privadas (contraseña maestra)</strong></p>
        <ul>
        <li>Si ha configurado una contraseña maestra (en Configuración → Gestor de contraseñas), puede marcar plantillas como "privadas".</li>
        <li>Active la casilla "Plantilla privada" en el diálogo antes de guardar.</li>
        <li>Las plantillas privadas solo se muestran en la lista si ha introducido su contraseña maestra una vez por sesión (autenticación mediante el icono de candado o al primer acceso).</li>
        <li>Así protege plantillas confidenciales del acceso no autorizado.</li>
        </ul>

        <p><strong>4. Insertar cruces</strong></p>
        <ul>
        <li>A través del menú contextual también puede insertar una cruz gráfica (por ejemplo, para casillas de verificación).</li>
        <li>El tamaño, grosor de línea y color de las cruces pueden ajustarse globalmente en los ajustes (menú "Configuración" → "Ajustes de cruces").</li>
        <li>Haga clic derecho sobre una cruz existente para modificarla individualmente.</li>
        </ul>

        <p><strong>5. Acciones por lotes</strong></p>
        <ul>
        <li>Si ha colocado varios textos o cruces en una página, puede guardarlos o descartarlos todos juntos mediante el menú contextual (clic derecho en modo texto).</li>
        <li>Al guardar, todos los elementos se incrustan en el PDF y permanecen como gráficos vectoriales.</li>
        </ul>

        <p><strong>6. Atajos de teclado en modo texto</strong></p>
        <ul>
        <li>Teclas de flecha: mover elemento</li>
        <li>Ctrl+Flechas: pasos más grandes</li>
        <li>Intro: abrir diálogo de guardado (guardar todo / ajustar / descartar)</li>
        <li>Esc: descartar elemento actual</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Ajustes de cruces",
        'cross_properties': "Propiedades de la cruz",
        'cross_size': "Tamaño (px):",
        'cross_line_width': "Grosor de línea:",
        'cross_color': "Color:",
        'cross_choose_color': "Elegir",
        'cross_fine_tuning': "Ajuste fino al guardar (píxeles)",
        'cross_offset_x': "Desplazamiento X:",
        'cross_offset_y': "Desplazamiento Y:",
        'cross_offset_x_tooltip': "Valores negativos desplazan la cruz a la izquierda, positivos a la derecha",
        'cross_offset_y_tooltip': "Valores negativos desplazan la cruz hacia arriba, positivos hacia abajo",
        'cross_preview': "Vista previa",
        'cross_save': "Aplicar ajustes",
        'cross_customized': "Cruz personalizada",
        'cross_settings_applied': "Ajustes de cruz guardados.\nTamaño: {0}px, Grosor: {1}px\n{2}",
        'cross_updated_count': "{0} cruces existentes actualizadas.",
        'cross_no_crosses': "No se encontraron cruces existentes.",
        'cross_settings_applied_all': "Ajustes de cruz aplicados a todas las {0} cruces",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Ajustes de firmas",
        'signature_1': "Firma 1",
        'signature_2': "Firma 2",
        'signature_select': "Seleccionar firma",
        'signature_add': "➕ Añadir nueva firma...",
        'signature_size': "Tamaño para firma {0} (%):",
        'signature_common': "Ajustes generales",
        'signature_timestamp': "Añadir marca de tiempo automáticamente",
        'signature_location': "Lugar por defecto:",
        'signature_timestamp_size': "Tamaño de letra de marca de tiempo:",
        'signature_no_files': "-- No se encontraron firmas --",
        'signature_insert': "Insertar firma",
        'signature_insert_1': "Insertar firma 1",
        'signature_insert_2': "Insertar firma 2",
        'signature_customize': " Personalizar firma",
        'signature_discard': " Descartar esta firma",
        'signature_save_all': " Guardar todas las firmas",
        'signature_discard_all': " Descartar todas las firmas",
        'signature_guide_title': "Firmas - Guía",
        'signature_guide': """
📝 Firmas - Guía rápida

- Configurar contraseña maestra
- Configurar las firmas en el menú Ajustes
  (tamaño, marca de tiempo ...)
- Insertar con CLIC DERECHO en la posición deseada
  (requiere contraseña maestra una vez por sesión)
- Mover la firma con el ratón o teclas de flecha
- Se pueden insertar varias firmas sucesivamente
- Cada firma puede personalizarse individualmente
- Descartar una firma
- Guardar / descartar todas las firmas a la vez
- También se puede usar la barra de menú.
        """,
        'signature_placeholder': "No hay vista previa disponible",
        'signature_info': "Firma {0}: {1}×{2} px ({3}% de {4}×{5})",
        'signature_info_placeholder': "Ajustes para firma {0}",
        'signature_inserted': "Firma {0} insertada en página {1}",
        'signature_deleted': "Firma eliminada",
        'signature_copied': "Firma copiada",
        'signature_pasted': "Firma {0} pegada",
        'signature_saved': "{0} firmas se insertaron en el PDF.\n\nPDF recargado...",
        'signature_saved_voice': "{0} firmas guardadas",
        'mode_replace_signature_format': "Salir del modo e insertar firma {0}",
        'mode_conflict_voice_signature': "El modo {0} está activo. ¿Salir e insertar firma?",
        'signature_not_configured': "Firma {0} no configurada",
        'signature_file_not_found': "Archivo de firma no encontrado",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "No hay firma copiada disponible",
        'no_signatures_to_save': "No hay firmas para guardar",
        'signature_save_question': "¿Guardar todas las firmas, ajustar o descartar esta?",
        'signatures_saved_title': "Firmas guardadas",
        'signatures_saved': "{0} firmas se insertaron en el PDF.\n\nPDF recargado...",
        'signatures_saved_voice': "{0} firmas guardadas.",
        'all_signatures_discarded': "Todas las firmas descartadas",
        'signature_settings_saved': "Ajustes de firma guardados",
        'signature_cancelled': "Firma descartada",
        'signature_active_title': "Firma activa",
        'signature_replace_question': "Ya hay una firma activa.\n\n¿Desea reemplazar la firma actual?",
        'signature_replace': "Reemplazar firma",
        'signature_replace_voice': "¿Reemplazar firma actual o cancelar?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Ajustes de imagen",
        'image_common': "Ajustes generales de imagen",
        'image_keep_aspect': "Mantener proporción al arrastrar",
        'image_default_size': "Tamaño por defecto (%):",
        'image_dark_invert': "Invertir imágenes en modo oscuro",
        'image_dark_invert_tooltip': "Activado: las imágenes se invierten para mejor visibilidad",
        'image_fine_tuning': "Ajuste fino (píxeles)",
        'image_offset_x': "Desplazamiento X:",
        'image_offset_y': "Desplazamiento Y:",
        'image_offset_x_tooltip': "Valores negativos desplazan la imagen a la izquierda, positivos a la derecha",
        'image_offset_y_tooltip': "Valores negativos desplazan la imagen hacia arriba, positivos hacia abajo",
        'image_select': "Seleccionar imagen",
        'image_insert': "Insertar imagen",
        'image_customize': " Personalizar imagen",
        'image_aspect': " Mantener proporción",
        'image_discard': " Descartar esta imagen",
        'image_save_all': " Guardar todas las imágenes",
        'image_discard_all': " Descartar todas las imágenes",
        'image_filter': "Imágenes",
        'image_guide_title': "Insertar imagen - Guía",
        'image_guide': """
📷 Insertar imagen en PDF - Guía rápida:

1. Clic derecho en la posición deseada
2. "Insertar imagen" → seleccionar imagen
3. Posicionar imagen: arrastrar con el ratón
4. Ajustar tamaño: arrastrar esquinas/bordes
5. Mantener proporción: tecla [A]
6. Más ajustes: clic derecho en la imagen

Consejo: puede ajustar la configuración en el menú contextual.
        """,
        'image_inserted': "Imagen {0} insertada en página {1}",
        'image_deleted': "Imagen descartada",
        'image_copied': "Imagen copiada",
        'image_pasted': "Imagen pegada",
        'image_saved': "{0} imágenes se insertaron en el PDF.\n\nPDF recargado...",
        'image_saved_voice': "{0} imágenes guardadas",
        'image_aspect_on': "activado",
        'image_aspect_off': "desactivado",
        'image_aspect_toggle': "Mantener proporción {0}",
        'image_reset': "Imagen restaurada a tamaño original",
        'image_replaced': "Imagen reemplazada",
        'image_invalid': "Imagen no válida",
        'mode_replace_image': "Insertar imagen",
        'mode_conflict_voice_image': "El modo {0} está activo. ¿Salir e insertar imagen?",
        'image_active_title': "Imagen activa",
        'image_replace_question': "Ya hay una imagen activa.\n\n¿Desea reemplazar la imagen actual?",
        'image_replace': "Reemplazar imagen",
        'image_replace_voice': "¿Reemplazar imagen actual o cancelar?",
        'image_filter_all': "Imágenes (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Todos los archivos (*.*)",
        'no_copied_image': "No hay imagen copiada disponible",
        'image_discarded': "Imagen descartada",
        'image_save_question': "¿Guardar todas las imágenes, ajustar o descartar esta?",
        'no_images_to_save': "No hay imágenes para guardar",
        'no_valid_images': "No hay imágenes válidas para guardar",
        'images_saved_title': "Imágenes guardadas",
        'images_saved': "{0} imágenes se insertaron en el PDF.\n\nPDF recargado...",
        'images_saved_voice': "{0} imágenes guardadas.",
        'all_images_discarded': "Todas las imágenes descartadas",
        'image_settings_updated': "Ajustes de imagen actualizados",
        'image_replace_title': "Seleccionar nueva imagen",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Ajustes de formas",
        'form_basic': "Ajustes básicos",
        'form_default_type': "Tipo de forma por defecto:",
        'form_rectangle': "Rectángulo",
        'form_ellipse': "Elipse",
        'form_line': "Línea",
        'form_arrow': "Flecha",
        'form_line_width': "Grosor de línea:",
        'form_colors': "Colores",
        'form_line_color': "Color de línea:",
        'form_fill_color': "Color de relleno:",
        'form_choose_color': "Elegir",
        'form_transparent': "Fondo transparente (solo línea)",
        'form_filled': "relleno",
        'form_dark_mode': "Modo oscuro",
        'form_dark_invert': "Invertir colores en modo oscuro",
        'form_fine_tuning': "Ajuste fino (píxeles)",
        'form_offset_x': "Desplazamiento X:",
        'form_offset_y': "Desplazamiento Y:",
        'form_offset_x_tooltip': "Valores negativos desplazan la forma a la izquierda, positivos a la derecha",
        'form_offset_y_tooltip': "Valores negativos desplazan la forma hacia arriba, positivos hacia abajo",
        'form_preview': "Vista previa",
        'form_insert': "Insertar forma",
        'form_rectangle_insert': "Rectángulo",
        'form_ellipse_insert': "Elipse/Círculo",
        'form_line_insert': "Línea (2 clics)",
        'form_arrow_insert': "Flecha (2 clics)",
        'form_customize': " Personalizar forma",
        'form_transparent_toggle': " Fondo transparente",
        'form_discard': " Descartar esta forma",
        'form_save_all': " Guardar todas las formas",
        'form_discard_all': " Descartar todas las formas",
        'form_guide_title': "Insertar forma - Guía",
        'form_guide': """
📐 Insertar forma en PDF - Guía rápida:

1. Elegir tipo de forma (rectángulo, elipse, línea, flecha)
2. Clic en la posición deseada
   - Para rectángulo/elipse: un clic coloca la forma
   - Para línea/flecha: dos clics para inicio y fin
3. Posicionar forma: arrastrar con el ratón
4. Ajustar tamaño: arrastrar esquinas/bordes
5. Guardar forma: Intro
6. Descartar forma: Esc
7. Más ajustes: clic derecho en la forma

Consejo: puede ajustar la configuración en el menú contextual.
        """,
        'form_inserted': "{0} insertada en página {1}",
        'form_deleted': "Forma eliminada",
        'form_copied': "Forma copiada",
        'form_pasted': "Forma pegada",
        'form_saved': "{0} formas se insertaron en el PDF.\n\nPDF recargado...",
        'form_saved_voice': "{0} formas guardadas",
        'form_reset': "Forma restaurada a tamaño por defecto",
        'form_transparent_on': "activado",
        'form_transparent_off': "desactivado",
        'form_transparent_toggled': "Fondo transparente {0}",
        'form_line_cancel': "Dibujo de línea cancelado",
        'form_second_click': "Ahora haga clic en el punto final para {0}",
        'mode_replace_form': "Insertar forma",
        'mode_conflict_voice_form': "El modo {0} está activo. ¿Salir e insertar una forma?",
        'form_settings_updated': "Ajustes de forma actualizados",
        'form_unknown': "Forma",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Haga clic en la posición de inicio",
        'form_line_guide_2': "2. Haga clic en la posición final",
        'form_line_guide_3': "La línea se dibujará entre ambos puntos.",
        'form_line_status_1': "Esperando primer clic...",
        'form_line_status_2': "Primer punto definido: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Ahora haga clic en el punto final...",
        'form_line_status_4': "Ambos puntos definidos.\nHaga clic en 'Finalizar' para guardar.",
        'form_line_reset': "Reiniciar",
        'form_line_finish': "Finalizar",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Copiar (Cmd+C)",
        'paste': "Pegar (Cmd+V)",
        'copied': "Copiado: {0}",
        'no_element_to_copy': "No hay elemento seleccionado para copiar",
        'no_copied_data': "No hay datos copiados disponibles",
        'no_valid_position': "No hay posición válida para pegar",
        'copy_text': "Texto copiado",
        'copy_image': "Imagen copiada",
        'copy_form': "Forma copiada",
        'copy_signature': "Firma copiada",
        'element_text': "texto",
        'element_image': "imagen",
        'element_form': "forma",
        'element_signature': "firma",
        'element_unknown': "elemento",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Conflicto de modo",
        'mode_conflict_message': "El modo '{0}' ya está activo.\n\n¿Desea salir de él y {1}?",
        'mode_replace': "Salir del modo y {0}",
        'mode_cancel': "Cancelar",
        'mode_replace_text': "insertar texto",
        'mode_replace_cross': "insertar cruz",
        'mode_replace_signature': "insertar firma",
        'mode_replace_image': "insertar imagen",
        'mode_replace_form': "insertar forma",
        'mode_conflict_voice': "El modo {0} está activo. ¿Salir e insertar texto?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Entrada de texto",
        'active_mode_signature': "Firma",
        'active_mode_image': "Imagen",
        'active_mode_form': "Forma",
        'active_mode_and': " y ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Insertar",                    # Hauptmenü
        'insert_another_text': "Insertar texto",          # Vereinfacht
        'insert_another_cross': "Insertar cruz",        # Vereinfacht
        'insert_another_signature_1': "Firma 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Firma 2",      # Untermenü-Eintrag
        'insert_another_image': "Insertar imagen",         # Vereinfacht
        'insert_another_form_rect': "Rectángulo",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Elipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Línea (2 clics)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Flecha (2 clics)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Guardar {0}",
        'save_dialog_message': "{0} se guardará en la página {1}.\n\n¿Cómo desea proceder?",
        'save_all': "Guardar todos los {0}",
        'save_single': "Guardar {0}",
        'save_customize': "Personalizar {0}",
        'save_discard': "Descartar {0}",
        'save_continue': "Seguir editando",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Ir a la página {0}",
        'context_rotate': " Rotar página {0}",
        'context_delete': " Eliminar página {0}",
        'context_export': " Exportar página {0}",
        'context_mark_as': " Marcar página como...",
        'context_mark_empty': " Página vacía",
        'context_unmark_empty': " Ya no vacía",
        'context_mark_export': " Marcar para exportar",
        'context_unmark_export': " No exportar",
        'context_batch_actions': " Acciones por lote",
        'context_batch_delete_empty': " Eliminar las {0} páginas vacías",
        'context_batch_export_single': " Todas las {0} páginas (un archivo)",
        'context_batch_export_split': " Todas las {0} páginas (separadas)",
        'context_drag_start': " Activar arrastrar y soltar",
        'context_drag_stop': " Desactivar arrastrar y soltar",
        'context_insert': " Insertar",
        'context_insert_pages': " Insertar páginas",
        'context_zoom': "Zoom",
        'discard_mixed': "Descartar {0} {1} y {2} {3}",
        'save_mixed': "Guardar {0} {1} y {2} {3}",
        'discard_texts': "Descartar {0} textos",
        'discard_text_single': "Descartar 1 texto",
        'save_texts': "Guardar {0} textos",
        'save_text_single': "Guardar 1 texto",
        'discard_crosses': "Descartar {0} cruces",
        'discard_cross_single': "Descartar 1 cruz",
        'save_crosses': "Guardar {0} cruces",
        'save_cross_single': "Guardar 1 cruz",
        'discard_signatures': "Descartar {0} firmas",
        'save_signature_single': "Guardar 1 firma",
        'save_signatures': "Guardar {0} firmas",
        'discard_images': "Descartar {0} imágenes",
        'save_image_single': "Guardar 1 imagen",
        'save_images': "Guardar {0} imágenes",
        'discard_forms': "Descartar {0} formas",
        'save_form_single': "Guardar 1 forma",
        'save_forms': "Guardar {0} formas",
        'cross_discard': "Descartar esta cruz",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Información de Exportación / Importación",
        'export_what': "📋 ¿Qué se exporta?",
        'export_general': "Ajustes generales",
        'export_general_items': "• Síntesis de voz (activada/desactivada, velocidad)\n• Modo oscuro/claro\n• Ajustes de copia de seguridad\n• Ajustes de OCR",
        'export_image_form': "Ajustes de imagen y forma",
        'export_image_form_items': "• Ajustes de imagen (proporción, tamaño por defecto)\n• Ajustes de forma (grosor de línea, colores)\n• Ajustes de firma (rutas, tamaños, marca de tiempo)",
        'export_passwords': "Base de datos de contraseñas",
        'export_passwords_items': "• Todas las contraseñas de PDF guardadas\n• Opcionalmente cifradas o descifradas",
        'export_master': "Ajustes de contraseña maestra",
        'export_master_items': "• Hash de contraseña maestra\n• Ajustes para firmas/plantillas de texto",
        'export_signatures': "Firmas y plantillas de texto",
        'export_signatures_items': "• Todos los archivos de imagen (firmas)\n• Todas las plantillas de texto con formato\n• Marcas privado/público",
        'export_import_warning': "⚠️ Notas importantes",
        'export_import_note': "• Al importar, TODOS los ajustes actuales se sobrescriben\n• Es necesario reiniciar la aplicación\n• Las firmas/plantillas existentes se reemplazarán",
        'export_master_note': "• Si hay una contraseña maestra configurada, puede elegir:\n  - Descifrado (contraseñas en texto claro)\n  - Cifrado (solo legible con contraseña maestra)",
        'export_security': "• El archivo ZIP exportado contiene datos confidenciales\n• Guárdelo en un lugar seguro (p. ej., memoria USB cifrada)\n• Si pierde el archivo, las contraseñas se pierden irreversiblemente",
        'export_format': "📁 Formato de exportación",
        'export_format_desc': "Los ajustes se guardan en un único archivo ZIP:",
        'export_filename': "PDFDarkView_Settings_AAAAMMDD_HHMMSS.zip",
        'export_success': "Ajustes exportados con éxito",
        'export_failed': "Error al exportar",
        'export_import_question': "¿Desea reiniciar la aplicación ahora?",
        'export_password_question': "Hay una contraseña maestra configurada.\n\n¿Desea exportar las contraseñas descifradas?\n(de lo contrario se exportarán cifradas)",
        'export_decrypt': "Exportar descifradas",
        'export_encrypt': "Exportar cifradas",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Información",
        'info_title': "Acerca de PDF Dark View",
        'info_version': "Versión",
        'info_author': "Desarrollado por Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Acerca de",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> es un visor de PDF accesible, desarrollado especialmente para personas con discapacidad visual.</p>

            <p><strong>Características principales:</strong></p>
            <ul>
                <li>Interfaz de alto contraste y personalizable</li>
                <li>Control total mediante teclado</li>
                <li>Locución integrada</li>
                <li>OCR para documentos escaneados</li>
                <li>Amplias herramientas de edición</li>
            </ul>

            <p>Se admiten más de 50 idiomas, para que los PDF sean accesibles para todos.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funciones",
        'info_features_intro': "PDF Dark View le ofrece las siguientes posibilidades:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Visualización y navegación</strong> – Modo oscuro/claro, pasar páginas, zoom, ir a página</li>
            <li><strong>OCR (reconocimiento de texto)</strong> – Haga que los documentos escaneados sean buscables y copiables</li>
            <li><strong>Edición</strong> – Inserte texto, cruces, firmas, imágenes y formas</li>
            <li><strong>Gestión de páginas</strong> – Eliminar, extraer, insertar, mover mediante arrastrar y soltar</li>
            <li><strong>Exportación</strong> – A Word, Pages o como texto</li>
            <li><strong>Seguridad</strong> – Protección y gestión con contraseña</li>
            <li><strong>Accesibilidad</strong> – Locución, control por teclado, alto contraste</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Operación",
        'info_accessibility': "♿ Accesibilidad – control total mediante teclado",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 General</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Abrir PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Buscar</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Cambiar modo oscuro/claro</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Imprimir</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Salir</div>

        <div class="shortcut-cat">📖 Navegación</div>
        <div class="shortcut-row"><kbd>Teclas de flecha</kbd> Hojear página por página</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Ir a página</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Primera página</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Última página</div>

        <div class="shortcut-cat">✏️ Edición</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Insertar texto</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Eliminar páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extraer páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Insertar páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Mover páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rotar página</div>

        <div class="shortcut-cat">🖼️ Mover elementos</div>
        <div class="shortcut-row"><kbd>Teclas de flecha</kbd> Mover texto/imagen/firma</div>
        <div class="shortcut-row"><kbd>Ctrl+Teclas de flecha</kbd> Pasos más grandes</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Guardar</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Descartar</div>

        <div class="shortcut-cat">🗣️ Locución</div>
        <div class="shortcut-row"><kbd>F2</kbd> Activar/desactivar locución</div>
        """,
        'info_contextmenu': "📌 Importante: ¡Todas las funciones también están disponibles a través del menú contextual (botón derecho del ratón)!",
        'info_accessibility_hint': "💡 Consejo: La locución (F2) facilita la orientación y proporciona retroalimentación sobre menús y diálogos.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licencia & Aviso legal",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 AVISO LEGAL</strong><br>
        Información según § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Alemania<br>
        Correo electrónico: binhdiez64@gmail.com<br>
        Responsable del contenido: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Exención de responsabilidad</strong><br>
        El software ha sido desarrollado con el máximo cuidado. No se asume ninguna garantía por la exactitud, integridad y funcionalidad. El uso es bajo su propia responsabilidad.<br><br>

        <strong>📄 Licencia MIT (uso privado)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permitido: uso gratuito, modificaciones privadas, copias personales.<br>
        No permitido: venta, uso comercial, eliminación de avisos de derechos de autor.<br><br>

        <strong>🔧 Componentes de terceros</strong><br>
        Este software contiene componentes bajo licencias GPL, AGPL, Apache 2.0, BSD y MIT.<br>
        Al redistribuir, se deben cumplir los respectivos términos de la licencia.<br><br>

        <strong>🌐 Código abierto</strong><br>
        El código fuente está disponible y puede ser consultado, modificado y redistribuido de acuerdo con los respectivos términos de la licencia.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Agradecimientos",
        'info_credits': "Agradecimiento a la comunidad de código abierto",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Procesamiento de PDF</li>
            <li><strong>PyQt5</strong> – Interfaz gráfica</li>
            <li><strong>Tesseract OCR</strong> – Reconocimiento de texto</li>
            <li><strong>OCRmyPDF</strong> – Integración de OCR</li>
            <li><strong>python-docx</strong> – Exportación a Word</li>
            <li><strong>qtawesome</strong> – Iconos</li>
            <li><strong>DeepSeek</strong> – Apoyo con traducciones (50+ idiomas)</li>
            <li><strong>Todos los usuarios</strong> – Por sus valiosos comentarios</li>
            <li><strong>La comunidad de código abierto</strong> – Por las excelentes bibliotecas</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Idiomas",
        'info_languages_header': "🌍 Soporte de idiomas",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View actualmente admite <strong>62 idiomas</strong> – para que el software pueda utilizarse de forma accesible en todo el mundo.</p>

            <p><strong>📖 Lista completa de idiomas (Estado: marzo de 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikáans</li>
                    <li>🇦🇱 Albanés (Shqip)</li>
                    <li>🇩🇿 Árabe (العربية)</li>
                    <li>🇮🇩 Balinés (Basa Bali)</li>
                    <li>🇧🇩 Bengalí (বাংলা)</li>
                    <li>🇲🇲 Birmano (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnio (Bosanski)</li>
                    <li>🇧🇬 Búlgaro (Български)</li>
                    <li>🇨🇳 Chino (中文)</li>
                    <li>🇩🇰 Danés (Dansk)</li>
                    <li>🇩🇪 Alemán (Deutsch)</li>
                    <li>🇬🇧 Inglés (English)</li>
                    <li>🇪🇪 Estonio (Eesti)</li>
                    <li>🇫🇮 Finés (Suomi)</li>
                    <li>🇫🇷 Francés (Français)</li>
                    <li>🇬🇷 Griego (Ελληνικά)</li>
                    <li>🇮🇱 Hebreo (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croata (Hrvatski)</li>
                    <li>🇭🇺 Húngaro (Magyar)</li>
                    <li>🇮🇩 Indonesio (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandés (Gaeilge)</li>
                    <li>🇮🇸 Islandés (Íslenska)</li>
                    <li>🇮🇹 Italiano (Italiano)</li>
                    <li>🇯🇵 Japonés (日本語)</li>
                    <li>🇰🇭 Jemer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Coreano (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Letón (Latviešu)</li>
                    <li>🇱🇹 Lituano (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgués (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malayo (Bahasa Melayu)</li>
                    <li>🇮🇳 Maratí (मराठी)</li>
                    <li>🇲🇳 Mongol (Монгол)</li>
                    <li>🇳🇵 Nepalí (नेपाली)</li>
                    <li>🇳🇱 Neerlandés (Nederlands)</li>
                    <li>🇳🇴 Noruego (Norsk)</li>
                    <li>🇦🇫 Pastún (پښتو)</li>
                    <li>🇮🇷 Persa (فارسی)</li>
                    <li>🇵🇱 Polaco (Polski)</li>
                    <li>🇵🇹 Portugués (Português)</li>
                    <li>🇮🇳 Panyabí (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumano (Română)</li>
                    <li>🇷🇺 Ruso (Русский)</li>
                    <li>🇸🇪 Sueco (Svenska)</li>
                    <li>🇷🇸 Serbio (Српски)</li>
                    <li>🇸🇰 Eslovaco (Slovenčina)</li>
                    <li>🇸🇮 Esloveno (Slovenščina)</li>
                    <li>🇪🇸 Español (Español)</li>
                    <li>🇹🇿 Suajili (Kiswahili)</li>
                    <li>🇵🇭 Tagalo (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Tailandés (ไทย)</li>
                    <li>🇨🇿 Checo (Čeština)</li>
                    <li>🇹🇷 Turco (Türkçe)</li>
                    <li>🇺🇦 Ucraniano (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamita (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yidis (ייִדיש)</li>
                    <li>🇿🇦 Zulú (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Añadir tus propios idiomas:</strong><br>
                ¿Quieres un idioma que aún no está incluido? Simplemente coloca tu propio archivo de diccionario (<code>sprache_xx.py</code>) junto a la aplicación – el software lo reconocerá automáticamente. Si estás interesado en una traducción específica, no dudes en contactarme.
            </div>

            <p><strong>🙏 Agradecimiento especial:</strong> DeepSeek por el apoyo en la traducción de todos los diccionarios a 62 idiomas.</p>

            <p>📧 Contacto para traducciones: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Error",
        'error_occurred': "Ha ocurrido un error",
        'error_pdf_load': "Error al cargar el PDF",
        'error_pdf_save': "Error al guardar el PDF",
        'error_ocr': "Error en el reconocimiento de texto",
        'error_no_pdf': "No hay ningún PDF cargado",
        'error_page_not_found': "Página no encontrada",
        'error_invalid_range': "Rango de páginas inválido",
        'error_file_not_found': "Archivo no encontrado",
        'error_permission': "Permiso denegado",
        'error_unknown': "Error desconocido",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Éxito",
        'success_operation': "Operación completada con éxito",
        'success_saved': "Guardado con éxito",
        'success_exported': "Exportado con éxito",
        'success_imported': "Importado con éxito",
        'success_deleted': "Eliminado con éxito",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Confirmación",
        'confirm_yes': "Sí",
        'confirm_no': "No",
        'confirm_ok': "Aceptar",
        'confirm_cancel': "Cancelar",
        'confirm_delete': "Eliminar",
        'confirm_overwrite': "Sobrescribir",
        'confirm_continue': "Continuar",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Cargando PDF...",
        'progress_saving': "Guardando PDF...",
        'progress_exporting': "Exportando PDF...",
        'progress_processing': "Procesando...",
        'progress_wait': "Por favor, espere...",
        'progress_preparing': "Preparando...",
        'progress_finalizing': "Finalizando...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Blanco",
        'color_black': "Negro",
        'color_red': "Rojo",
        'color_green': "Verde",
        'color_blue': "Azul",
        'color_yellow': "Amarillo",
        'color_magenta': "Magenta",
        'color_cyan': "Cian",
        'color_orange': "Naranja",
        'color_gray': "Gris",
        'color_custom': "Selector de color",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Archivo",
        'menu_edit': "&Edición",
        'menu_view': "&Vista",
        'menu_tools': "&Herramientas",
        'menu_settings': "&Configuración",
        'menu_help': "&Ayuda",
        'menu_language': "🌐 Idioma",
        'menu_guides': "&Guías",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Abrir",
        'file_save_as': "&Guardar como...",
        'file_protect': "&Proteger documento...",
        'file_export': "&Exportar",
        'file_export_pages': "Exportar a Pages",
        'file_export_word': "Exportar a DOCX",
        'file_export_text': "Exportar a TXT",
        'file_print_now': "&Imprimir ahora",
        'file_print': "&Imprimir",
        'file_close': "&Cerrar",
        'file_quit': "&Salir",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Buscar",
        'edit_ocr': " Ejecutar OCR",
        'edit_rotate': "&Rotar página",
        'edit_rotate_all': "&Rotar todas las páginas",
        'edit_delete_pages': "&Eliminar páginas",
        'edit_extract_pages': "&Extraer páginas",
        'edit_insert_pages': "&Insertar páginas",
        'edit_move_pages': "&Mover páginas",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Insertar texto y cruces",
        'text_insert': " Insertar texto",
        'cross_insert': " Insertar cruz",
        'text_customize': " Personalizar texto",
        'cross_customize': " Personalizar esta cruz",
        'cross_customize_all': " Personalizar todas las cruces",
        'text_discard': " Descartar este texto / esta cruz",
        'text_discard_all': " Descartar todos los textos y cruces",
        'text_save_all': " Guardar todos los textos y cruces",
        'text_guide': " Entrada de texto / plantillas - Guía",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Insertar firma",
        'signature_settings_menu': " Ajustes...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Insertar imagen",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Insertar formas",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Mostrar ventana de texto",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Ancho de página (por defecto)",
        'view_zoom_two': "&Dos páginas",
        'view_zoom_overview': "&Vista general (varias páginas)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Accesibilidad",
        'settings_voice': "Síntesis de voz",
        'settings_voice_tooltip': "complementa la síntesis de voz de los lectores de pantalla con información adicional",
        'settings_signature': "&Ajustes de firma",
        'settings_password': "&Gestor de contraseñas",
        'settings_backup': "Crear copia de seguridad antes de cambios",
        'settings_export_import': "&Exportar / importar ajustes",
        'settings_export': "&Exportar todos los ajustes...",
        'settings_import': "&Importar todos los ajustes...",
        'settings_export_info': "&¿Qué se exporta?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "activada",
        'voice_off': "desactivada",
        'voice_toggle': "Síntesis de voz {0}",
        'voice_speed': "Velocidad al {0} por ciento",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Herramienta no encontrada:\n{0}\n\nBASE_DIR: {1}\nAsegúrese de que las herramientas PDF están instaladas en el directorio {1}.",
        'tool_started': "{0} iniciado",
        'tool_start_failed': "No se pudo iniciar",
        'process_error_failed_to_start': "No se pudo iniciar el proceso. ¿Existe el archivo?",
        'process_error_crashed': "El proceso se bloqueó durante el inicio.",
        'process_error_timeout': "Tiempo de espera del proceso agotado.",
        'process_error_write': "Error de escritura en el proceso.",
        'process_error_read': "Error de lectura del proceso.",
        'process_error_unknown': "Error de proceso desconocido",
        'process_command': "Comando",
        'process_normal_exit': "terminado normalmente",
        'process_crashed': "bloqueado",
        'process_nonzero_exit': "{0} terminó con código de error {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Cancelando...",
        'move_cancelling': "Cancelando movimiento",
        'opening_pdf': "Abriendo PDF...",
        'loading_document': "Cargando documento...",
        'pdf_opened': "PDF abierto",
        'pages_found_moving': "{0} páginas encontradas, {1} a mover",
        'creating_backup': "Creando copia de seguridad...",
        'backup_description': "Respaldando archivo original...",
        'backup_saved_as': "Respaldado como: {0}",
        'error_format': "Error: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Búsqueda reiniciada",
        'page_header_simple': "=== Página {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Gestor de contraseñas – Guía",
        'password_guide_voice': "Guía de gestión de contraseñas. Por favor, lea las notas.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Gestor de contraseñas – Guía detallada</strong></p>

        <p><strong>1. Protección con contraseña para PDF</strong></p>
        <ul>
        <li>Al abrir un PDF protegido por contraseña, aparece un diálogo donde puede introducir la contraseña.</li>
        <li>Puede guardar la contraseña cifrada para no tener que volver a introducirla cada vez (casilla "Guardar contraseña").</li>
        <li>Con el botón "Quitar contraseña" puede crear una copia descifrada del PDF y eliminar la contraseña de la base de datos.</li>
        </ul>

        <p><strong>2. Contraseña maestra</strong></p>
        <ul>
        <li>La contraseña maestra protege el acceso a todas las contraseñas de PDF guardadas.</li>
        <li><strong>Configuración:</strong> Vaya a "Configuración → Gestor de contraseñas → Ajustes contraseña maestra" y haga clic en "Configurar contraseña maestra". Elija una contraseña segura (al menos 8 caracteres).</li>
        <li><strong>Cambio:</strong> Tras autenticarse correctamente, puede cambiar la contraseña maestra.</li>
        <li><strong>Eliminación:</strong> Si elimina la contraseña maestra, se borrarán TODAS las contraseñas guardadas de forma irreversible. Puede exportar una copia de seguridad antes.</li>
        <li>Una vez por sesión debe autenticarse con la contraseña maestra para acceder a funciones protegidas (por ejemplo, ver contraseñas).</li>
        </ul>

        <p><strong>3. Gestor de contraseñas (lista)</strong></p>
        <ul>
        <li>En "Configuración → Gestor de contraseñas" se abre una tabla con todos los PDF guardados y sus contraseñas cifradas.</li>
        <li><strong>Sin contraseña maestra:</strong> Solo puede eliminar entradas – las contraseñas permanecen ocultas.</li>
        <li><strong>Con contraseña maestra (autenticado):</strong> Puede ver, copiar, exportar y eliminar contraseñas.</li>
        <li><strong>Exportación:</strong> Elija un formato (JSON, CSV, TXT) y guarde la lista. Si hay contraseña maestra, puede decidir si las contraseñas se exportan en texto claro o todavía cifradas.</li>
        <li><strong>Importación:</strong> Un archivo ZIP exportado previamente con todos los ajustes (incluidas contraseñas) puede reimportarse mediante "Configuración → Exportar/importar ajustes". Atención: ¡los datos existentes se sobrescribirán!</li>
        </ul>

        <p><strong>4. Generador de contraseñas</strong></p>
        <ul>
        <li>En el diálogo de contraseña (por ejemplo, al proteger un PDF) encontrará un botón de dado 🎲 a la derecha del campo de entrada.</li>
        <li>Haga clic en él para abrir el generador de contraseñas. Puede ajustar la longitud, los conjuntos de caracteres (mayúsculas, minúsculas, dígitos, símbolos) y un separador para mejorar la legibilidad.</li>
        <li>La contraseña generada puede adoptarse directamente y copiarse si es necesario.</li>
        </ul>

        <p><strong>5. Notas de seguridad importantes</strong></p>
        <ul>
        <li>Las contraseñas guardadas se almacenan cifradas con AES-256. La clave se deriva de su contraseña maestra (si está configurada) o de un valor fijo (sin contraseña maestra).</li>
        <li>Sin contraseña maestra, las contraseñas están cifradas, pero la clave está incrustada en el programa – un atacante con acceso a sus archivos podría descifrarlas. Por lo tanto, recomendamos encarecidamente usar una contraseña maestra.</li>
        <li>La base de datos de contraseñas se encuentra en el directorio `Data/passwords.json`. Haga copias de seguridad periódicas, especialmente antes de eliminar la contraseña maestra.</li>
        <li>Si pierde la contraseña maestra, todas las contraseñas guardadas se perderán irreversiblemente.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Modo de inversión",
        'invert_mode_classic': "Clásico (invertir todos los colores)",
        'invert_mode_smart': "Inteligente (invertir solo el brillo)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Umbral de escala de grises",
        'gray_threshold_10': "10% (estricto)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Estándar)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (suave)",
        'threshold_changed': "Umbral establecido en {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Umbral de escala de grises – Explicación",
        'threshold_guide_text': "El umbral de escala de grises determina qué píxeles en el modo oscuro inteligente se consideran 'grises' y se invierten.\n\n"
                                "• Un valor bajo (10%) invierte solo tonos de gris casi perfectos – los elementos de color permanecen completamente conservados.\n"
                                "• Un valor alto (50%) también invierte píxeles ligeramente coloreados – esto aumenta el contraste, pero puede distorsionar los colores.\n\n"
                                "El valor óptimo depende del documento. Para documentos de texto puro, 30–40% es a menudo ideal, para gráficos en color más bien 10–20%.\n\n"
                                "Puede ajustar el valor en cualquier momento a través del menú 'Configuración' – el PDF se recargará inmediatamente.\n\n"
                                "Nota:\n* ¡Las fotos e imágenes solo se pueden mostrar correctamente en modo claro!\n* La configuración de inversión solo se muestra cuando el modo oscuro está activado.",
        'threshold_guide_voice': "El umbral de escala de grises determina cuánto interviene el modo oscuro inteligente. Un valor bajo preserva los colores, un valor alto aumenta el contraste.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Abriendo PDF...",
        'progress_loading_document': "Cargando documento...",
        'progress_pdf_opened': "PDF abierto",
        'progress_creating_backup': "Creando copia de seguridad...",
        'progress_backup_description': "Asegurando archivo original...",
        'progress_backup_created': "Copia de seguridad creada",
        'progress_backup_saved_as': "Guardado como: {0}",
        'progress_analyzing_start': "Iniciando análisis...",
        'progress_searching_empty': "Buscando páginas vacías...",
        'progress_page_empty': "La página {0} está vacía",
        'progress_page_keep': "Mantener página {0}",
        'progress_analysis_complete': "Análisis completado",
        'progress_empty_found': "Se encontraron {0} páginas vacías",
        'progress_current_page': "Página actual",
        'progress_mark_delete': "Marcada para eliminar",
        'progress_range_selected': "Rango de páginas {0}-{1}",
        'progress_deleting_pages': "Eliminando {0} páginas",
        'progress_creating_new_pdf': "Creando nuevo PDF...",
        'progress_transferring_pages': "Transfiriendo páginas",
        'progress_keeping_page': "La página {0} se mantendrá ({1}/{2})",
        'progress_saving_pdf': "Guardando PDF...",
        'progress_optimizing': "Optimizando tamaño del archivo...",
        'progress_finalizing': "Finalizando...",
        'progress_new_size': "Nuevo tamaño: {0:.2f} MB",
        'progress_cancelling': "Cancelando...",
        'progress_cancel_message': "Cancelando {0}",
        'progress_pages_found_moving': "Se encontraron {0} páginas, {1} para mover",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analizando PDF...",
        'ocr_status_optimizing': "Optimización de imagen en curso...",
        'ocr_status_recognizing': "Reconocimiento de texto en curso...",
        'ocr_status_embedding': "Incrustando texto...",
        'ocr_status_finalizing': "Finalizando PDF...",

        # PDF-Laden
        'progress_preparing': "Preparando...",
        'progress_loading': "Cargando PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Eliminando páginas...",
        'progress_moving_title': "Moviendo páginas...",
        'pages_found': "Páginas encontradas",
        'progress_creating_new_order': "Creando nuevo orden...",
        'progress_sorting_pages': "Ordenando páginas...",
        'progress_moving_to_begin': "Moviendo {0} páginas al principio",
        'progress_transferring_count': "Transfiriendo {0} páginas",
        'progress_transferring_before_target': "Transfiriendo páginas antes del destino",
        'progress_moving_pages': "Moviendo {0} páginas",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_copia_seguridad_",
        'filename_protected_suffix': "_protegido_",
        'filename_copy_suffix': "_Copia",
        'filename_page_single': "_Pagina_",
        'filename_page_range': "_Paginas_",
        'filename_export_page': "_Pagina_{0:03}",
        'filename_export_range': "_Paginas_{0}-{1}",
        'filename_export_multiple': "_Paginas_{0}",
        'filename_with_text': "_con_Texto",
        'filename_with_signature': "_con_Firma",
        'filename_with_image': "_con_Imagen",
        'filename_with_forms': "_con_Formas",
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
        'view_toggle_navbar': "Mostrar barra de botones",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "No se pueden eliminar todas las páginas",
		'pages_cannot_delete_last_page': '¡La última página no se puede eliminar!',
		'pages_cannot_delete_all_pages': '¡Debe quedar al menos una página en el documento!',
		'delete_pages_confirm': '¿Está seguro de que desea eliminar {0} páginas?',
		'delete_pages_confirm_voice': '¿Está seguro de que desea eliminar {0} páginas?',
		'pages_deleted': '{0} páginas se eliminaron correctamente.',
		'warning': 'Advertencia',
		'error': 'Error',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Ningún formulario seleccionado",
        'form_customized': "Formulario personalizado",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Seleccionar",
        'btn_use': "Usar",
        'master_password_for_spasswords': "Para guardar y usar contraseñas, primero debe configurar una contraseña maestra.\n\n¿Desea configurar la contraseña maestra ahora?",
        'open_saved_dialog_title': "Abrir archivo guardado",
        'open_saved_question': "¿Desea abrir el archivo guardado ahora?",
        'password': "Contraseña",
        'password_manager_master_required': "El administrador de contraseñas solo está disponible si se ha configurado una contraseña maestra.\n\n¿Desea configurar la contraseña maestra ahora?",
        'password_master_required_for_select': "Para ver y seleccionar contraseñas guardadas, primero debe autenticarse con su contraseña maestra.\n\n¿Desea autenticarse ahora?",
        'password_not_available': "La contraseña seleccionada no está disponible o no se pudo descifrar.",
        'password_options_title': "Opciones de contraseña",
        'password_save_choice_change': "Establecer nueva contraseña",
        'password_save_choice_keep': "Usar contraseña existente",
        'password_save_choice_none': "Guardar sin cifrar",
        'password_save_hint': "Primero configure una contraseña maestra para guardar contraseñas de forma segura.",
        'password_save_master_required': "Guardar contraseña (solo posible con contraseña maestra)",
        'password_save_question': "El PDF actual está protegido con contraseña. ¿Desea usar la contraseña existente, establecer una nueva o guardar sin cifrar?",
        'password_select': "Seleccionar contraseña",
        'password_select_none': "No se seleccionó ninguna contraseña.\n\nPor favor, seleccione una contraseña de la lista.",
        'password_select_one': "Por favor, seleccione exactamente una contraseña.\n\nHa marcado varias contraseñas.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_copia_seguridad",
        'filename_insert_suffix': "_con_inserción",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_páginas_eliminadas",
        'filename_pages_moved': "_páginas_movidas",
        'filename_rotated_all_suffix': "_todas_páginas_rotadas",
        'filename_rotated_suffix': "_página_rotada",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configuración de nombres de archivo al cambiar PDF",
        'filename_keep_suffixes': "Mantener extensiones anteriores (ej. _con_texto)",
        'filename_keep_suffixes_false': "Reemplazar",
        'filename_keep_suffixes_true': "Mantener",
        'filename_preview_label': "Vista previa del nombre de archivo:",
        'filename_preview_overwrite_hint': "Vista previa no disponible – el original se sobrescribirá.",
        'filename_separator': "Separador entre palabras",
        'filename_separator_none': "Sin separador",
        'filename_separator_space': "Espacio ( )",
        'filename_separator_underscore': "Guión bajo (_)",
        'filename_settings_saved': "Configuración de nombre de archivo guardada",
        'filename_settings_title': "Formato de nombre de archivo y copia de seguridad",
        'filename_timestamp_position': "Posición de la marca de tiempo",
        'filename_timestamp_position_after': "Después del nombre base",
        'filename_timestamp_position_before': "Al principio",
        'filename_timestamp_position_end': "Al final",
        'filename_use_timestamp': "Usar marca de tiempo",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Comportamiento ante cambios:</b><ul><li>Eliminar e insertar páginas</li><li>Insertar texto, firma, imagen y formas</li><li>OCR</li></ul></html>",
        'backup_section': "Copia de seguridad para operaciones de páginas (Eliminar, Mover)",
        'behavior_info': "Nota: Con 'Sobrescribir original' se ignoran las marcas de tiempo y sufijos – el archivo conserva su nombre.",
        'behavior_new_file': "Siempre crear nuevo archivo (con marca de tiempo y sufijo)",
        'behavior_overwrite': "Sobrescribir original (sin nuevo archivo)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Todas las páginas fueron rotadas.\n\nEl original permaneció sin cambios.\nNuevo archivo: {0}",
        'all_pages_rotated_voice': "Todas las páginas rotadas, nuevo archivo creado.",
        'empty_pages_deleted_new_file': "{0} páginas vacías fueron eliminadas.\n\nEl original permaneció sin cambios.\nNuevo archivo: {1}",
        'empty_pages_deleted_voice': "{0} páginas vacías eliminadas, nuevo archivo creado.",
        'ocr_keep_original': "Mantener original (abrir manualmente más tarde)",
        'ocr_new_file_question': "El nuevo PDF con capacidad de búsqueda se guardó en:\n{0}\n\n¿Desea abrirlo ahora?",
        'ocr_open_new': "Abrir nuevo archivo OCR",
        'ocr_original_kept': "El archivo original permanece abierto. El archivo OCR ha sido guardado.",
        'page_deleted_new_file': "La página {0} fue eliminada.\n\nEl original permaneció sin cambios.\nNuevo archivo: {1}",
        'page_deleted_voice': "Página {0} eliminada, nuevo archivo creado.",
        'page_rotated_new_file': "La página {0} fue rotada.\n\nEl original permaneció sin cambios.\nNuevo archivo: {1}",
        'page_rotated_voice': "Página {0} rotada, nuevo archivo creado.",
        'pages_deleted_new_file': "Se eliminaron {0} páginas.\n\nEl archivo original permaneció sin cambios.\nNuevo archivo: {1}",
        'pages_deleted_new_file_voice': "{0} páginas eliminadas, nuevo archivo creado.",
        'pages_inserted_new_file': "Se insertaron {0} páginas.\n\nEl archivo original permaneció sin cambios.\nNuevo archivo: {1}",
        'pages_inserted_new_file_ask': "Se insertaron {0} páginas.\n\nEl original permaneció sin cambios.\nNuevo archivo: {1}\n\n¿Desea abrirlo ahora?",
        'pages_inserted_voice_new': "{0} páginas insertadas, nuevo archivo creado.",
        'pages_moved_new_file': "Se movieron {0} páginas.\n\nEl archivo original permaneció sin cambios.\nNuevo archivo: {1}",
        'pages_moved_new_file_voice': "{0} páginas movidas, nuevo archivo creado.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "No mostrar de nuevo",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Configuración de copia de seguridad</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Copia de seguridad ACTIVADA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">En todos los cambios que sobrescriben el original</strong> (texto, firma, imagen, forma, OCR, rotar, insertar, eliminar/mover páginas) se crea <strong>automáticamente una copia de seguridad con marca de tiempo</strong> antes de aplicar el cambio.</p>
                <p style="margin: 5px 0 5px 20px;">• La copia de seguridad se encuentra junto al archivo original (ej. <code>Documento_copia_seguridad_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Si además ha activado la opción <strong>„Sobrescribir original“</strong>, también se crea una copia de seguridad.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Copia de seguridad DESACTIVADA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>No se crea ninguna copia de seguridad</strong> – ni al sobrescribir ni en operaciones de páginas.</p>
                <p style="margin: 5px 0 5px 20px;">• El archivo original puede perderse irreversiblemente al sobrescribirlo.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">¡Recomendado solo para usuarios experimentados!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Consejo:</strong> La configuración de copia de seguridad es independiente de la opción "Sobrescribir original". Puede combinar ambas.<br>
                Puede ocultar este mensaje permanentemente.
            </div>
        </div>
        """,
        'backup_info_title': "Comportamiento de la copia de seguridad",
        'backup_info_voice': "Aviso sobre el comportamiento de la copia de seguridad en operaciones de páginas. Copia de seguridad activada sobrescribe el original, copia de seguridad desactivada crea nuevo archivo.",
        'show_backup_info': "Información sobre la configuración de copia de seguridad",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "No mostrar de nuevo",
        'overwrite_enable_backup': "Activar copia de seguridad (recomendado)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Sobrescribir original</p>
            <p>Si activa esta opción, los cambios (texto, firma, imagen, forma, OCR, rotar, insertar) se guardan <strong>directamente en el original</strong> – <strong>no se crea ningún archivo nuevo</strong>.</p>
            <p>• El nombre del archivo permanece sin cambios.<br>
            • Las marcas de tiempo y sufijos se ignoran.<br>
            • <strong>Sin copia de seguridad, el original puede perderse irreversiblemente.</strong></p>
            <p style="color: #FFD700;">Recomendación: Active adicionalmente la opción de copia de seguridad para obtener copias de seguridad automáticas.</p>
        </div>
        """,
        'overwrite_info_title': "Sobrescribir original",
        'overwrite_info_voice': "Advertencia: Sobrescribir original – sin archivo nuevo. Se recomienda copia de seguridad.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Se insertaron {0} páginas.\n\nEl archivo original fue sobrescrito.\nSe creó una copia de seguridad.",
        'pages_inserted_overwrite_no_backup': "Se insertaron {0} páginas.\n\nEl archivo original fue sobrescrito.\nNO se creó ninguna copia de seguridad.",
        'texts_saved_overwrite_with_backup': "Los cambios se guardaron en el original.\n\nSe creó una copia de seguridad.",
        'texts_saved_overwrite_no_backup': "Los cambios se guardaron en el original.\n\nNO se creó ninguna copia de seguridad.",
        'texts_crosses_saved_new_file': "Se insertaron {0} {1} y {2} {3}.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",
        'texts_saved_new_file': "Se insertaron {0} {1}.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",
        'crosses_saved_new_file': "Se insertaron {0} {1}.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",
        'elements_saved_new_file': "Se insertaron {0} elementos.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",
        'signatures_saved_overwrite_with_backup': "La(s) firma(s) se guardaron en el original.\n\nSe creó una copia de seguridad.",
        'signatures_saved_overwrite_no_backup': "La(s) firma(s) se guardaron en el original.\n\nNO se creó ninguna copia de seguridad.",
        'images_saved_overwrite_with_backup': "La(s) imagen(es) se guardaron en el original.\n\nSe creó una copia de seguridad.",
        'images_saved_overwrite_no_backup': "La(s) imagen(es) se guardaron en el original.\n\nNO se creó ninguna copia de seguridad.",
        'forms_saved_overwrite_with_backup': "La(s) forma(s) se guardaron en el original.\n\nSe creó una copia de seguridad.",
        'forms_saved_overwrite_no_backup': "La(s) forma(s) se guardaron en el original.\n\nNO se creó ninguna copia de seguridad.",
        'signatures_saved_new_file': "Se insertaron {0} firmas.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",
        'images_saved_new_file': "Se insertaron {0} imágenes.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",
        'forms_saved_new_file': "Se insertaron {0} formas.\n\nEl archivo original permaneció sin cambios.\nSe creó un nuevo archivo.\n\nCargando el nuevo PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Advertencia: Este PDF contiene páginas rotadas. El posicionamiento podría diferir.",
        'page_rotated_warning_title': "Página rotada detectada",
        'page_rotated_warning_message': "La página actual {0} está rotada {1}°.\n\nLa inserción de elementos en páginas rotadas no es compatible.\n\n¿Desea rotar la página ahora a la posición vertical?",
        'page_rotated_warning_voice': "Advertencia: La página está rotada. Por favor, rótela primero.",
        'paste_on_rotated_page_simple_warning': "¡Inserción en la página {0} no posible!\n\nEsta página está rotada {1}°.\n\nPor favor, primero rote la página a 0° (Menú: Editar → Alinear página).\n\nAdvertencia:\nEl elemento copiado anteriormente se perderá si no guarda antes de rotar la página.",
        'paste_on_rotated_page_voice': "Inserción cancelada. La página está rotada. Por favor, alinee la página primero.",
        'page_rotated_cancel': "Cancelar",
        'page_rotated_rotate_until_upright': "Rotar página repetidamente (hasta que esté vertical)",
        'page_rotated_now_upright': "La página ahora está vertical. Ahora puede insertar.",
        'page_rotated_still_not_upright': "No se pudo rotar la página a la posición vertical. Por favor, corrija manualmente.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Ayuda: Corregir páginas rotadas",
        'help_rotated_pages_voice': "Se abre la ayuda para corregir páginas rotadas.",
        'btn_help': "Ayuda",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problema: Página rotada – La inserción no funciona correctamente</p>

            <p>Si la inserción de textos, firmas o formas en una página rotada no funciona correctamente, puede corregir la página con un editor de PDF externo.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solución con herramienta externa (ej. Vista previa de macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exportar página</strong><br>
                &nbsp;&nbsp;Haga clic en el menú <strong>Archivo → Exportar como páginas</strong> o use otro método para guardar la página deseada como un solo PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Abrir página en programa externo</strong><br>
                &nbsp;&nbsp;Abra el PDF exportado en un editor de PDF (ej. <strong>Vista previa de macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rotar página</strong><br>
                &nbsp;&nbsp;Gire la página para que quede vertical (en Vista previa: <strong>Herramientas → Rotar</strong> o <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Guardar</strong><br>
                &nbsp;&nbsp;Guarde la página corregida (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Volver a insertar la página en el documento original</strong><br>
                &nbsp;&nbsp;Vuelva a PDFDarkView e inserte la página corregida en la posición deseada:<br>
                &nbsp;&nbsp;<strong>Editar → Insertar páginas</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativa: Rotar página en el original</p>
                <p style="margin: 5px 0 5px 20px;">• Use la función de rotación integrada (<strong>Editar → Rotar página</strong>) para corregir la página paso a paso.<br>
                • Después de cada rotación puede comprobar si la inserción funciona ahora.<br>
                • Esta es a menudo la solución más rápida – ¡pruébela primero!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Consejo:</strong> Si encuentra páginas rotadas con frecuencia, puede ocultar permanentemente la advertencia en el diálogo de inserción.<br>
                El posicionamiento podría entonces diferir – use esta opción solo si conoce las consecuencias.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Alinear páginas",
        'menu_rotate_normalize_tooltip': "Rotar página o restablecer a 0°",
        'normalize_current_page': "Llevar la página actual a posición vertical (establecer a 0°)",
        'normalize_all_pages': "Llevar todas las páginas a posición vertical (establecer a 0°)",
        'page_normalized': "La página {0} se estableció en posición vertical.",
        'all_pages_normalized': "Todas las páginas se establecieron en posición vertical.",
        'page_already_upright': "La página {0} ya está vertical.",
        'all_pages_already_upright': "Todas las páginas ya están verticales.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>El PDF no contiene texto buscable.</p><p>¿Desea realizar OCR para exportar a {0}?</p>",
        'export_ocr_voice': "El PDF no contiene texto. Se requiere OCR para exportar a {0}.",
        'export_no_ocr_possible': "Exportación sin OCR no posible. Por favor, realice OCR a través del menú.",
        'ocr_failed_export_not_possible': "OCR falló. No se puede realizar la exportación.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "El PDF se abrirá en Vista Previa. Por favor, inicie el proceso de impresión allí.",
        'print_preview_manual': "El PDF se ha abierto. Por favor, ejecute el comando de impresión manualmente (ej. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Combinar PDFs",
        'merge_pdfs': "Combinar PDFs",
        'merge_progress_title': "Combinando PDFs...",
        'merge_pdfs_list': "PDFs en orden (Arrastrar y soltar para ordenar)",
        'merge_add_pdf': "Añadir PDF",
        'merge_remove': "Eliminar",
        'merge_move_up': "Subir",
        'merge_move_down': "Bajar",
        'merge_pdfs_info': "💡 Consejo: Puede cambiar el orden arrastrando y soltando",
        'merge_no_pdfs': "No se seleccionaron PDFs. Haga clic en 'Añadir PDF'.",
        'merge_info': "{0} PDFs seleccionados (aprox. {1} páginas)",
        'merge_open_file': "Abrir archivo",
        'merge_merge': "Combinar",
        'merge_error': "Error al combinar",
        'merge_min_two_pdfs_error': "Por favor, seleccione al menos dos archivos PDF para combinar.",
        'merge_select_pdfs': "Seleccionar PDFs para combinar",
        'merge_error_file': "Error al procesar",
        'merge_cancelled': "La combinación fue cancelada",
        'merge_preparing': "Preparando...",
        'merge_processing': "Procesando PDF {0} de {1}",
        'merge_saving': "Guardando PDF combinado...",
        'merge_complete': "¡Completado!",
        'merge_success_title': "Combinación exitosa",
        'merge_success_voice': "{0} PDFs se combinaron exitosamente.",
        'merge_success_message': "{0} PDFs se combinaron exitosamente.\n\nEl nuevo documento tiene ahora {1} páginas.\n\nNuevo archivo:\n{2}\n\nUbicación de guardado:\n{3}\n{2}\n\n¿Desea abrir este PDF?",
        'replace_file_title': "¿Reemplazar archivo?",
        'replace_file_message': "Ya hay un PDF abierto. ¿Desea reemplazarlo con el nuevo archivo?",
        'btn_yes': "Sí",
        'btn_no': "No",
        'filename_merge_suffix': "combinado",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Abriendo {0}...",
        'progress_merge_reading': "Leyendo {0}...",
        'progress_merge_adding': "Añadiendo {0} páginas...",
        'progress_merge_optimizing': "Optimizando PDF...",
        'progress_merge_writing': "Escribiendo PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "cerrar el PDF",
        'action_close_window': "cerrar la ventana",
        'action_open_new_pdf': "abrir un nuevo PDF",
        'action_quit_app': "salir de la aplicación",
        'changes_saved': "Los cambios se guardaron.",
        'file_close_title': "Cerrar archivo PDF",
        'save_before_action': "¿Deben guardarse los cambios antes de {0}? ¿Sí o No?",
        'save_before_action_voice': "¿Deben guardarse los cambios antes de {0}? ¿Sí o No?",
        'save_before_close_question': "¿Deben guardarse los cambios antes de cerrar? ¿Sí o No?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF con capacidad de búsqueda creado:\n\n{0}\n\n<b>inténtelo de nuevo si es necesario",
        "ocr_rotate_title": "Alinear páginas antes del OCR",
        "ocr_rotate_question": "El PDF contiene páginas rotadas.\n¿Desea alinear todas las páginas a 0° antes del OCR?\nEsto mejora significativamente el reconocimiento de texto.",
        "ocr_rotate_yes": "Sí, alinear",
        "ocr_rotate_no": "No, iniciar OCR directamente",
        "ocr_rotate_voice": "El PDF contiene páginas rotadas. ¿Deben alinearse todas las páginas antes del OCR?",
        "ocr_not_performed_message": "No hay texto presente. Realice OCR (menú \"Editar\" → \"Realizar OCR\" o tecla Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Configuración de OCR",
        "ocr_language_btn": "Seleccionar idioma de OCR",
        "ocr_language": "Idioma(s) de OCR",
        "ocr_language_current": "Idioma actual:",
        "ocr_param_info": "Información del parámetro",

        "ocr_force_ocr_label": "Forzar OCR",
        "ocr_deskew_label": "Corregir inclinación",
        "ocr_clean_label": "Limpiar imagen",
        "ocr_oversample_label": "Resolución (DPI)",
        "ocr_pagesegmode_label": "Segmentación de página",
        "ocr_oem_label": "Modo de motor OCR",
        "ocr_optimize_label": "Compresión de PDF",
        "ocr_jobs_label": "Procesos paralelos",
        "ocr_verbose_label": "Detalle del registro",

        "ocr_force_ocr_tooltip": "Forzar OCR en cada página, incluso si ya existe texto",
        "ocr_deskew_tooltip": "Alinear automáticamente escaneos inclinados",
        "ocr_clean_tooltip": "Eliminar ruido y artefactos de la imagen",
        "ocr_oversample_tooltip": "Escalar imagen antes del OCR a este DPI",
        "ocr_pagesegmode_tooltip": "Determina cómo se divide la página en áreas de texto",
        "ocr_oem_tooltip": "Selecciona el motor OCR de Tesseract",
        "ocr_optimize_tooltip": "Nivel de compresión del PDF de salida",
        "ocr_jobs_tooltip": "Número de procesos OCR paralelos",
        "ocr_verbose_tooltip": "Nivel de detalle de la salida del registro",
        "ocr_settings_explain_btn": "Explicación",

        "ocr_force_ocr_explain": "Fuerza el reconocimiento de texto en <b>cada</b> página, incluso si ya contiene texto.\n\nRecomendación: <b>Activado</b> para PDF escaneados, <b>Desactivado</b> para PDF nativos con texto ya existente.",

        "ocr_deskew_explain": "Corrige escaneos ligeramente inclinados (hasta aprox. 5°).\n\nRecomendación: <b>Activado</b> para documentos escaneados, <b>Desactivado</b> si las páginas ya están perfectamente rectas.",

        "ocr_clean_explain": "Elimina ruido, puntos y pequeños artefactos de la imagen.\n<b>IMPORTANTE:</b> Para textos árabes, tailandeses o vietnamitas con signos diacríticos (puntos arriba/abajo de las letras) esta opción debe estar <b>desactivada</b>, de lo contrario se pueden perder caracteres importantes.",

        "ocr_oversample_explain": "Escala la imagen <b>antes</b> del reconocimiento de texto a los DPI especificados.<br><br>• <b>72-150 DPI:</b> Muy rápido, pero baja tasa de reconocimiento<br>• <b>200-300 DPI:</b> Rango óptimo (Predeterminado: 300)<br>• <b>400+ DPI:</b> Apenas mejor reconocimiento, pero archivos significativamente más grandes<br><br>Recomendación: 300 DPI para escrituras complejas (árabe, chino, japonés), 200 DPI para idiomas occidentales.",

        "ocr_pagesegmode_explain": "Determina cómo Tesseract divide la página en áreas de texto.\n\n• <b>3 - Automático (Predeterminado):</b> Bueno para diseños mixtos\n• <b>4 - Columna única:</b> Para textos de una columna\n• <b>5 - Bloque vertical:</b> Para escrituras verticales (japonés, chino)\n• <b>6 - Bloque de texto uniforme:</b> Óptimo para texto fluido sin columnas\n• <b>11 - Imagen sin procesar:</b> Para escaneos deficientes / escritura a mano\n\nRecomendación: <b>6</b> para documentos de texto simples, <b>3</b> para diseños complejos.",

        "ocr_oem_explain": "Selecciona el motor OCR de Tesseract.\n\n• <b>0 - Legacy:</b> Motor antiguo (rápido, pero menos preciso)\n• <b>1 - LSTM:</b> Motor neuronal (más lento, pero más preciso)\n• <b>2 - Legacy + LSTM:</b> Combina ambos resultados\n• <b>3 - Predeterminado (LSTM preferido):</b> Mejor opción para la mayoría de los casos\n\nRecomendación: <b>3</b> para máxima precisión de reconocimiento.",

        "ocr_optimize_explain": "Comprime el PDF de salida.\n\n• <b>0:</b> Sin optimización (procesamiento más rápido)\n• <b>1:</b> Optimización ligera (buen compromiso)\n• <b>2:</b> Optimización moderada\n• <b>3:</b> Optimización fuerte (archivo más pequeño, pero más lento)\n\nRecomendación: <b>1</b> para uso diario.",

        "ocr_jobs_explain": "Número de procesos paralelos para OCR.\n\n• <b>1:</b> Lento, pero menor consumo de memoria\n• <b>4-8:</b> Óptimo para procesadores multinúcleo modernos\n• <b>12+:</b> Apenas procesamiento más rápido con alto consumo de memoria\n\nRecomendación: Número de núcleos de CPU (por ejemplo, <b>4</b> en sistemas de 4 núcleos).",

        "ocr_verbose_explain": "Nivel de detalle de la salida del registro en la consola.\n\n• <b>0:</b> Sin salida\n• <b>1:</b> Progreso y mensajes de estado\n• <b>2:</b> Salida detallada\n• <b>3:</b> Salida de depuración completa (muy extensa)\n\nRecomendación: <b>1</b> para operación normal.",

        "ocr_reset_title": "Configuración restablecida",
        "ocr_reset_message": "Toda la configuración de OCR se ha restablecido a los valores predeterminados.",
        "info_tooltip": "Más información sobre este parámetro",
        "ocr_reset_defaults": "Restablecer a valores predeterminados",

        "ocr_psm_0": "Automático (motor Legacy)",
        "ocr_psm_1": "Detección automática de columnas",
        "ocr_psm_3": "Automático (Predeterminado)",
        "ocr_psm_4": "Columna única",
        "ocr_psm_5": "Bloque vertical",
        "ocr_psm_6": "Bloque de texto uniforme",
        "ocr_psm_7": "Línea de texto única",
        "ocr_psm_8": "Palabra única",
        "ocr_psm_11": "Imagen sin procesar (sin análisis de diseño)",

        "ocr_oem_0": "Motor Legacy (rápido)",
        "ocr_oem_1": "Motor LSTM (neuronal, preciso)",
        "ocr_oem_2": "Legacy + LSTM combinado",
        "ocr_oem_3": "Predeterminado (LSTM preferido)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Idioma(s) de OCR...",
        "ocr_language_title": "Seleccionar idioma(s) de OCR",
        "ocr_language_instruction": "Seleccione el idioma(s) para el reconocimiento de texto (OCR).\n¡Precaución: Varios idiomas van en detrimento del rendimiento y la precisión!\nObtiene los mejores resultados si selecciona solo un idioma.",
        "ocr_language_predefined": "Combinaciones predefinidas",
        "ocr_language_custom": "Personalizado...",
        "ocr_language_selected": "Idiomas OCR seleccionados",
        "ocr_language_changed": "Idioma OCR cambiado a {0}",
        "ocr_language_auto_detect": "Los idiomas disponibles se detectan automáticamente.",
        "ocr_language_none_found": "¡No se encontraron datos de idioma de Tesseract! Instale paquetes de idioma (por ejemplo, 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Selección de idioma personalizada",
        "ocr_language_available": "Idiomas disponibles (instalados):",
        "ocr_language_select_hint": "Seleccione uno o más idiomas:",
        "ocr_language_confirm": "Aplicar",
        "ocr_language_reset": "Restablecer a predeterminado (deu+eng+vie)",
        "ocr_language_priorities": "Idiomas recomendados (preinstalados):",

        "select_all_languages": "Seleccionar todo",
        "clear_all_languages": "Borrar selección",
        "install_language_packs": "Instalar paquetes de idioma faltantes...",
        "install_hint": "💡 Consejo: No todos los idiomas están instalados en su sistema. Mediante este botón obtendrá ayuda para la instalación.",
        "ocr_language_install_title": "Instalación de paquetes de idioma de Tesseract",

        "ocr_missing_languages": "Paquetes de idioma OCR faltantes",
        "ocr_missing_languages_message": "Los siguientes idiomas seleccionados no están instalados en su sistema:\n\n{0}\n\nInstale los paquetes de idioma faltantes (consulte la ayuda en 'Ayuda de instalación').\n\n¿Desea abrir la ayuda de instalación ahora?",
        "ocr_missing_languages_voice": "Faltan paquetes de idioma. Instale los idiomas faltantes.",
        "ocr_install_help_now": "Abrir ayuda",
        "ocr_continue_anyway": "Intentar de todas formas",
        "ocr_language_error_title": "Error de idioma OCR",
        "ocr_language_error_message": "Error durante el reconocimiento de texto: {0}\n\nVerifique su configuración de idioma OCR (Configuración → Idioma OCR).",
        "ocr_install_help_button": "Ayuda de instalación",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalar paquetes de idioma de Tesseract</p>

        <p>Para que el OCR funcione en un idioma específico, los datos de idioma correspondientes deben estar instalados en su sistema. Siga las instrucciones para su sistema operativo:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Abra la <strong>Terminal</strong> (Finder → Programas → Utilidades → Terminal).</li>
        <li>Instale todos los idiomas disponibles con:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Esto puede tardar unos minutos.)</li>
        <li>O solo idiomas individuales (por ejemplo, vietnamita):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        En versiones actuales de Homebrew, es posible que <code>*.traineddata</code> deba descargarse manualmente (ver abajo).</li>
        <li>Después de la instalación: Cierre este diálogo y vuelva a abrir la selección de idioma OCR – los nuevos idiomas aparecerán automáticamente.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Abra una terminal (Ctrl+Alt+T).</li>
        <li>Instale el idioma deseado, por ejemplo, para vietnamita:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Códigos de idioma importantes: <code>deu</code> (alemán), <code>eng</code> (inglés), <code>vie</code> (vietnamita), <code>spa</code> (español), <code>fra</code> (francés), <code>ita</code> (italiano), <code>nld</code> (neerlandés), <code>fin</code> (finlandés), <code>swe</code> (sueco), <code>nor</code> (noruego).</li>
        <li>Mostrar todos los paquetes disponibles:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Descargue los archivos <code>*.traineddata</code> deseados de:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (por ejemplo, <code>vie.traineddata</code> para vietnamita).</li>
        <li>Copie los archivos a la carpeta de idiomas de Tesseract, generalmente:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Ajuste según la instalación individual.)</li>
        <li>Reinicie la aplicación (o vuelva a abrir la selección de idioma OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativa para todos los sistemas</p>
        <ul>
        <li>Instale <strong>OCRmyPDF</strong> y <strong>Tesseract</strong> con un administrador de paquetes de su elección. La mayoría de las instalaciones ya contienen algunos idiomas estándar (inglés, alemán, francés).</li>
        <li>Los idiomas faltantes se pueden instalar en cualquier momento – la selección de idioma OCR solo muestra los idiomas realmente existentes.</li>
        </ul>

        <hr>
        <p><b>✅ Después de la instalación:</b> No es necesario reiniciar la aplicación – los idiomas recién agregados aparecerán inmediatamente en la lista.</p>
        <p><b>📖 Ayuda con códigos de idioma:</b> Puede encontrar una lista completa en la <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">documentación de Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Fuentes Noto Sans",
        "info_noto_font_voice": "Guía de instalación de fuentes Noto Sans",
        "btn_info_noto_font_install": "Información de fuente",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Cómo instalar las fuentes gratuitas Noto de Google</h2>

        <p>Las <strong>fuentes Noto</strong> son una familia de fuentes de código abierto de Google. Su objetivo es no ver <em>"ningún tofu"</em> (es decir, sin cuadros vacíos □) y mostrar correctamente cada carácter del estándar Unicode. Son el complemento ideal para aplicaciones que necesitan mostrar textos en muchos idiomas diferentes.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalación en macOS</h3>

        <p><strong>Método 1: Con Homebrew (para avanzados)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Método 2: A través del "Font Book" (Recomendado)</strong></p>

        <ol>
        <li>Descargue el paquete de fuentes oficial:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extraiga el archivo ZIP</li>
        <li>Copie los archivos a <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalación en Windows (10 & 11)</h3>

        <p><strong>Método 1: Microsoft Store (Recomendado)</strong><br>
        Busque "Google Noto Fonts" o "Noto Sans" y haga clic en <strong>Instalar</strong>.</p>

        <p><strong>Método 2: Instalación manual</strong></p>

        <ol>
        <li>Descarga:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extraer ZIP</li>
        <li>Seleccione archivos .ttf / .otf</li>
        <li>Clic derecho → <strong>Instalar</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        o<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nombre\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalación en Linux</h3>

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

        <p>Verificación:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Administrar marcadores",
        "bookmark_add": "Agregar marcador",
        "bookmark_add_tooltip": "Guardar página actual como marcador",
        "bookmark_remove": "Eliminar marcador",
        "bookmark_remove_tooltip": "Borrar el marcador marcado",
        "bookmark_remove_all": "Eliminar todos",
        "bookmark_remove_all_tooltip": "Borrar todos los marcadores de este PDF",
        "bookmark_jump": "Ir al marcador",
        "bookmark_jump_tooltip": "Ir a la página seleccionada",
        "bookmark_name": "Nombre",
        "bookmark_page": "Página",
        "bookmark_no_bookmarks": "No hay marcadores presentes.\nHaga clic en 'Agregar' para guardar la página actual como marcador.",
        "bookmark_added": "Marcador para la página {0} agregado: {1}",
        "bookmark_removed": "Marcador eliminado: {0}",
        "bookmark_all_removed": "Se han eliminado todos los marcadores.",
        "bookmark_name_default": "Página {0}",
        "bookmark_name_prompt": "Nombre para el marcador:\n(el texto largo se acortará a 50 caracteres)",
        "bookmark_name_prompt_title": "Nombre del marcador",
        "bookmark_confirm_remove_all": "¿Está seguro de que desea eliminar todos los {0} marcadores?",
        "menu_bookmarks": "Marcadores",
        "bookmark_manage": "Administrar marcadores",
        "bookmark_next": "Siguiente marcador",
        "bookmark_prev": "Marcador anterior",
        "bookmark_page_display": "Página {0}",
        "bookmark_exists": "Ya existe un marcador para esta página con este nombre.",
        "bookmark_select_first": "Primero seleccione un marcador.",
        "bookmark_confirm_remove": "¿Está seguro de que desea eliminar el marcador 'Página {0}: {1}'?",
        "bookmark_jumped_to": "Saltado al marcador '{0}' en la página {1}.",
        "bookmark_jumped_to_voice": "Marcador {0}, página {1}",
        "btn_close": "Cerrar",

        "bookmark_list": "Sus marcadores",
        "bookmark_rename": "Renombrar marcador",
        "bookmark_rename_tooltip": "Cambiar el nombre del marcador seleccionado",
        "bookmark_rename_title": "Renombrar marcador",
        "bookmark_rename_prompt": "Nuevo nombre para el marcador en la página {0}:\n(máx. 50 caracteres)",
        "bookmark_renamed": "El marcador '{0}' ha sido renombrado a '{1}'.",
        "bookmark_item_tooltip": "Página {0}: {1}\nDoble clic para saltar",
        "bookmark_name_exists_question": "Ya existe un marcador con el nombre '{0}' en esta página.\n¿Renombrar de todas formas?",

        "context_bookmarks": "Marcadores",
        "context_bookmark_add_here": "Agregar marcador para esta página",
        "context_bookmarks_existing": "Marcadores existentes:",
        "context_bookmarks_jump": "Ir al marcador:",
        "context_bookmarks_none": "No hay marcadores presentes",
        "context_bookmarks_clear_all": "Eliminar todos los {0} marcadores",

        "bookmark_search_placeholder": "Buscar marcadores... (nombre o página)",
        "bookmark_search_results": "%d marcadores encontrados para \"%s\"",
        "bookmark_no_search_results": "No se encontraron marcadores para \"%s\"",
        "bookmark_no_search_results_label": "Sin resultados para \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Editar metadatos PDF",
        "metadata_title": "Título",
        "metadata_title_placeholder": "Título del documento",
        "metadata_title_tooltip": "El título del documento (se muestra en la barra de título)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Nombre del autor",
        "metadata_author_tooltip": "El creador del documento",
        "metadata_subject": "Asunto",
        "metadata_subject_placeholder": "Asunto del documento",
        "metadata_subject_tooltip": "Una breve descripción del contenido",
        "metadata_keywords": "Palabras clave",
        "metadata_keywords_placeholder": "Palabras clave separadas por comas",
        "metadata_keywords_tooltip": "Palabras clave para categorizar el documento",
        "metadata_creator": "Creador",
        "metadata_creator_placeholder": "Aplicación que creó el PDF",
        "metadata_creator_tooltip": "El software con el que se creó el documento",
        "metadata_producer": "Productor",
        "metadata_producer_placeholder": "Aplicación que convirtió el PDF",
        "metadata_producer_tooltip": "El software que convirtió el PDF",
        "metadata_creation_date": "Fecha de creación",
        "metadata_creation_date_tooltip": "La fecha de creación del documento",
        "metadata_mod_date": "Fecha de modificación",
        "metadata_mod_date_tooltip": "La fecha de la última modificación",
        "metadata_pdf_info": "📄 Información del PDF",
        "metadata_pages": "Número de páginas",
        "metadata_file_size": "Tamaño del archivo",
        "metadata_pdf_version": "Versión del PDF",
        "metadata_encrypted": "Cifrado",
        "metadata_encrypted_yes": "Sí (protegido con contraseña)",
        "metadata_encrypted_no": "No",
        "metadata_reload": "📂 Recargar desde PDF",
        "metadata_reset": "Descartar cambios",
        "metadata_reloaded": "Los metadatos se han recargado desde el PDF.",
        "metadata_reset_done": "Todos los campos de metadatos se han restablecido.",
        "metadata_no_file": "No se ha cargado ningún archivo PDF.",
        "metadata_save_error": "Error al guardar los metadatos",
        "metadata_saved": "Los metadatos se han guardado correctamente.",
        "metadata_pdf_version_unknown": "PDF (desconocido)",
        "metadata_saved_message": "Los metadatos se han guardado correctamente.",
        "metadata_saved_voice": "Metadatos guardados.",

        "metadata_custom": "🔧 Metadatos personalizados",
        "metadata_custom_placeholder": "{\n  \"mi_campo\": \"mi valor\",\n  \"otro_campo\": 123\n}",
        "metadata_custom_tooltip": "Formato JSON para metadatos personalizados (opcional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Plantilla \"{0}\" seleccionada - Doble clic para insertar",
        "text_use_template": "Usar bloque de texto",
        "text_type": "Tipo",
        "text_search_templates": "Buscar bloques de texto...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Información de Exportación / Importación",
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

        <h3>📦 ¿Qué se exporta? (Descripción general)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Configuración general de la aplicación</span></li>
            <li class="detail">• Modo oscuro/claro</li>
            <li class="detail">• Inversión del modo oscuro para imágenes</li>
            <li class="detail">• Valor umbral de gris</li>
            <li class="detail">• Idioma</li>
            <li class="detail">• Geometría de la ventana</li>
            <li class="detail">• Modo de zoom</li>
            <li class="detail">• Navegación (Barra de navegación visible)</li>
            <li class="detail">• Salida de voz (activado/desactivado)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Configuración de copia de seguridad</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nomenclatura de archivos (Marca de tiempo, Separador, Sufijos)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Configuración para inserciones de</span></li>
            <li class="detail">• Firmas</li>
            <li class="detail">• Texto y bloques de texto</li>
            <li class="detail">• Cruces, imágenes y formas</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Configuración de OCR</span></li>
            <li class="detail">• Idioma</li>
            <li class="detail">• Forzar OCR · Modo de página</li>
            <li class="detail">• Preprocesamiento de imagen: Corregir inclinación, Limpiar, Sobremuestreo</li>
            <li class="detail">• Número de trabajos paralelos</li>
            <li class="detail">• Modo de inversión</li>
            <li class="detail">• Valor umbral de gris</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Marcadores</span></li>
            <li class="detail">• Todos los marcadores por archivo PDF (Página, Nombre, Hora de creación)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Base de datos de contraseñas</span></li>
            <li class="detail">• Contraseñas PDF guardadas (opcionalmente cifradas o texto plano)</li>
            <li class="detail">• Hash de contraseña maestra (si está establecida)</li>
            <li class="detail">• Datos de verificación</li>
        </ul>

        <h4>⚠️ Notas importantes</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Al importar:</strong>
            <ul>
                <li><span class="warning">➜ TODA la configuración actual se sobrescribirá por completo</span></li>
                <li>• Es obligatorio reiniciar la aplicación</li>
                <li>• Las firmas, bloques de texto y marcadores existentes serán reemplazados</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Contraseña maestra y modo de exportación:</strong>
            <ul>
                <li>• Cuando la contraseña maestra está activa, puede elegir:</li>
                <li>  - <span style="color: #98FB98;"><strong>Descifrado</strong></span> (las contraseñas están en texto plano en el ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Cifrado</strong></span> (solo se pueden leer con la contraseña maestra en el sistema de destino)</li>
                <li>• El hash de la contraseña maestra se almacena <strong>siempre</strong> cifrado</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Aviso de seguridad:</strong>
            <ul>
                <li>• El archivo ZIP exportado contiene datos confidenciales (<strong>contraseñas, marcadores, firmas</strong>)</li>
                <li>• Guárdelo de forma segura (por ejemplo, unidad USB cifrada, administrador de contraseñas)</li>
                <li>• Si se pierde el archivo, las contraseñas PDF guardadas se pierden irrecuperablemente</li>
            </ul>
        </div>

        <h4>📁 Formato de exportación</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            La configuración se guarda en un único archivo ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Este ZIP contiene el <code>settings.json</code> completo (de su configuración), así como posibles archivos de imagen de firma incrustados y contraseñas cifradas.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Firmas - Guía",
        'signature_guide_html': """
        📝 <strong>Firmas - Guía rápida</strong><br>
        <ul>
        <li>Configurar contraseña maestra</li>
        <li>Configurar firmas en el menú <em>Ajustes</em> (tamaño, marca de tiempo, …)</li>
        <li>Insertar con <strong>CLIC DERECHO</strong> en la posición deseada (se necesita contraseña maestra una vez por sesión)</li>
        <li>Mover firma con el ratón o teclas de flecha</li>
        <li>Insertar varias firmas consecutivas</li>
        <li>Personalizar cada firma individualmente</li>
        <li>Descartar firma individual</li>
        <li>Guardar / descartar todas las firmas a la vez</li>
        <li>Alternativamente, también se puede usar la barra de menú.</li>
        </ul>
        """,
        'signature_guide_voice': "Guía rápida para firmas. Configurar contraseña maestra. Configurar firmas en ajustes. Insertar con clic derecho.",

        'image_guide_title': "Insertar imágenes - Guía",
        'image_guide_html': """
        📷 <strong>Insertar imágenes en PDF - Guía rápida</strong><br>
        <ol>
        <li>Clic derecho en la posición deseada</li>
        <li><em>„Insertar imagen“</em> → Seleccionar imagen</li>
        <li>Posicionar imagen: Arrastrar con el ratón</li>
        <li>Ajustar tamaño: Arrastrar por las esquinas/bordes</li>
        <li>Mantener relación de aspecto: Tecla <strong>[A]</strong></li>
        <li>Más ajustes: Clic derecho en la imagen</li>
        </ol>
        <p><strong>Consejo:</strong> En el menú contextual puede ajustar la configuración.</p>
        """,
        'image_guide_voice': "Guía rápida para imágenes. Clic derecho, insertar imagen, seleccionar. Posicionar con ratón, ajustar tamaño en esquinas. Relación de aspecto con tecla A.",

        'form_guide_title': "Insertar formas - Guía",
        'form_guide_html': """
        📐 <strong>Insertar formas en PDF - Guía rápida</strong><br>
        <ol>
        <li>Seleccionar tipo de forma (rectángulo, elipse, línea, flecha)</li>
        <li>Clic en la posición:
            <ul>
            <li>Para rectángulo/elipse: Un clic coloca la forma</li>
            <li>Para línea/flecha: Dos clics para punto inicial y final</li>
            </ul>
        </li>
        <li>Posicionar forma: Arrastrar con el ratón</li>
        <li>Ajustar tamaño: Arrastrar por las esquinas/bordes</li>
        <li>Guardar forma: <strong>Enter</strong></li>
        <li>Descartar forma: <strong>ESC</strong></li>
        <li>Más ajustes: Clic derecho en la forma</li>
        </ol>
        <p><strong>Consejo:</strong> En el menú contextual puede ajustar la configuración.</p>
        """,
        'form_guide_voice': "Guía rápida para formas. Seleccionar tipo de forma. Para rectángulo o elipse hacer un clic, para línea o flecha dos clics. Posicionar con ratón, ajustar tamaño en esquinas. Guardar con Enter, descartar con Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "anterior",
        "btn_next_result": "siguiente",
        "ocr_text_window": "Ventana de texto OCR",
        "bookmark_existing": "Marcadores existentes",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Comparación OCR Mac - Windows",
        'ocr_method_mac_win_title': "Diferencias OCR entre Mac y Windows",
        'ocr_method_mac_win_voice': "Mac es mejor",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Diferencias entre macOS y Windows</strong></p>

        <p><strong>macOS (recomendado)</strong></p>
        <p>Herramienta:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultado:</p>
        <ul>
        <li>Un PDF con capacidad de búsqueda con texto incrustado que conserva en gran medida el diseño original.</li>
        </ul>
        <p>Ventajas:</p>
        <ul>
        <li>Excelente calidad de reconocimiento de texto (incluso en páginas torcidas).</li>
        <li>Conservación de gráficos vectoriales y fuentes.</li>
        <li>Barra de progreso GUI mediante evaluación de subproceso.</li>
        <li>Control total sobre todos los parámetros de OCR (Deskew, Clean, Oversample, optimización).</li>
        <li>La búsqueda de texto está directamente disponible en la ventana principal (vista PDF).</li>
        </ul>
        <p>Desventajas:</p>
        <ul>
        <li>Requiere herramientas adicionales del sistema (ocrmypdf, Ghostscript, unpaper, pngquant – incluidas en el paquete de la aplicación).</li>
        <li>Manejo de errores más complejo (bloqueos, tiempos de espera).</li>
        </ul>

        <p><strong>Windows (alternativa estable)</strong></p>
        <p>Herramienta:</p>
        <ul>
        <li>pytesseract (conexión directa a Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultado:</p>
        <ul>
        <li>Un PDF con capacidad de búsqueda que visualmente corresponde a un PDF de imagen, pero se puede buscar a través del texto transparente.</li>
        </ul>
        <p>Ventajas:</p>
        <ul>
        <li>No se me ocurre ninguna ahora mismo.</li>
        </ul>
        <p>Desventajas:</p>
        <ul>
        <li>El PDF es esencialmente una imagen con texto invisible; el diseño puede desviarse ligeramente en documentos complejos (columnas, tablas).</li>
        <li>No hay corrección automática de inclinación (--deskew) ni limpieza de imagen (--clean).</li>
        <li>La barra de progreso GUI se actualiza solo de forma aproximada basada en el número de páginas procesadas.</li>
        <li>La velocidad de OCR es ligeramente más lenta (ya que cada página se procesa individualmente).</li>
        <li>La búsqueda de texto se redirige a la ventana de texto OCR.</li>
        </ul>

        <p><strong>Similitudes</strong></p>
        <ul>
        <li>Ambos métodos crean un PDF con capacidad de búsqueda en el mismo directorio que el archivo fuente.</li>
        <li>Los ajustes de OCR (idioma, DPI, modo de segmentación de página, modo de motor OCR) se pueden configurar a través de OCRSettingsDialog y son válidos en ambas implementaciones.</li>
        </ul>

        <p><strong>Recomendación:</strong></p>
        <ul>
        <li>macOS: El binario ocrmypdf proporciona los mejores resultados – Compre un Mac y use la versión (PDFDarkView para Mac con chip Apple Silicon o Intel). ¡Los resultados de OCR son mejores que en Windows!</li>
        <li>Windows: Use la solución pytesseract. Es estable y proporciona una calidad completamente suficiente para la mayoría de los documentos.</li>
        </ul>

        <p><strong>Nota importante:</strong></p>
        <ul>
        <li>Ambas versiones están completamente integradas en la interfaz de usuario – el usuario no nota ninguna diferencia.</li>
        <li>El programa decide automáticamente qué motor OCR usar según el sistema operativo.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Crear firma (desde escaneo)",
        "signature_create_title": "Seleccionar firma escaneada (PDF/imagen)",
        "image_pdf_filter": "Imágenes y PDF",
        "signature_pdf_empty": "El PDF no contiene páginas.",
        "signature_created_success": "Firma creada exitosamente: {0}",
        "signature_create_error": "Error al crear la firma:\n{0}",
        "rembg_missing": "rembg no está instalado.\nPor favor instale: pip install rembg\nError: {0}",
        "signature_name_title": "Nombre de archivo para la firma",
        "signature_name_message": "Por favor ingrese un nombre de archivo para la nueva firma (se guardará como PNG con fondo transparente):",
        "signature_name_label": "Nombre de archivo:",
        "signature_name_voice": "Ingrese nombre de archivo para la firma",
        "signature_processing": "Procesando...",
        "signature_creation_title": "Creando firma",
        "signature_overwrite_warning": "El archivo '{0}' ya existe. ¿Sobrescribir?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Preparar PDF para firma",
        "signature_prepare_instruction":"Por favor seleccione un PDF que contenga una firma escaneada en una sola página.\n\nPara un reconocimiento óptimo, asegúrese de que:\n• La firma esté escrita con tinta negra (bolígrafo o rotulador fino) sobre papel blanco.\n• La firma se encuentre en el tercio superior de una página A4 por lo demás en blanco.\n• El PDF haya sido escaneado con al menos 300 dpi.\n• La firma sea clara y no demasiado delgada.\n• No haya patrones de fondo o líneas molestas.",
        "signature_prepare_voice":"Por favor seleccione un PDF con una firma escaneada. Preste atención a la buena calidad y contraste.",
        "sig_thickness_label":"Grosor de línea:",
        "sig_thickness_normal":"Normal (fino)",
        "sig_thickness_bold":"Negrita (recomendado)",
        "sig_thickness_very_bold":"Muy negrita",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Agregar idiomas GUI y OCR - Guía",
        'language_guide_title': "Agregar idiomas GUI y OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Descargue el archivo de traducción deseado <code>translations_xy.py</code> de<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        y colóquelo en el siguiente directorio:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Abra su navegador web.</li>
        <li>Vaya a: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Busque en el borde derecho de la pantalla "Releases" y seleccione el marcado con <strong>"latest"</strong>.</li>
        <li>En la siguiente página de lanzamiento, descargue el archivo <code>Source Code.zip</code> en la parte inferior.</li>
        <li>Descomprima el archivo ZIP.</li>
        <li>Busque en la carpeta descomprimida todos los archivos de idioma que necesite y cópielos en el directorio:<br/>
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
        "menu_watermark":"Insertar marca de agua",
        "fullpage_text_watermark_title":"Texto como marca de agua",
        "fullpage_image_watermark_title":"Imagen como marca de agua",
        "filename_with_watermark":"_con_marca_de_agua",
        "watermark_text":"Texto:",
        "watermark_text_placeholder":"Su texto de marca de agua...",
        "watermark_font_family":"Fuente:",
        "watermark_font_size":"Tamaño de fuente:",
        "watermark_format":"Formato:",
        "watermark_bold":"Negrita",
        "watermark_italic":"Cursiva",
        "watermark_color":"Color:",
        "watermark_choose_color":"Elegir color...",
        "watermark_opacity":"Opacidad / Transparencia:",
        "watermark_direction":"Dirección de lectura:",
        "watermark_direction_l_r":"Izquierda → Derecha",
        "watermark_direction_bl_tr":"Abajo izquierda → Arriba derecha",
        "watermark_direction_tl_br":"Arriba izquierda → Abajo",
        "watermark_direction_b_t":"Abajo → Arriba",
        "watermark_direction_t_b":"Arriba → Abajo",
        "watermark_preview":"Vista previa:",
        "watermark_preview_sample":"Texto de ejemplo",
        "watermark_empty_text":"Por favor, introduzca un texto.",
        "watermark_applied":"La marca de agua se ha aplicado a todas las páginas.",
        "watermark_saved":"Marca de agua guardada.",
        "image_scale":"Tamaño:",
        "image_preview":"Vista previa de la imagen:",
        "no_image_selected":"No se ha seleccionado ninguna imagen",
        "browse":"Examinar...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redacciones",
        "redact_add_black": "Redacción (negro)",
        "redact_add_white": "Redacción (blanco / borrar)",
        "redact_added_black": "Redacción negra añadida",
        "redact_added_white": "Redacción blanca añadida",
        "redact_apply_all": "Aplicar todas las redacciones y guardar",
        "redact_discard_all": "Descartar todas las redacciones",
        "redact_discard": "Descartar esta redacción",
        "no_redactions": "No hay redacciones",
        "redact_confirm_title": "Aplicar redacciones de forma permanente",
        "redact_confirm_message": "Advertencia: Las áreas marcadas se eliminarán de forma irrevocable (negro o blanco).\nSe creará una copia de seguridad (si está activada).\n\n¿Continuar?",
        "redact_apply": "Sí, redactar ahora",
        "redact_saved": "{0} redacción(es) aplicada(s) y guardada(s) correctamente.",
        "redact_saved_voice": "{0} redacción(es) aplicada(s)",
        "redact_error": "Error al redactar",
        "filename_redacted":"_redactado",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Insertar números de página',
        'page_numbers_format': 'Formato de número:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arábigo)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romano minúscula)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romano mayúscula)',
        'page_numbers_format_letter': 'A, B, C ... (letras)',
        'page_numbers_format_custom': 'Personalizado',
        'page_numbers_custom_pattern': 'Patrón:',
        'page_numbers_custom_placeholder': 'p.ej. "Página {nummer}" o "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Use {nummer} para el número de página actual y {total} para el total',
        'page_numbers_position': 'Posición:',
        'page_numbers_pos_tl': 'Arriba izquierda',
        'page_numbers_pos_tc': 'Arriba centro',
        'page_numbers_pos_tr': 'Arriba derecha',
        'page_numbers_pos_ml': 'Medio izquierda',
        'page_numbers_pos_mc': 'Centrado',
        'page_numbers_pos_mr': 'Medio derecha',
        'page_numbers_pos_bl': 'Abajo izquierda',
        'page_numbers_pos_bc': 'Abajo centro',
        'page_numbers_pos_br': 'Abajo derecha',
        'page_numbers_margins': 'Márgenes:',
        'page_numbers_margin_x': 'Distancia horizontal:',
        'page_numbers_margin_y': 'Distancia vertical:',
        'page_numbers_range': 'Rango de páginas:',
        'page_numbers_all_pages': 'Todas las páginas',
        'page_numbers_custom_range': 'Rango personalizado',
        'page_numbers_from': 'Desde:',
        'page_numbers_to': 'Hasta:',
        'page_numbers_progress': 'Insertando números de página...',
        'page_numbers_start': 'Iniciando inserción de números de página...',
        'page_numbers_cancel': 'Inserción de números de página cancelada',
        'page_numbers_success': 'Los números de página se añadieron correctamente.\n\n¿Desea abrir el nuevo PDF?\n\n{0}',
        'page_numbers_complete': 'Números de página añadidos',
        'page_numbers_error_format': 'Error al insertar números de página: {0}',
        'page_numbers_content_type': 'Tipo de contenido:',
        'page_numbers_tab_simple': 'Número simple',
        'page_numbers_tab_range': 'Página X de Y',
        'page_numbers_tab_date': 'Fecha',
        'page_numbers_tab_custom': 'Texto libre',
        'page_numbers_range_format': 'Formato:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Página {aktuell} de {gesamt}',
        'page_numbers_range_custom': 'Personalizado',
        'page_numbers_range_placeholder': 'p.ej. "Página {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formato de fecha:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 de enero de 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Personalizado',
        'page_numbers_date_placeholder': 'p.ej. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posición:',
        'page_numbers_date_before': 'Fecha antes del número de página',
        'page_numbers_date_after': 'Fecha después del número de página',
        'page_numbers_date_only': 'Solo fecha (sin número de página)',
        'page_numbers_custom_text': 'Texto personalizado:',
        'page_numbers_custom_placeholder_text': 'Use {seite} para el número de página y {gesamt} para el total\np.ej. "Confidencial - Página {seite}" o "{seite} de {gesamt}"',
        "filename_with_page_number":"_con_numero_de_pagina",
        "filename_with_page_declaration":"_con_declaracion_de_pagina",
        "filename_with_pagenumber":"_con_numero_de_pagina",
        "filename_with_date":"_con_fecha",
        "filename_with_my_page_declaration":"_con_declaracion_personalizada",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Cambios sin guardar",
        "unsaved_changes_message_darkmode": "Hay inserciones sin guardar.\n¿Desea guardarlas antes de cambiar?",
        "save_and_switch": "Guardar y cambiar",
        "discard_and_switch": "Cambiar ahora",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exportar páginas como imágenes',
        'export_images_menu': 'Exportar como imágenes (PNG/JPEG)',
        'export_images_format': 'Formato de imagen:',
        'export_images_dpi': 'Resolución (DPI):',
        'export_images_quality': 'Calidad JPEG:',
        'export_images_range': 'Rango de páginas:',
        'export_images_all_pages': 'Todas las páginas',
        'export_images_custom_range': 'Rango personalizado',
        'export_images_from': 'Desde:',
        'export_images_to': 'Hasta:',
        'export_images_options': 'Opciones:',
        'export_images_single_files': 'Cada página como archivo separado',
        'export_images_subfolder': 'Exportar a subcarpeta',
        'export_images_subfolder_info': 'A subcarpeta "nombrePDF_imagenes"',
        'export_images_same_folder': 'En la misma carpeta que el PDF',
        'export_images_apply_darkmode': 'Aplicar configuración de PDFDarkView (Modo oscuro)',
        'export_images_target_folder': 'Carpeta de destino:',
        'export_images_browse': 'Examinar...',
        'export_images_preview': 'Vista previa:',
        'export_images_preview_info': 'Seleccione la configuración para la exportación',
        'export_images_preview_info_detail': '{0} páginas como {1}\nResolución: {2} DPI\nNombre de archivo: {3}\n{4}',
        'export_images_select_folder': 'Seleccionar carpeta de destino',
        'export_images_start': 'Iniciando exportación de imágenes...',
        'export_images_progress': 'Exportando imágenes...',
        'export_images_saving': 'Guardando página {0} de {1}...',
        'export_images_success': '¡Exportación exitosa!\n\n{0} imágenes se guardaron en:\n{1}',
        'export_images_complete': 'Exportación de imágenes completada',
        'export_images_open_folder': '📁 Abrir carpeta',
        'export_images_cancel': 'Exportación de imágenes cancelada',
        'export_images_error_format': 'Error al exportar imágenes: {0}',
        'export_images_pdf2image_missing': 'La biblioteca "pdf2image" no está instalada.\n\nPor favor, instálela con:\npip install pdf2image\n\nPara Windows también necesita Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Conversión PDF/A para archivado a largo plazo',
        'pdfa_menu': 'Conversión PDF/A (apto para archivo)',
        'pdfa_info': 'Convierte el PDF al formato PDF/A.\n\nPDF/A está diseñado específicamente para el archivado a largo plazo y garantiza que el documento se muestre correctamente en el futuro.',
        'pdfa_standard': 'Estándar PDF/A:',
        'pdfa_standard_select': 'Versión:',
        'pdfa_1': 'PDF/A-1 (simple, ampliamente compatible)',
        'pdfa_2': 'PDF/A-2 (moderno, mejor compresión)',
        'pdfa_3': 'PDF/A-3 (versión más reciente, permite archivos adjuntos)',
        'pdfa_standards_explanation': '📖 Explicación de los estándares:\n\n'
            '• PDF/A-1: Básico, compatible con sistemas antiguos (aprox. 2005)\n'
            '• PDF/A-2: Más moderno, mejor compresión, soporte de transparencia (aprox. 2011)\n'
            '• PDF/A-3: Versión más reciente, permite incrustar archivos adjuntos (aprox. 2013)\n\n'
            'Recomendación: PDF/A-2 es un buen compromiso entre compatibilidad y funciones modernas.',
        'pdfa_options': 'Opciones:',
        'pdfa_compress_enable': 'Comprimir PDF (archivo más pequeño)',
        'pdfa_metadata_preserve': 'Conservar metadatos (título, autor, etc.)',
        'pdfa_target_folder': 'Carpeta de destino:',
        'pdfa_browse': 'Examinar...',
        'pdfa_select_folder': 'Seleccionar carpeta de destino',
        'pdfa_ocr_info_unknown': '🔍 No se pudo verificar el contenido del texto.',
        'pdfa_ocr_info_not_needed': '✅ Texto disponible - OCR no es necesario.\nSe puede crear PDF/A directamente.',
        'pdfa_ocr_info_recommended': '⚠️ No se encontró suficiente texto.\n\nPara PDFs buscables, recomendamos ejecutar OCR primero.\nNota: PDF/A también funciona sin OCR - pero el texto no será buscable.',
        'pdfa_ocr_info_error': '❌ Error al verificar: {0}',
        'pdfa_start': 'Iniciando conversión PDF/A...',
        'pdfa_progress': 'Conversión PDF/A en curso...',
        'pdfa_success': '¡Conversión PDF/A exitosa!\n\nGuardado como:\n{0}\n\n¿Desea abrir el nuevo PDF?',
        'pdfa_complete': 'Conversión PDF/A completada',
        'pdfa_cancel': 'Conversión PDF/A cancelada',
        'pdfa_error_format': 'Error durante la conversión PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'La biblioteca "ocrmypdf" no está instalada.\n\nPor favor, instálela con:\npip install ocrmypdf',
        'btn_convert': 'Convertir',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimizar PDF (reducir tamaño de archivo)',
        'optimize_menu': 'Optimizar PDF (tamaño de archivo)',
        'optimize_info': 'Reduce el tamaño del archivo PDF mediante varios métodos de optimización.\n\nCuanto mayor sea el nivel de compresión, más pequeño será el archivo - con posible pérdida de calidad en las imágenes.',
        'optimize_level': 'Nivel de compresión:',
        'optimize_level_low': 'Bajo (rápido, poco ahorro)',
        'optimize_level_medium': 'Medio (buen compromiso)',
        'optimize_level_high': 'Alto (gran ahorro)',
        'optimize_level_maximum': 'Máximo (ahorro máximo, lento)',
        'optimize_level_explanation': 'Recomendación: "Medio" es un buen compromiso entre velocidad y tamaño de archivo.',
        'optimize_options': 'Opciones:',
        'optimize_compress_images': 'Comprimir imágenes (reducir calidad JPEG)',
        'optimize_clean_objects': 'Eliminar objetos no utilizados',
        'optimize_preserve_metadata': 'Conservar metadatos (título, autor, etc.)',
        'optimize_image_quality': 'Calidad de imagen:',
        'optimize_range': 'Rango de páginas:',
        'optimize_all_pages': 'Todas las páginas',
        'optimize_custom_range': 'Rango personalizado',
        'optimize_from': 'Desde:',
        'optimize_to': 'Hasta:',
        'optimize_target_folder': 'Carpeta de destino:',
        'optimize_browse': 'Examinar...',
        'optimize_select_folder': 'Seleccionar carpeta de destino',
        'optimize_info_box': 'Información',
        'optimize_info_text': 'La optimización puede tardar varios minutos en PDFs grandes.\n\nLas imágenes se guardan con calidad reducida, lo que puede reducir significativamente el tamaño del archivo.',
        'optimize_start': 'Iniciando optimización PDF...',
        'optimize_progress': 'Optimizando PDF...',
        'optimize_cancel': 'Optimización PDF cancelada',
        'optimize_complete': 'Optimización PDF completada',
        'optimize_error_format': 'Error durante la optimización PDF:\n\n{0}',
        'optimize_success_message': '¡Optimización PDF exitosa!\n\nGuardado como:\n{0}\n\nAntes: {1}\nDespués: {2}\nAhorro: {3:.1f}%\n\n{4}\n\n¿Desea abrir el PDF optimizado?',
        'optimize_success_message_no_size': '¡Optimización PDF exitosa!\n\nGuardado como:\n{0}\n\nInformación de tamaño no disponible.\n\n¿Desea abrir el PDF optimizado?',
        'optimize_result_positive': 'El archivo se redujo un {0:.1f}%.',
        'optimize_result_zero': 'Sin cambios en el tamaño del archivo.',
        'optimize_result_negative': 'El archivo aumentó un {0:.1f}%.\nSe omitió la optimización, se conservó el archivo original.',
        'btn_optimize': 'Iniciar optimización',
        'filename_optimize_low_suffix': '_optimizado_bajo',
        'filename_optimize_medium_suffix': '_optimizado',
        'filename_optimize_high_suffix': '_optimizado_alto',
        'filename_optimize_maximum_suffix': '_optimizado_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Recortar PDF',
        'crop_menu': 'Recortar PDF (Crop)',
        'crop_range': 'Aplicar a:',
        'crop_all_pages': 'Todas las páginas',
        'crop_current_page': 'Solo página actual',
        'crop_values': 'Valores de recorte (en puntos):',
        'crop_left': 'Izquierda:',
        'crop_right': 'Derecha:',
        'crop_top': 'Arriba:',
        'crop_bottom': 'Abajo:',
        'crop_presets': 'Preconfiguraciones:',
        'crop_preset_white': 'Detectar márgenes blancos',
        'crop_reset': 'Restablecer',
        'crop_mouse_hint': '🖱️ Arrastre un rectángulo para seleccionar aproximadamente el área.\nLuego puede ajustar los valores con precisión en los SpinBoxes.\nNo es posible el ajuste manual con el ratón.',
        'crop_apply': 'Recortar',
        'crop_scope_all': 'Todas las páginas',
        'crop_scope_current': 'Página actual',
        'crop_new_size': 'Nuevo tamaño: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'No se ha cargado ningún PDF',
        'crop_preview_error': 'Error al cargar la vista previa',
        'crop_start': 'Iniciando recorte...',
        'crop_progress': 'Recortando PDF...',
        'crop_success': '¡PDF recortado correctamente!\n\nGuardado como:\n{0}\n\n¿Desea abrir el PDF recortado?',
        'crop_complete': 'Recorte completado',
        'crop_cancel': 'Recorte cancelado',
        'crop_error_format': 'Error al recortar:\n\n{0}',
        'filename_crop_suffix': '_recortado',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Aplanar PDF (Flatten)',
        'flatten_menu': 'Aplanar PDF (Flatten)',
        'flatten_info': 'Aplanar un PDF "quema" todos los elementos editables en el contenido de la página.\n\nDespués, los campos de formulario, anotaciones, textos, cruces, firmas, imágenes y formas ya no se pueden editar individualmente.',
        'flatten_explanation_title': '📖 ¿Para qué sirve esto?',
        'flatten_explanation_text': 'El aplanamiento es necesario en las siguientes situaciones:\n\n'
            '• 📄 Desea preparar el documento para la impresión\n'
            '• 🔒 Desea evitar que alguien modifique los campos de formulario\n'
            '• 📎 Desea "incrustar" anotaciones y comentarios de forma permanente en el documento\n'
            '• 🖼️ Desea anclar permanentemente textos, cruces, firmas, imágenes y formas en el documento\n'
            '• 📦 Desea preparar el archivo para el archivado\n\n'
            'El aplanamiento hace que el PDF sea más pequeño y evita que los elementos se muevan o eliminen accidentalmente.',
        'flatten_what_title': '¿Qué se aplana?',
        'flatten_what_list': '• ✅ Campos de formulario (campos de texto, casillas de verificación, botones)\n'
            '• ✅ Anotaciones (comentarios, resaltados, notas)\n'
            '• ✅ Superposiciones (textos, cruces, firmas, imágenes, formas)',
        'flatten_options': 'Opciones:',
        'flatten_forms': 'Aplanar campos de formulario',
        'flatten_annotations': 'Aplanar anotaciones',
        'flatten_overlays': 'Aplanar superposiciones (textos, cruces, firmas, imágenes, formas)',
        'flatten_target_folder': 'Carpeta de destino:',
        'flatten_browse': 'Examinar...',
        'flatten_select_folder': 'Seleccionar carpeta de destino',
        'flatten_warning': '⚠️ Importante: ¡El aplanamiento es un proceso irreversible!\n\nDespués del aplanamiento, los elementos editables ya no se pueden cambiar ni eliminar individualmente.\nCree una copia de seguridad de antemano si es necesario.',
        'flatten_apply': 'Aplanar',
        'flatten_start': 'Iniciando aplanamiento...',
        'flatten_progress': 'Aplanando PDF...',
        'flatten_success': '¡PDF aplanado correctamente!\n\nGuardado como:\n{0}\n\n¿Desea abrir el PDF aplanado?',
        'flatten_complete': 'Aplanamiento completado',
        'flatten_cancel': 'Aplanamiento cancelado',
        'flatten_error_format': 'Error al aplanar:\n\n{0}',
        'filename_flatten_suffix': '_aplanado',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Superponer PDF (Overlay)',
        'overlay_menu': 'Superponer PDF (Overlay)',
        'overlay_info': 'Coloca un PDF (superposición) sobre otro PDF.\n\nEl PDF de superposición se coloca sobre el PDF base. Esto es útil para marcas de agua, logotipos, membretes o sellos.',
        'overlay_explanation_title': '📖 ¿Para qué sirve esto?',
        'overlay_explanation_text': 'La superposición es necesaria en las siguientes situaciones:\n\n'
            '• 🏢 Colocar un logotipo de empresa como marca de agua en cada página\n'
            '• 📄 Colocar un membretes en un PDF vacío\n'
            '• 🖊️ Colocar una superposición de sello en un documento\n'
            '• 🔖 Colocar una marca de agua en todas las páginas\n'
            '• 📑 Colocar una superposición de formulario en una plantilla',
        'overlay_type': 'Tipo de superposición:',
        'overlay_type_fullpage': 'Página completa (cubriente)',
        'overlay_type_transparent': 'Página completa (transparente - recomendado)',
        'overlay_type_stamp': 'Sello (posicionable)',
        'overlay_type_info_fullpage': '📄 El PDF de superposición se coloca exactamente sobre toda la página.\nEl fondo blanco se puede eliminar para que solo el contenido sea visible.',
        'overlay_type_info_transparent': '🔍 El PDF de superposición se coloca sobre toda la página con fondo transparente.\nEl fondo blanco se elimina automáticamente - ¡ideal para marcas de agua y logotipos!',
        'overlay_type_info_stamp': '🖊️ El PDF de superposición se posiciona y escala como un sello.\nPerfecto para logotipos, sellos o firmas en posiciones específicas.',
        'overlay_remove_background': 'Eliminar fondo blanco:',
        'overlay_remove_background_enable': 'Eliminar el fondo blanco del PDF de superposición (hace que la superposición sea transparente)',
        'overlay_remove_background_tooltip': 'Elimina las áreas blancas del PDF de superposición para que el texto subyacente sea visible.',
        'overlay_threshold': 'Valor umbral:',
        'overlay_threshold_hint': '(1-254, más alto = se elimina más blanco)',
        'overlay_select_file': 'Seleccionar PDF de superposición:',
        'overlay_file_placeholder': 'Por favor, seleccione un archivo PDF para la superposición',
        'overlay_browse': 'Examinar...',
        'overlay_select_overlay': 'Seleccionar PDF de superposición',
        'overlay_range': 'Rango de páginas:',
        'overlay_all_pages': 'Todas las páginas',
        'overlay_custom_range': 'Rango personalizado',
        'overlay_from': 'Desde:',
        'overlay_to': 'Hasta:',
        'overlay_position': 'Posición:',
        'overlay_position_center': 'Centro',
        'overlay_position_top_left': 'Arriba izquierda',
        'overlay_position_top_right': 'Arriba derecha',
        'overlay_position_bottom_left': 'Abajo izquierda',
        'overlay_position_bottom_right': 'Abajo derecha',
        'overlay_size': 'Tamaño:',
        'overlay_size_original': 'Tamaño original',
        'overlay_size_fit_page': 'Ajustar a la página',
        'overlay_size_custom': 'Personalizado (%)',
        'overlay_opacity': 'Transparencia:',
        'overlay_target_folder': 'Carpeta de destino:',
        'overlay_browse_folder': 'Examinar...',
        'overlay_select_folder': 'Seleccionar carpeta de destino',
        'overlay_warning': '⚠️ Nota: El PDF de superposición se coloca sobre el PDF base y se "quema" en él.\n\nLos elementos del PDF de superposición ya no se pueden editar individualmente después de guardar.',
        'overlay_apply': 'Superponer',
        'overlay_start': 'Iniciando superposición...',
        'overlay_progress': 'Superponiendo PDF...',
        'overlay_success': '¡PDF superpuesto correctamente!\n\nGuardado como:\n{0}\n\n¿Desea abrir el PDF superpuesto?',
        'overlay_complete': 'Superposición completada',
        'overlay_cancel': 'Superposición cancelada',
        'overlay_error_format': 'Error al superponer:\n\n{0}',
        'overlay_no_file': 'No se seleccionó ningún PDF de superposición.\n\nPor favor, seleccione un archivo PDF para superponer.',
        'filename_overlay_suffix': '_superpuesto',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extraer imágenes del PDF',
        'extract_images_menu': 'Extraer todas las imágenes',
        'extract_images_info': 'Extrae todas las imágenes del PDF y las guarda como archivos separados.\n\nLas imágenes se guardan en su formato original o se convierten a un formato seleccionado.',
        'extract_images_format': 'Formato de imagen:',
        'extract_images_quality': 'Calidad JPEG:',
        'extract_images_options': 'Opciones:',
        'extract_images_subfolder': 'Extraer a subcarpeta ("nombrePDF_imagenes")',
        'extract_images_unique': 'Solo imágenes únicas (evitar duplicados)',
        'extract_images_range': 'Rango de páginas:',
        'extract_images_all_pages': 'Todas las páginas',
        'extract_images_custom_range': 'Rango personalizado',
        'extract_images_from': 'Desde:',
        'extract_images_to': 'Hasta:',
        'extract_images_target_folder': 'Carpeta de destino:',
        'extract_images_browse': 'Examinar...',
        'extract_images_select_folder': 'Seleccionar carpeta de destino',
        'extract_images_info_box': 'Información',
        'extract_images_info_text': 'La extracción puede tardar varios minutos en PDFs grandes.\n\nLas imágenes se guardan con su nombre original (página_imagen).',
        'extract_images_extract': 'Extraer',
        'extract_images_start': 'Iniciando extracción...',
        'extract_images_progress': 'Extrayendo imágenes...',
        'extract_images_success': '✅ ¡Imágenes extraídas correctamente!\n\n{0} imágenes se guardaron en:\n{1}',
        'extract_images_complete': 'Extracción de imágenes completada',
        'extract_images_cancel': 'Extracción cancelada',
        'extract_images_error_format': 'Error al extraer imágenes:\n\n{0}',
        'extract_images_open_folder': '📁 Abrir carpeta',
        'extract_images_no_images': 'No se encontraron imágenes en el PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Múltiples páginas en una página (N-Up)',
        'nup_menu': 'Múltiples páginas en una página (N-Up)',
        'nup_info': 'Organiza varias páginas PDF en una página.\n\nIdeal para impresiones compactas, resúmenes o folletos.',
        'nup_layout': 'Diseño:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Vista previa:',
        'nup_preview_info': '{0} páginas → {1} páginas por hoja → {2} hojas\nDiseño: {3}',
        'nup_order': 'Orden:',
        'nup_order_horizontal': 'Horizontal (fila por fila)',
        'nup_order_vertical': 'Vertical (columna por columna)',
        'nup_order_horizontal_reverse': 'Horizontal inverso',
        'nup_order_vertical_reverse': 'Vertical inverso',
        'nup_range': 'Rango de páginas:',
        'nup_all_pages': 'Todas las páginas',
        'nup_custom_range': 'Rango personalizado',
        'nup_from': 'Desde:',
        'nup_to': 'Hasta:',
        'nup_options': 'Opciones:',
        'nup_margins': 'Márgenes:',
        'nup_margin_between': 'Distancia entre páginas:',
        'nup_page_numbers': 'Insertar números de página',
        'nup_target_folder': 'Carpeta de destino:',
        'nup_browse': 'Examinar...',
        'nup_select_folder': 'Seleccionar carpeta de destino',
        'nup_create': 'Crear',
        'nup_start': 'Iniciando N-Up...',
        'nup_progress': 'Creando N-Up...',
        'nup_success': '¡N-Up creado correctamente!\n\nGuardado como:\n{0}\n\n¿Desea abrir el nuevo PDF?',
        'nup_complete': 'N-Up completado',
        'nup_cancel': 'N-Up cancelado',
        'nup_error_format': 'Error durante N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Cambiar tamaño de página',
        'pagesize_menu': 'Cambiar tamaño de página',
        'pagesize_info': 'Cambia el tamaño de página del PDF.\n\nEl contenido se adapta automáticamente al nuevo tamaño.',
        'pagesize_format': 'Formato:',
        'pagesize_select': 'Seleccione un formato estándar:',
        'pagesize_custom': 'Tamaño personalizado:',
        'pagesize_width': 'Ancho:',
        'pagesize_height': 'Alto:',
        'pagesize_orientation': 'Orientación:',
        'pagesize_portrait': 'Vertical',
        'pagesize_landscape': 'Horizontal',
        'pagesize_scale_options': 'Opciones de escala:',
        'pagesize_fit': 'Ajustar (mantener relación de aspecto)',
        'pagesize_stretch': 'Estirar (distorsionar)',
        'pagesize_center': 'Centrar (tamaño original)',
        'pagesize_range': 'Rango de páginas:',
        'pagesize_all_pages': 'Todas las páginas',
        'pagesize_custom_range': 'Rango personalizado',
        'pagesize_from': 'Desde:',
        'pagesize_to': 'Hasta:',
        'pagesize_target_folder': 'Carpeta de destino:',
        'pagesize_browse': 'Examinar...',
        'pagesize_select_folder': 'Seleccionar carpeta de destino',
        'pagesize_apply': 'Aplicar',
        'pagesize_start': 'Iniciando cambio de tamaño de página...',
        'pagesize_progress': 'Cambiando tamaño de página...',
        'pagesize_success': '¡Tamaño de página cambiado correctamente!\n\nGuardado como:\n{0}\n\n¿Desea abrir el nuevo PDF?',
        'pagesize_complete': 'Cambio de tamaño de página completado',
        'pagesize_cancel': 'Cambio de tamaño de página cancelado',
        'pagesize_error_format': 'Error al cambiar el tamaño de página:\n\n{0}',
        'pagesize_preview_info': 'Nuevo tamaño: {0} x {1} pt',
        'filename_pagesize_suffix': '_nuevo_tamano',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Información del PDF',
        'pdf_info_menu': 'Mostrar información del PDF',
        'pdf_info_voice': 'Mostrando información del PDF',
        'pdf_info_error': 'Error al mostrar la información del PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Mostrar atajos de teclado",
        "shortcuts_dialog_title": "Atajos de teclado",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 ARCHIVO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Abrir PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Cerrar PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Guardar como...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Proteger documento</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Imprimir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Imprimir directamente (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Salir de la aplicación</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORTAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportar como Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportar como DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportar como TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportar como imágenes (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extraer imágenes</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PROCESAMIENTO DE DOCUMENTOS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Múltiples páginas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Conversión PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Aplanar PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Superponer PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimizar PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDITAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Buscar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Añadir marcador</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Gestionar marcadores</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Siguiente marcador</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Marcador anterior</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Ejecutar OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 GESTIÓN DE PÁGINAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rotar página actual</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rotar todas las páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizar página actual</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizar todas las páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Eliminar páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extraer páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Insertar páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Mover páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Combinar PDFs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Cambiar tamaño de página</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INSERTAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Insertar texto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Insertar cruz</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Insertar firma 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Insertar firma 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Insertar imagen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Insertar rectángulo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Insertar elipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Insertar línea</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Insertar flecha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Insertar números de página</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Marca de agua de texto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Marca de agua de imagen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDACCIONES</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redacción (negro)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redacción (blanco)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Aplicar todas las redacciones</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANZADO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Recortar PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Editar metadatos</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Alternar modo Oscuro/Claro</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Mostrar ventana de texto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Ancho de página (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dos páginas (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Vista general (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ CONFIGURACIÓN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Gestión de contraseñas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Configuración de OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Configuración de firma</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formato de nombres de archivo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exportar configuración</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importar configuración</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACIÓN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Mostrar información del PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Activar/desactivar salida de voz</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Enfocar barra de menús</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nueva versión disponible",
        "update_available_message": "Hay una nueva versión <b>{0}</b>.\n\nVisite la página de lanzamiento para descargar la actualización:\n{1}",
        "update_available_voice": "Nueva versión {0} disponible. Descargue la actualización desde la página de GitHub.",
        "update_open_release": "Abrir página de lanzamiento",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Descargar todas las traducciones",
        "ask_download_all_translations": """Además del alemán, inglés y vietnamita, hay {total_languages} idiomas de interfaz más disponibles.\n\n¿Deben proporcionarse / actualizarse?\n\nNota:\nLos idiomas no necesarios se pueden eliminar más tarde manualmente en el directorio:\n{translations_path}
        \nSi cancela, puede descargar los idiomas de interfaz más tarde a través del menú 'Herramientas → Actualizar traducciones'.""",
        "menu_update_translations": "Actualizar traducciones",
        "translations_updated": "Traducciones actualizadas",
        "translations_update_success": "{} traducciones se actualizaron correctamente ({} nuevas, {} actualizadas).",
        "translations_update_error": "Error al actualizar las traducciones",
        "translations_update_no_changes": "Todas las traducciones ya están actualizadas.",
        "translations_update_offline": "Sin conexión a Internet. No se pudieron actualizar las traducciones.",
        "translations_update_in_progress": "Las traducciones se están actualizando en segundo plano...",
        "translations_downloading": "Descargando traducciones...",
        "translations_path_hint": "Directorio de usuario para traducciones",
        "translations_update_not_available_title": "Actualización no disponible",
        "translations_update_not_available_message": """La actualización de traducciones solo está disponible en la versión instalada.\n\nEn modo de desarrollo, las traducciones ya están actualizadas.""",
        "translations_update_no_internet_title": "Sin conexión a Internet",
        "translations_update_no_internet_message": """No se pudo establecer conexión a Internet.\n\nLas traducciones no se pueden descargar desde GitHub.\n\nPosibles soluciones:
        • Verifique su conexión a Internet
        • Desactive temporalmente cualquier cortafuegos
        • Inténtelo de nuevo más tarde
        \nTambién puede descargar las traducciones manualmente desde GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "La actualización ya está en curso",
        "btn_retry": "Reintentar",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Bienvenido a PDF Dark View",
        "welcome_title_not_supported": "Bienvenido a PDF Dark View",
        "welcome_message": "Bienvenido a PDF Dark View!\n\nSu idioma del sistema fue detectado como '{language}'.\n¿Desea usar este idioma para la interfaz de usuario?\n\nPuede cambiar el idioma en cualquier momento a través de 'Configuración → Idioma'.",
        "welcome_message_language_not_available": "Bienvenido a PDF Dark View!\n\nSu idioma del sistema fue detectado como '{language}'.\nEste idioma aún no está instalado.\n\n¿Desea descargar ahora las traducciones para {language} desde GitHub?\n\n(El idioma se usará automáticamente para la interfaz de usuario.)",
        "welcome_message_language_not_supported": "Bienvenido a PDF Dark View!\n\nSu idioma del sistema fue detectado como '{language}'.\nLamentablemente, aún no hay traducciones para este idioma.\n\nLa interfaz de usuario se mostrará en {fallback_language}.\n\nPuede cambiar el idioma en cualquier momento a través de 'Configuración → Idioma'.\nSi lo desea, también puede contribuir con una traducción para su idioma:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Sí, usar idioma del sistema",
        "welcome_keep_english": "No, mantener inglés",
        "welcome_download_language": "Sí, descargar {language}",

        # ============================================
        # 107. RUTAS RECIENTES
        # ============================================

        'menu_recent': 'Usado recientemente',
        'menu_recent_dirs': 'Directorios...',
        'menu_recent_files': 'Archivos...',
        'recent_manage': 'Administrar...',
        'recent_enable_tracking': 'Guardar rutas recientes (privacidad)',
        'recent_enable_info': 'Desactive esta opción para no guardar rutas',
        'recent_tracking_disabled': 'Seguimiento de rutas desactivado',
        'recent_enabled': 'activado',
        'recent_disabled': 'desactivado',
        'recent_tracking_status': 'Seguimiento de rutas {0}',
        'recent_dialog_title': 'Rutas recientes',
        'recent_tab_directories': 'Directorios',
        'recent_tab_files': 'Archivos',
        'recent_dirs_instruction': 'Doble clic para abrir el diálogo de archivo en el directorio',
        'recent_files_instruction': 'Doble clic para abrir el PDF directamente',
        'recent_no_directories': '(no hay directorios guardados)',
        'recent_no_files': '(no hay archivos guardados)',
        'recent_default_current': '⭐ Predeterminado: {0}',
        'recent_set_as_default': '⭐ Establecer como predeterminado',
        'recent_default_set_title': 'Directorio predeterminado establecido',
        'recent_default_set_message': 'El directorio "{0}" se ha establecido como predeterminado para abrir PDF.',
        'recent_default_set_voice': 'Directorio predeterminado establecido',
        'recent_directory_not_found': 'Directorio no encontrado',
        'recent_file_not_found': 'Archivo no encontrado',
        'recent_remove_selected': 'Eliminar',
        'recent_remove_title': 'Eliminar ruta',
        'recent_remove_confirm': '¿Realmente desea eliminar la ruta "{0}" de la lista?',
        'recent_path_removed': 'Ruta eliminada',
        'recent_clear_all': 'Eliminar todo',
        'recent_clear_title': 'Eliminar todas las rutas',
        'recent_clear_confirm_type': '¿Realmente desea eliminar todos los {0}?',
        'recent_cleared': 'Lista borrada',
        'recent_path_not_found_title': 'Ruta no encontrada',
        'recent_path_not_found_message': 'La ruta "{0}" ya no existe.',
        'recent_open_file': 'Abrir archivo',
        'btn_open_recent': 'Abrir',
        'recent_open_file_question': '¿Desea abrir "{0}" como PDF?',
        'recent_not_pdf': 'El archivo seleccionado no es un PDF.',
        'recent_more_entries': 'Más entradas...',
        'btn_remove': 'Eliminar',
        'btn_clear': 'Borrar todo',
        'recent_context_open': 'Abrir',
        'recent_context_reveal': 'Mostrar en Finder',
        'recent_context_set_default': '⭐ Establecer como predeterminado',
        'recent_context_open_terminal': '💻 Abrir terminal',
        'recent_context_file_info': 'Información del archivo',
        'recent_context_open_with_default': '📄 Abrir con la aplicación predeterminada',
        'recent_context_remove': 'Eliminar de la lista',
        'recent_context_clear_all': 'Eliminar todo',
        'recent_file_info_title': 'Información del archivo',
        'recent_file_info_name': 'Nombre',
        'recent_file_info_path': 'Ruta',
        'recent_file_info_size': 'Tamaño',
        'recent_file_info_modified': 'Modificado',
        'recent_file_info_pages': 'Páginas',
        'recent_error_reveal': 'Error al abrir en Finder',
        'recent_error_terminal': 'Error al abrir la terminal',
        'recent_error_info': 'Error al obtener información del archivo',
        'open_user_data_folder': 'Mostrar directorio de datos del usuario',

        # ============================================
        # 108. ELIMINAR PÁGINAS PARES/IMPARES
        # ============================================
        "pages_delete_even": "Eliminar todas las páginas pares",
        "pages_delete_odd":  "Eliminar todas las páginas impares",
        "progress_even_pages": "Eliminando páginas pares",
        "progress_odd_pages": "Eliminando páginas impares",
        "progress_mark_delete_even": "{} página(s) par(es) marcada(s) para eliminar",
        "progress_mark_delete_odd":  "{} página(s) impar(es) marcada(s) para eliminar",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "El programa se está cerrando",

    }
