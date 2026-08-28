
# ============================================
# translations_pt.py - Dicionário português
# Completamente ordenado por categorias
# Comentários em alemão para consistência
# ============================================

def load_portuguese_strings():
    """Carrega todas as strings em português"""

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
        'btn_first': "Primeira página",
        'btn_prev': "Página anterior",
        'btn_next': "Página seguinte",
        'btn_last': "Última página",
        'btn_print': "Imprimir",
        'btn_darkmode_light': "Modo claro",
        'btn_darkmode_dark': "Modo escuro",
        'btn_delete_pages': "Eliminar páginas",
        'btn_extract_pages': "Extrair páginas",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Cancelar",
        'btn_save': "Guardar",
        'btn_close': "Fechar",
        'btn_delete': "Eliminar",
        'btn_delete_all': "Eliminar tudo",
        'btn_copy': "Copiar",
        'btn_export': "Exportar",
        'btn_show': "Mostrar palavra‑passe",
        'btn_hide': "Ocultar palavra‑passe",
        'btn_authenticate': "Autenticar",
        'btn_settings': "Configurações",
        'btn_protect': "Proteger",
        'btn_remove_password': "Remover palavra‑passe",
        'btn_manage': "Gestor de palavras‑passe",
        'btn_retry': "Tentar novamente",
        'btn_select_all': "Selecionar tudo",
        'btn_clear_selection': "Limpar seleção",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Página {0} de {1}",
        'page_count': "de {0}",
        'goto_page': "Ir para a página",
        'page_simple': "Página {0}",
        'full_view_page': "Vista completa página {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Introduzir termo + Enter",
        'search_results': "Resultados: {0} de {1}",
        'search_nav_hint': "Enter: próximo  (Shift+Enter: anterior)",
        'search_no_results': "Sem resultados",
        'search_error': "Erro de pesquisa",
        'search_active': "Campo de pesquisa ativado",
        'search_closed': "Pesquisa encerrada",
        'search_position': "Página {0} {1}",
        'search_pos_top': "no topo",
        'search_pos_upper': "acima",
        'search_pos_middle': "meio",
        'search_pos_lower': "abaixo",
        'search_pos_bottom': "no fundo",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Reconhecimento de texto concluído com sucesso!",
        'ocr_success_title': "OCR bem‑sucedido",
        'ocr_success_message': "O documento agora é pesquisável.",
        'ocr_failed': "Falha no OCR",
        'ocr_in_progress': "OCR em curso",
        'ocr_preparing': "A preparar PDF...",
        'ocr_analyzing': "A analisar PDF...",
        'ocr_optimizing': "Otimização de imagem...",
        'ocr_recognizing': "Reconhecimento de texto...",
        'ocr_embedding': "A incorporar texto...",
        'ocr_finalizing': "A finalizar PDF...",
        'ocr_not_available': "OCR não disponível",
        'ocr_install_message': "Ferramentas OCR não encontradas.\n\nPor favor, instale:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR necessário",
        'ocr_question': "O PDF não contém texto pesquisável.\nDeseja executar OCR para permitir {0}?",
        'ocr_perform': "Executar OCR",
        'ocr_later': "Mais tarde",
        'ocr_starting': "A iniciar OCR garantido...",
        'ocr_success_voice': "OCR bem‑sucedido. O PDF agora é pesquisável.",
        'ocr_partial_success': "OCR foi executado, mas houve problemas durante a substituição.\n\nA versão pesquisável foi guardada em:\n{0}\n\nErro: {1}",
        'ocr_partial_title': "OCR parcialmente bem‑sucedido",
        'ocr_partial_voice': "OCR executado, mas substituição falhou.",
        'original_file': "Ficheiro original:",
        'old_size': "Tamanho antigo:    {0} bytes",
        'new_size': "Novo tamanho: {0} bytes",
        'size_change': "Alteração: {0}{1} bytes",
        'backup_created_file': "Cópia de segurança criada:\n{0}",
        'backup_not_created': "Cópia de segurança: não criada (configuração desativada)",
        'page_header': "=== Página {0} ===\n{1}\n",
        'scanned_page_header': "=== Página {0} (digitalizada) ===\n[Esta página contém apenas texto digitalizado]\n[Por favor, execute OCR manualmente]\n",
        'scanned_warning': "⚠️ TEXTO DIGITALIZADO - OCR NECESSÁRIO",
        'guaranteed_title': "PDF pesquisável criado",
        'guaranteed_message': "<b>Versão pesquisável garantida criada!</b>\n\nComo o OCR automático falhou, foi criado um PDF alternativo pesquisável:\n\n{0}\n\n<b>Este ficheiro contém:</b>\n• Texto extraído (se disponível)\n• Indicações para páginas digitalizadas\n• É totalmente pesquisável",
        'guaranteed_voice': "PDF pesquisável garantido criado.",
        'instruction_title': "INSTRUÇÕES PARA OCR",
        'instruction_file': "Ficheiro original: {0}",
        'instruction_text': "O reconhecimento automático de texto (OCR) falhou.\nPor favor, execute OCR manualmente:\n\n1. COM OCRmyPDF (linha de comandos):\n   ocrmypdf --force-ocr \"[FICHEIRO]\" \"saida.pdf\"\n\n2. COM ADOBE ACROBAT (macOS/Windows):\n   • Abrir o PDF no Acrobat\n   • Ferramentas > Editar PDF\n   • Selecionar 'Reconhecer texto'\n\n3. COM VISUALIZAÇÃO (macOS):\n   • Abrir o PDF no Visualização\n   • Ficheiro > Exportar...\n   • Filtro Quartz: 'Reduzir tamanho do ficheiro'\n   • Ativar 'Executar OCR'\n\n4. SERVIÇOS ONLINE:\n   • smallpdf.com/pt/ocr-pdf\n   • ilovepdf.com/pt/ocr-pdf\n   • adobe.com/pt/acrobat/online/pdf-to-word.html",
        'instruction_created': "Instruções OCR criadas",
        'instruction_created_message': "Foram criadas instruções detalhadas:\n\n{0}\n\nSiga os passos para OCR manual.",
        'instruction_created_voice': "Instruções OCR criadas.",
        'ocr_impossible': "OCR impossível",
        'ocr_impossible_message': "Não foi possível executar OCR.\n\nPor favor, processe '{0}' manualmente com software OCR.",
        'ocr_impossible_voice': "OCR impossível. Processe manualmente.",
        'emergency_title': "OCR de emergência",
        'emergency_message': "Foi criado um PDF de emergência:\n\n{0}\n\nProcesse este ficheiro manualmente com OCR.",
        'emergency_voice': "PDF de emergência criado. Execute OCR manualmente.",
        'critical_error': "Erro crítico",
        'critical_error_message': "Não foi possível iniciar OCR.\n\nReinicie o programa e\nverifique a instalação do OCR.",
        'critical_error_voice': "Erro crítico de OCR",
        'ocr_question_html': "<p>O PDF não contém texto pesquisável.<p>Deseja executar OCR para permitir <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR necessário. O PDF não contém texto pesquisável. Deseja executar OCR para permitir {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "nenhum PDF carregado",
        'no_pdf_message': "Nenhum PDF está carregado",
        'pdf_not_found': "Ficheiro PDF não encontrado",
        'file_size': "Tamanho do ficheiro",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Cópia de segurança criada",
        'backup_disabled': "Cópia de segurança desativada",
        'backup_activated': "Criação de cópia de segurança ativada",
        'backup_deactivated': "Criação de cópia de segurança desativada",
        'backup_status': "Cópia de segurança: {0}",
        'backup_on': "✔ ativada",
        'backup_off': "✘ desativada",
        'close_pdf': "A fechar PDF: {0}",
        'pdf_not_found_format': "Ficheiro PDF não encontrado: {0}",
        'error_pdf_load_format': "Erro ao carregar o PDF: {0}",
        'load_failed_format': "Falha no carregamento:\n{0}",
        'decrypted_suffix': "(desencriptado)",
        'decryption_failed': "Desencriptação falhou.",
        'decryption_error': "Erro durante a desencriptação",
        'decryption_success': "Desencriptação bem‑sucedida",
        'decryption_success_message': "O PDF foi desencriptado e guardado em:\n\n{0}",
        'decryption_success_voice': "PDF desencriptado e guardado.",
        'password_remove_error': "Erro ao remover a palavra‑passe",
        'save_unencrypted': "Guardar PDF não encriptado como",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Guardar como...",
        'save_copy': "Guardar cópia",
        'save_success': "PDF guardado em: {0}",
        'save_encrypted': "PDF protegido guardado em: {0}",
        'save_error': "Não foi possível guardar o PDF",
        'encryption_question': "Deseja proteger o PDF com uma palavra‑passe?",
        'encryption_yes': "Sim",
        'encryption_no': "Não",
        'encryption_cancel': "Cancelar",
        'save_cancel': "Gravação cancelada",
        'save_encrypted_voice': "Ficheiro encriptado e guardado.",
        'save_success_voice': "O ficheiro PDF foi guardado não encriptado.",
        'save_error_format': "Não foi possível guardar o PDF:\n{0}",
        'export_pages_success': "Exportação para Pages bem‑sucedida",
        'export_pages_error': "Falha na exportação para Pages",
        'export_pages_error_format': "Falha na exportação para Pages: {0}",
        'export_word_success': "Exportação para Word bem‑sucedida",
        'export_word_error': "Falha na exportação para Word",
        'export_word_error_format': "Falha na exportação para Word: {0}",
        'export_text_success': "Exportação para texto bem‑sucedida",
        'export_text_error': "Falha na exportação para texto",
        'export_text_error_format': "Falha na exportação para texto: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Palavra‑passe necessária",
        'password_enter': "Por favor, introduza a palavra‑passe",
        'password_confirm': "Confirmar palavra‑passe",
        'password_new': "Nova palavra‑passe",
        'password_current': "Palavra‑passe atual",
        'password_save': "Guardar palavra‑passe (encriptada)",
        'password_saved': "✓ Palavra‑passe para este ficheiro guardada",
        'password_wrong': "Palavra‑passe errada",
        'password_mismatch': "As palavras‑passe não coincidem",
        'password_too_short': "Palavra‑passe demasiado curta",
        'password_min_length': "A palavra‑passe deve ter pelo menos 4 caracteres",
        'password_strength': "Força da palavra‑passe",
        'password_strength_very_weak': "Muito fraca",
        'password_strength_weak': "Fraca",
        'password_strength_medium': "Média",
        'password_strength_strong': "Forte",
        'password_strength_very_strong': "Muito forte",
        'password_char_count': "({0} caracteres)",
        'password_match': "✓ Coincidem",
        'password_no_match': "✗ As palavras‑passe não coincidem",
        'password_show': "Mostrar",
        'password_hide': "Ocultar",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Gestor de palavras‑passe",
        'password_table_filename': "Nome do ficheiro",
        'password_table_password': "Palavra‑passe",
        'password_count': "{0} palavra‑passe guardada{1}",
        # Português: 1 palavra‑passe guardada, 2 palavras‑passe guardadas -> usamos {1} para plural "s"
        'password_count_singular': "",
        'password_count_plural': "s",
        'password_none': "Nenhuma palavra‑passe guardada",
        'password_copied': "{0} palavra‑passe copiada{1}",
        'password_copied_singular': "",
        'password_copied_plural': "s",
        'password_delete_confirm': "Deseja realmente eliminar a palavra‑passe para '{0}'?",
        'password_delete_multiple': "Deseja realmente eliminar as {0} palavras‑passe selecionadas?",
        'password_delete_all_confirm': "Deseja realmente eliminar todas as {0} palavras‑passe guardadas?",
        'password_deleted': "{0} palavra‑passe eliminada{1}",
        'password_deleted_singular': "",
        'password_deleted_plural': "s",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "s",
        'password_all_deleted': "Todas as palavras‑passe foram eliminadas",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Gerador de palavras‑passe",
        'generator_generated': "Palavra‑passe gerada:",
        'generator_regenerate': "Regenerar",
        'generator_copy': "Copiar",
        'generator_use': "Usar",
        'generator_settings': "Configurações",
        'generator_length': "Comprimento:",
        'generator_group_every': "Separador a cada",
        'generator_group_chars': "caracteres.   Separador:",
        'generator_uppercase': "Maiúsculas (A-Z)",
        'generator_lowercase': "Minúsculas (a-z)",
        'generator_digits': "Dígitos (0-9)",
        'generator_symbols': "Símbolos (!@#$%^&*)",
        'generator_exclude': "Excluídos:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Palavra‑passe mestre necessária",
        'master_password_setup': "Configurar palavra‑passe mestre",
        'master_password_change': "Alterar palavra‑passe mestre",
        'master_password_enter': "Introduza a sua palavra‑passe mestre",
        'master_password_choose': "Escolha uma palavra‑passe mestre segura (pelo menos 8 caracteres)",
        'master_password_new': "Introduza a sua nova palavra‑passe mestre",
        'master_password_confirm': "Confirmar palavra‑passe",
        'master_password_authenticate': "Autenticar",
        'master_password_success': "Palavra‑passe mestre configurada com sucesso.",
        'master_password_changed': "Palavra‑passe mestre alterada com sucesso.",
        'master_password_removed': "Palavra‑passe mestre e todas as palavras‑passe eliminadas.",
        'master_password_remove': "Remover palavra‑passe mestre",
        'master_password_remove_confirm': "TEM A CERTEZA de que deseja eliminar TODAS as palavras‑passe?\n\nEsta ação é IRREVERSÍVEL!",
        'master_password_export_before': "Deseja exportar uma cópia de segurança primeiro?",
        'master_password_export_delete': "Exportar e eliminar",
        'master_password_delete_now': "Eliminar agora",
        'master_password_for_signatures': "Para usar assinaturas, precisa de configurar uma palavra‑passe mestre.\n\nDeseja configurar uma palavra‑passe mestre agora?",
        'master_password_for_private': "Para usar modelos de texto privados, precisa de configurar uma palavra‑passe mestre.\n\nDeseja configurar uma palavra‑passe mestre agora?",
        'master_password_info': """
            <b>🔐 SEM PALAVRA‑PASSE MESTRE:</b><br>
            • Não é possível ver, copiar ou exportar palavras‑passe<br>
            • A eliminação de palavras‑passe é sempre possível (mesmo sem palavra‑passe mestre)<br><br>

            <b>🔐 COM PALAVRA‑PASSE MESTRE:</b><br>
            • Todas as funções disponíveis após autenticação<br>
            • As palavras‑passe são encriptadas com a palavra‑passe mestre<br>
            • Comprimento mínimo: 8 caracteres<br>
            • Armazenamento seguro por hash SHA‑256<br><br>

            <b>IMPORTANTE:</b><br>
            • Em caso de perda da palavra‑passe mestre, as palavras‑passe não podem ser recuperadas<br>
            • Ao remover a palavra‑passe mestre, TODAS as palavras‑passe são eliminadas<br>
            • Opção de exportação disponível antes da eliminação<br>
            • A palavra‑passe mestre pode ser alterada a qualquer momento
        """,
        'signature_auth_disabled': "Desativar pedido de palavra‑passe para assinaturas",
        'template_auth_disabled': "Desativar pedido de palavra‑passe para modelos privados",
        'master_password_for_signatures_settings': "Para usar assinaturas, precisa de configurar uma palavra‑passe mestre.\n\nAceda a Configurações - Gestor de palavras‑passe",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Proteger PDF",
        'protect_info': "O ficheiro '{0}' será protegido com palavra‑passe.",
        'protect_instruction': "Introduza duas vezes a palavra‑passe desejada para proteger o documento, ou use o gerador de palavras‑passe à direita do campo de entrada.",
        'protect_success': "O PDF foi protegido com sucesso e guardado em:\n{0}\n\nPalavra‑passe: {1}\n\nDeseja abrir o PDF protegido agora?",
        'protect_open': "Sim",
        'protect_skip': "Não",
        'protect_error': "Erro ao proteger o PDF",
        'protect_open_title': "abrir PDF protegido",
        'protect_question': "Concluído. Deseja abrir o PDF protegido agora? Sim ou Não?",
        'password_cancel': "Diálogo de palavra‑passe cancelado",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Eliminar páginas",
        'pages_extract': "Extrair páginas",
        'pages_insert': "Inserir páginas",
        'pages_move': "Mover páginas",
        'pages_delete_options': "Opções de eliminação",
        'pages_delete_empty': "Eliminar todas as páginas vazias",
        'pages_delete_current': "Eliminar página atual",
        'pages_delete_range': "Eliminar intervalo de páginas",
        'pages_extract_options': "Opções de extração",
        'pages_extract_current': "Extrair página atual",
        'pages_extract_range': "Extrair intervalo de páginas",
        'pages_insert_position': "Posição de inserção",
        'pages_insert_before': "Inserir antes da página:",
        'pages_insert_select': "Selecionar PDF",
        'pages_insert_none': "Nenhum PDF selecionado",
        'pages_move_source': "Páginas a mover",
        'pages_move_from': "Da página:",
        'pages_move_to': "Até à página:",
        'pages_move_target': "Posição de destino",
        'pages_move_before': "Mover antes da página:",
        'pages_move_hint': "Nota: página 1 = início, {0} = fim",
        'pages_range_invalid': "A página inicial deve ser menor ou igual à página final.",
        'pages_position_invalid': "A posição de destino não deve estar dentro do intervalo a mover.",
        'pages_no_pdf_selected': "Nenhum PDF selecionado.",
        'pages_deleted': "{0} páginas foram eliminadas.",
        'pages_extracted': "Extraído: {0}\nGuardado em: {1}\nTamanho: {2:.1f} KB",
        'pages_inserted': "{0} páginas inseridas",
        'pages_moved': "{0} páginas foram movidas.",
        'pages_deleted_none': "Nenhuma página foi eliminada.",
        'pages_delete_progress': "A eliminar páginas...",
        'pages_deleted_with_backup': "{0} páginas foram eliminadas.\n\nCópia de segurança: {1}",
        'pages_deleted_voice': "Foi criada uma cópia de segurança e {0} páginas eliminadas.",
        'info': "Informação",
        'error_dialog_creation': "Não foi possível criar a caixa de diálogo",
        'extract_page_single': "Extrair página {0}",
        'extract_page_range': "Extrair páginas {0}–{1}",
        'extract_success_voice': "Páginas extraídas com sucesso",
        'extract_error_format': "Erro ao extrair: {0}",
        'pages_inserted_voice': "{0} páginas inseridas.",
        'insert_error_format': "Erro ao inserir: {0}",
        'pages_move_progress': "A mover páginas...",
        'pages_moved_with_backup': "{0} páginas foram movidas.\n\nCópia de segurança: {1}",
        'move_success_title': "Movimento bem‑sucedido",
        'pages_moved_voice': "{0} páginas movidas com sucesso",
        'mark_removed': "Marcação removida da página {0}",
        'mark_empty': "Página {0} marcada como vazia",
        'mark_export_removed': "Marcação de exportação removida da página {0}",
        'mark_export': "Página {0} marcada para exportação",
        'no_empty_pages': "Nenhuma página vazia marcada para eliminação",
        'delete_empty_confirm': "Deseja eliminar todas as {0} páginas vazias marcadas?",
        'delete_empty_confirm_voice': "Eliminar agora todas as {0} páginas vazias marcadas? Sim ou Não.",
        'empty_pages_deleted': "{0} páginas vazias eliminadas",
        'no_export_pages': "Nenhuma página marcada para exportação",
        'overwrite_title': "Substituir ficheiro existente",
        'overwrite_question': "O ficheiro\n\n{0}\n\njá existe.\nDeseja substituí‑lo?",
        'overwrite_voice': "Substituir ficheiro existente? Sim ou Não.",
        'page_skipped': "Página {0} ignorada",
        'export_complete': "Exportação concluída.",
        'export_complete_voice': "A exportação está concluída.",
        'no_pages_exported': "Nenhuma página exportada",
        'export_cancelled': "Exportação cancelada",
        'pages_exported': "{0} páginas exportadas para {1}",
        'export_page_title': "Exportar página",
        'page_exported': "Página {0} exportada para {1}",
        'export_error': "Erro ao exportar",
        'export_marked_title': "Exportar páginas marcadas",
        'rotate_all_title': "rodar todas as páginas",
        'rotate_all_question': "Deseja rodar todas as páginas 90 graus para a direita?",
        'rotate_all_voice': "Deseja rodar todas as páginas 90 graus para a direita? Sim ou Não?",
        'all_pages_rotated': "Todas as páginas rodadas",
        'page_rotated': "Página {0} rodada",
        'rotate_error': "Não foi possível rodar a página",
        'delete_page_confirm': "Deseja eliminar a página {0}?",
        'delete_page_confirm_voice': "Deseja realmente eliminar a página {0}? Sim ou Não.",
        'page_deleted': "Página {0} eliminada",
        'delete_error': "Não foi possível eliminar a página",
        'pages_deleted_voice': "{0} páginas eliminadas",
        'pages_exported_split': "{0} páginas foram exportadas com sucesso.",
        'pages_skipped': "{0} páginas foram ignoradas.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extrair páginas (avançado)",
        'pdf_splitter_title': "Separador e extrator de PDF",
        'pdf_splitter_load': " Selecionar ficheiro PDF",
        'pdf_splitter_info': "Escolha uma opção para o seu documento PDF",
        'pdf_splitter_basic': "Operações básicas",
        'pdf_splitter_single': "Dividir em páginas individuais",
        'pdf_splitter_range': "Extrair páginas:",
        'pdf_splitter_range_placeholder': "ex. 1-3,5,7-9",
        'pdf_splitter_clean': "Operações de limpeza",
        'pdf_splitter_remove_empty': "Remover todas as páginas vazias",
        'pdf_splitter_remove': "Eliminar intervalo de páginas:",
        'pdf_splitter_remove_placeholder': "ex. 2,4-6",
        'pdf_splitter_process': "Processar PDF",
        'pdf_splitter_loaded': "PDF carregado. Escolha uma opção",
        'pdf_read_error': "Não foi possível ler o PDF",
        'pages': "Páginas",
        'pages_created': "Páginas foram criadas",
        'range_empty': "Por favor, introduza um intervalo de páginas",
        'range_invalid': "Intervalo de páginas inválido",
        'range_created': "Novo PDF com as páginas selecionadas foi criado:\n{0}",
        'empty_removed': "{0} páginas vazias removidas.\nSaída: {1}",
        'remove_empty': "Por favor, introduza páginas a remover",
        'remove_invalid': "Páginas a remover inválidas",
        'remove_done': "PDF limpo criado:\n{0}",
        'open_folder': "Abrir pasta",
        'show_in_finder': "Mostrar no Finder",
        'pdf_splitter_no_pdf': "Carregue primeiro um ficheiro PDF.",
        'process_error': "Erro ao processar o PDF",
        'pages_created_voice': "{0} páginas foram criadas",
        'range_created_voice': "PDF com as páginas selecionadas foi criado",
        'empty_removed_voice': "{0} páginas vazias foram removidas",
        'remove_done_voice': "PDF limpo foi criado",
        'pdf_splitter_split_groups': "Cada grupo contíguo em ficheiro separado",
        'range_created_single': "Novo PDF criado:\n{0}",
        'range_created_multiple': "{0} ficheiros PDF foram criados.",
        'range_created_voice_single': "Um PDF com as páginas selecionadas foi criado",
        'range_created_voice_multiple': "{0} ficheiros PDF foram criados",
        'empty_removed_none_left': "Nenhuma página restante",
        'empty_removed_all_empty': "Todas as páginas foram reconhecidas como vazias e seriam removidas. Nenhum ficheiro foi criado.",
        'preview_single': "Pré‑visualização: {0}",
        'preview_enter_range': "Por favor, introduza um intervalo de páginas.",
        'preview_invalid_range': "Intervalo de páginas inválido.",
        'preview_file': "Pré‑visualização: {0}",
        'preview_files': "Pré‑visualização: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "A iniciar impressão",
        'print_sent': "Trabalho de impressão enviado",
        'print_now': "Imprimir agora",
        'print_error': "Erro durante a impressão direta",
        'print_limited': "Função de impressão limitada neste sistema",
        'print_error_format': "Erro durante a impressão direta: {0}",
        'warning': "Aviso",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Mudar para modo claro",
        'mode_switch_to_dark': "Mudar para modo escuro",
        'mode_dark_activated': "Modo escuro ativado",
        'mode_light_activated': "Modo claro ativado",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Página inteira",
        'zoom_two_pages': "Duas páginas lado a lado",
        'zoom_overview': "Modo de vista geral",
        'zoom_cannot_during_search': "Zoom não possível durante a pesquisa",
        'zoom_exit_first': "Saia primeiro do zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Arrastar e soltar ativado",
        'drag_disabled': "Arrastar e soltar desativado",
        'drag_page_grab': "Agarrar página {0}",
        'drag_page_dropped': "Página {0} inserida na posição {1}",
        'drag_position_invalid': "Posição inválida",
        'drag_same_position': "A página {0} permanece na posição {0}",
        'drag_error': "Erro ao mover",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Inserção de texto com formatação avançada e gestão de modelos",
        'text_templates': "Modelos de texto disponíveis:",
        'text_name': "Nome",
        'text_preview': "Pré‑visualização do texto",
        'text_enter': "Texto:",
        'text_font_size': "Tamanho da letra:",
        'text_formatting': "Formatação:",
        'text_bold': "Negrito",
        'text_italic': "Itálico",
        'text_underline': "Sublinhado",
        'text_alignment': "Alinhamento:",
        'text_left': "Esquerda",
        'text_center': "Centrado",
        'text_right': "Direita",
        'text_color': "Cor do texto:",
        'text_opacity': "Opacidade:",
        'text_word_wrap': "Quebra de linha:",
        'text_auto': "Automática",
        'text_page_width_95': "Largura da página (95%)",
        'text_page_width_85': "Muito largo (85%)",
        'text_page_width_75': "Mais largo (75%)",
        'text_page_width_60': "Largo (60%)",
        'text_page_width_50': "Médio (50%)",
        'text_page_width_30': "Estreito (30%)",
        'text_page_width_20': "Mais estreito (20%)",
        'text_page_width_10': "Muito estreito (10%)",
        'text_no_wrap': "Sem quebra",
        'text_private': "Modelo privado (requer autenticação)",
        'text_preview_label': "Pré‑visualização:",
        'text_preview_placeholder': "Aqui será mostrada uma pré‑visualização do texto...",
        'text_no_text': "(Sem texto)",
        'text_save_template': "💾 Guardar como modelo",
        'text_delete_template': "🗑 Eliminar modelo selecionado",
        'text_show_private': "Mostrar privados",
        'text_hide_private': "Ocultar privados",
        'text_use': "✅ Usar texto",
        'text_saved': "Modelo de texto guardado como:\n{0}",
        'text_saved_voice': "Modelo de texto guardado",
        'text_deleted': "Modelo de texto eliminado",
        'text_no_text_to_save': "Não há texto para guardar.",
        'text_no_templates': "Nenhum modelo de texto encontrado",
        'text_private_master_required': "Os modelos privados só podem ser usados se uma palavra‑passe mestre estiver configurada.\n\nDeseja configurar uma palavra‑passe mestre agora?",
        'text_filename': "Nome do ficheiro para o modelo (sem 'Text_' e '.txt'):",
        'text_filename_hint': "Exemplo: 'Telefone Casa' será guardado como 'Text_Telefone Casa.txt'",
        'text_save_hint': "O modelo de texto será guardado automaticamente com a formatação.",
        'text_guide_title': "Inserção de texto - Guia",
        'text_delete_confirm': "Deseja realmente eliminar o modelo de texto?\n\nFicheiro: {0}\nTexto: {1}...",
        'text_make_public': "Marcar como público",
        'text_make_private': "Marcar como privado",
        'text_privacy_changed': "Estado de privacidade alterado",
        'text_private_always': "Privados sempre visíveis (configuração)",
        'text_mode_required': "Ative primeiro o modo de texto",
        'text_continue_editing': "Continuar edição - cursor no fim do texto",
        'text_no_input': "Nenhum texto introduzido - texto descartado",
        'save_dialog_question': "Como deseja proceder?",
        'text_save_question': "Guardar todos os textos e cruzes, ajustar, continuar edição ou descartar?",
        'copy_cross': "Cruz copiada",
        'paste_cross': "Cruz colada",
        'paste_text': "Texto colado",
        'cross_discarded': "Cruz descartada",
        'all_discarded': "Tudo descartado",
        'text_discarded': "Texto descartado",
        'no_texts_to_save': "Não há textos para guardar",
        'no_valid_texts': "Não há textos válidos para guardar",
        'text_word_singular': "texto",
        'text_word_plural': "textos",
        'cross_word_singular': "cruz",
        'cross_word_plural': "cruzes",
        'texts_saved_title': "Textos guardados",
        'texts_crosses_saved': "{0} {1} e {2} {3} foram inseridos no PDF.\n\nPDF recarregado...",
        'texts_crosses_saved_voice': "{0} {1} e {2} {3} guardados.",
        'texts_saved': "{0} {1} foram inseridos no PDF.\n\nPDF recarregado...",
        'texts_saved_voice': "{0} {1} guardados.",
        'crosses_saved': "{0} {1} foram inseridos no PDF.\n\nPDF recarregado...",
        'crosses_saved_voice': "{0} {1} guardados.",
        'elements_saved': "{0} elementos foram inseridos no PDF.\n\nPDF recarregado...",
        'elements_saved_voice': "{0} elementos guardados.",
        'text_window_load_error': "Não foi possível carregar a janela de texto",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Inserção de texto e modelos – Guia detalhado**

        **1. Inserir e editar texto**
        - Clique com o botão direito na posição desejada do documento e selecione "Inserir texto".
        - Abre‑se uma janela onde pode introduzir e formatar o seu texto:
        • Tamanho da letra, Negrito, Itálico, Sublinhado
        • Cor do texto (livre escolha)
        • Transparência (opacidade) através de controlo deslizante
        • Quebra de linha (várias larguras, ex. largura da página, estreito, sem quebra)
        - Após confirmação, o texto aparece na posição clicada. Pode movê‑lo com o rato ou teclas de seta.
        - Duplo clique no texto abre o modo de edição; Esc fecha‑o.

        **2. Gerir modelos de texto**
        - Na janela de diálogo, à esquerda vê uma lista de todos os modelos guardados.
        - **Guardar um modelo:** Introduza o seu texto, formate‑o e clique em "💾 Guardar como modelo". Introduza um nome de ficheiro (sem extensão).
        - **Carregar um modelo:** Clique no nome desejado na lista. O texto e a formatação são aplicados e podem ser ajustados se necessário.
        - **Eliminar:** Clique com o botão direito num modelo para o eliminar ou alterar o seu estado privado/público.

        **3. Modelos privados (palavra‑passe mestre)**
        - Se tiver configurado uma palavra‑passe mestre (em Configurações → Gestor de palavras‑passe), pode marcar modelos como "privados".
        - Ative a caixa "Modelo privado" na janela de diálogo antes de guardar.
        - Os modelos privados só são mostrados na lista se tiver introduzido a sua palavra‑passe mestre uma vez por sessão (autenticação através do ícone do cadeado ou no primeiro acesso).
        - Assim protege modelos confidenciais de acesso não autorizado.

        **4. Inserir cruzes**
        - Através do menu de contexto também pode inserir uma cruz gráfica (por exemplo, para caixas de verificação).
        - O tamanho, espessura da linha e cor das cruzes podem ser ajustados globalmente nas configurações (menu "Configurações" → "Configurações de cruzes").
        - Clique com o botão direito numa cruz existente para a modificar individualmente.

        **5. Ações em lote**
        - Se tiver colocado vários textos ou cruzes numa página, pode guardá‑los ou descartá‑los todos juntos através do menu de contexto (clique direito em modo de texto).
        - Ao guardar, todos os elementos são incorporados no PDF e permanecem como gráficos vetoriais.

        **6. Atalhos de teclado em modo de texto**
        - Teclas de seta: mover elemento
        - Ctrl+Setas: passos maiores
        - Enter: abrir janela de guardar (guardar tudo / ajustar / descartar)
        - Esc: descartar elemento atual
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Inserção de texto e modelos – Guia detalhado</strong></p>

        <p><strong>1. Inserir e editar texto</strong></p>
        <ul>
        <li>Clique com o botão direito na posição desejada do documento e selecione "Inserir texto".</li>
        <li>Abre‑se uma janela onde pode introduzir e formatar o seu texto:<br/>
        • Tamanho da letra, Negrito, Itálico, Sublinhado<br/>
        • Cor do texto (livre escolha)<br/>
        • Transparência (opacidade) através de controlo deslizante<br/>
        • Quebra de linha (várias larguras, ex. largura da página, estreito, sem quebra)</li>
        <li>Após confirmação, o texto aparece na posição clicada. Pode movê‑lo com o rato ou teclas de seta.</li>
        <li>Duplo clique no texto abre o modo de edição; Esc fecha‑o.</li>
        </ul>

        <p><strong>2. Gerir modelos de texto</strong></p>
        <ul>
        <li>Na janela de diálogo, à esquerda vê uma lista de todos os modelos guardados.</li>
        <li><strong>Guardar um modelo:</strong> Introduza o seu texto, formate‑o e clique em "💾 Guardar como modelo". Introduza um nome de ficheiro (sem extensão).</li>
        <li><strong>Carregar um modelo:</strong> Clique no nome desejado na lista. O texto e a formatação são aplicados e podem ser ajustados se necessário.</li>
        <li><strong>Eliminar:</strong> Clique com o botão direito num modelo para o eliminar ou alterar o seu estado privado/público.</li>
        </ul>

        <p><strong>3. Modelos privados (palavra‑passe mestre)</strong></p>
        <ul>
        <li>Se tiver configurado uma palavra‑passe mestre (em Configurações → Gestor de palavras‑passe), pode marcar modelos como "privados".</li>
        <li>Ative a caixa "Modelo privado" na janela de diálogo antes de guardar.</li>
        <li>Os modelos privados só são mostrados na lista se tiver introduzido a sua palavra‑passe mestre uma vez por sessão (autenticação através do ícone do cadeado ou no primeiro acesso).</li>
        <li>Assim protege modelos confidenciais de acesso não autorizado.</li>
        </ul>

        <p><strong>4. Inserir cruzes</strong></p>
        <ul>
        <li>Através do menu de contexto também pode inserir uma cruz gráfica (por exemplo, para caixas de verificação).</li>
        <li>O tamanho, espessura da linha e cor das cruzes podem ser ajustados globalmente nas configurações (menu "Configurações" → "Configurações de cruzes").</li>
        <li>Clique com o botão direito numa cruz existente para a modificar individualmente.</li>
        </ul>

        <p><strong>5. Ações em lote</strong></p>
        <ul>
        <li>Se tiver colocado vários textos ou cruzes numa página, pode guardá‑los ou descartá‑los todos juntos através do menu de contexto (clique direito em modo de texto).</li>
        <li>Ao guardar, todos os elementos são incorporados no PDF e permanecem como gráficos vetoriais.</li>
        </ul>

        <p><strong>6. Atalhos de teclado em modo de texto</strong></p>
        <ul>
        <li>Teclas de seta: mover elemento</li>
        <li>Ctrl+Setas: passos maiores</li>
        <li>Enter: abrir janela de guardar (guardar tudo / ajustar / descartar)</li>
        <li>Esc: descartar elemento atual</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Configurações de cruzes",
        'cross_properties': "Propriedades da cruz",
        'cross_size': "Tamanho (px):",
        'cross_line_width': "Espessura da linha:",
        'cross_color': "Cor:",
        'cross_choose_color': "Escolher",
        'cross_fine_tuning': "Ajuste fino ao guardar (píxeis)",
        'cross_offset_x': "Deslocamento X:",
        'cross_offset_y': "Deslocamento Y:",
        'cross_offset_x_tooltip': "Valores negativos deslocam a cruz para a esquerda, positivos para a direita",
        'cross_offset_y_tooltip': "Valores negativos deslocam a cruz para cima, positivos para baixo",
        'cross_preview': "Pré‑visualização",
        'cross_save': "Aplicar configurações",
        'cross_customized': "Cruz personalizada",
        'cross_settings_applied': "Configurações de cruz guardadas.\nTamanho: {0}px, Espessura: {1}px\n{2}",
        'cross_updated_count': "{0} cruzes existentes foram atualizadas.",
        'cross_no_crosses': "Nenhuma cruz existente encontrada.",
        'cross_settings_applied_all': "Configurações de cruz aplicadas a todas as {0} cruzes",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Configurações de assinaturas",
        'signature_1': "Assinatura 1",
        'signature_2': "Assinatura 2",
        'signature_select': "Selecionar assinatura",
        'signature_add': "➕ Adicionar nova assinatura...",
        'signature_size': "Tamanho para assinatura {0} (%):",
        'signature_common': "Configurações gerais",
        'signature_timestamp': "Adicionar automaticamente carimbo de data/hora",
        'signature_location': "Local predefinido:",
        'signature_timestamp_size': "Tamanho da letra do carimbo:",
        'signature_no_files': "-- Nenhuma assinatura encontrada --",
        'signature_insert': "Inserir assinatura",
        'signature_insert_1': "Inserir assinatura 1",
        'signature_insert_2': "Inserir assinatura 2",
        'signature_customize': " Personalizar assinatura",
        'signature_discard': " Descartar esta assinatura",
        'signature_save_all': " Guardar todas as assinaturas",
        'signature_discard_all': " Descartar todas as assinaturas",
        'signature_guide_title': "Assinaturas - Guia",
        'signature_guide': """
📝 Assinaturas - Guia rápido

- Configurar palavra‑passe mestre
- Configurar as assinaturas no menu Configurações
  (tamanho, carimbo de data/hora ...)
- Inserir com BOTÃO DIREITO na posição desejada
  (requer palavra‑passe mestre uma vez por sessão)
- Mover a assinatura com o rato ou teclas de seta
- Podem ser inseridas várias assinaturas em sequência
- Cada assinatura pode ser personalizada individualmente
- Descartar uma assinatura
- Guardar / descartar todas as assinaturas de uma vez
- Em alternativa, pode usar a barra de menu.
        """,
        'signature_placeholder': "Nenhuma pré‑visualização disponível",
        'signature_info': "Assinatura {0}: {1}×{2} px ({3}% de {4}×{5})",
        'signature_info_placeholder': "Configurações para assinatura {0}",
        'signature_inserted': "Assinatura {0} inserida na página {1}",
        'signature_deleted': "Assinatura eliminada",
        'signature_copied': "Assinatura copiada",
        'signature_pasted': "Assinatura {0} colada",
        'signature_saved': "{0} assinaturas foram inseridas no PDF.\n\nPDF recarregado...",
        'signature_saved_voice': "{0} assinaturas guardadas",
        'mode_replace_signature_format': "Sair do modo e inserir assinatura {0}",
        'mode_conflict_voice_signature': "O modo {0} está ativo. Sair e inserir assinatura?",
        'signature_not_configured': "Assinatura {0} não configurada",
        'signature_file_not_found': "Ficheiro de assinatura não encontrado",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nenhuma assinatura copiada disponível",
        'no_signatures_to_save': "Não há assinaturas para guardar",
        'signature_save_question': "Guardar todas as assinaturas, ajustar ou descartar esta?",
        'signatures_saved_title': "Assinaturas guardadas",
        'signatures_saved': "{0} assinaturas foram inseridas no PDF.\n\nPDF recarregado...",
        'signatures_saved_voice': "{0} assinaturas guardadas.",
        'all_signatures_discarded': "Todas as assinaturas descartadas",
        'signature_settings_saved': "Configurações de assinatura guardadas",
        'signature_cancelled': "Assinatura descartada",
        'signature_active_title': "Assinatura ativa",
        'signature_replace_question': "Já existe uma assinatura ativa.\n\nDeseja substituir a assinatura atual?",
        'signature_replace': "Substituir assinatura",
        'signature_replace_voice': "Substituir assinatura atual ou cancelar?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Configurações de imagem",
        'image_common': "Configurações gerais de imagem",
        'image_keep_aspect': "Manter proporção ao arrastar",
        'image_default_size': "Tamanho predefinido (%):",
        'image_dark_invert': "Inverter imagens no modo escuro",
        'image_dark_invert_tooltip': "Ativado: as imagens são invertidas para melhor visibilidade",
        'image_fine_tuning': "Ajuste fino (píxeis)",
        'image_offset_x': "Deslocamento X:",
        'image_offset_y': "Deslocamento Y:",
        'image_offset_x_tooltip': "Valores negativos deslocam a imagem para a esquerda, positivos para a direita",
        'image_offset_y_tooltip': "Valores negativos deslocam a imagem para cima, positivos para baixo",
        'image_select': "Selecionar imagem",
        'image_insert': "Inserir imagem",
        'image_customize': " Personalizar imagem",
        'image_aspect': " Manter proporção",
        'image_discard': " Descartar esta imagem",
        'image_save_all': " Guardar todas as imagens",
        'image_discard_all': " Descartar todas as imagens",
        'image_filter': "Imagens",
        'image_guide_title': "Inserir imagem - Guia",
        'image_guide': """
📷 Inserir imagem em PDF - Guia rápido:

1. Botão direito na posição desejada
2. "Inserir imagem" → selecionar imagem
3. Posicionar imagem: arrastar com o rato
4. Ajustar tamanho: arrastar nos cantos/bordas
5. Manter proporção: tecla [A]
6. Outros ajustes: botão direito na imagem

Dica: pode ajustar as configurações no menu de contexto.
        """,
        'image_inserted': "Imagem {0} inserida na página {1}",
        'image_deleted': "Imagem descartada",
        'image_copied': "Imagem copiada",
        'image_pasted': "Imagem colada",
        'image_saved': "{0} imagens foram inseridas no PDF.\n\nPDF recarregado...",
        'image_saved_voice': "{0} imagens guardadas",
        'image_aspect_on': "ativado",
        'image_aspect_off': "desativado",
        'image_aspect_toggle': "Manter proporção {0}",
        'image_reset': "Imagem restaurada ao tamanho original",
        'image_replaced': "Imagem substituída",
        'image_invalid': "Imagem não válida",
        'mode_replace_image': "Inserir imagem",
        'mode_conflict_voice_image': "O modo {0} está ativo. Sair e inserir imagem?",
        'image_active_title': "Imagem ativa",
        'image_replace_question': "Já existe uma imagem ativa.\n\nDeseja substituir a imagem atual?",
        'image_replace': "Substituir imagem",
        'image_replace_voice': "Substituir imagem atual ou cancelar?",
        'image_filter_all': "Imagens (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Todos os ficheiros (*.*)",
        'no_copied_image': "Nenhuma imagem copiada disponível",
        'image_discarded': "Imagem descartada",
        'image_save_question': "Guardar todas as imagens, ajustar ou descartar esta?",
        'no_images_to_save': "Não há imagens para guardar",
        'no_valid_images': "Não há imagens válidas para guardar",
        'images_saved_title': "Imagens guardadas",
        'images_saved': "{0} imagens foram inseridas no PDF.\n\nPDF recarregado...",
        'images_saved_voice': "{0} imagens guardadas.",
        'all_images_discarded': "Todas as imagens descartadas",
        'image_settings_updated': "Configurações de imagem atualizadas",
        'image_replace_title': "Selecionar nova imagem",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Configurações de formas",
        'form_basic': "Configurações básicas",
        'form_default_type': "Tipo de forma predefinido:",
        'form_rectangle': "Retângulo",
        'form_ellipse': "Elipse",
        'form_line': "Linha",
        'form_arrow': "Seta",
        'form_line_width': "Espessura da linha:",
        'form_colors': "Cores",
        'form_line_color': "Cor da linha:",
        'form_fill_color': "Cor de preenchimento:",
        'form_choose_color': "Escolher",
        'form_transparent': "Fundo transparente (apenas linha)",
        'form_filled': "preenchido",
        'form_dark_mode': "Modo escuro",
        'form_dark_invert': "Inverter cores no modo escuro",
        'form_fine_tuning': "Ajuste fino (píxeis)",
        'form_offset_x': "Deslocamento X:",
        'form_offset_y': "Deslocamento Y:",
        'form_offset_x_tooltip': "Valores negativos deslocam a forma para a esquerda, positivos para a direita",
        'form_offset_y_tooltip': "Valores negativos deslocam a forma para cima, positivos para baixo",
        'form_preview': "Pré‑visualização",
        'form_insert': "Inserir forma",
        'form_rectangle_insert': "Retângulo",
        'form_ellipse_insert': "Elipse/Círculo",
        'form_line_insert': "Linha (2 cliques)",
        'form_arrow_insert': "Seta (2 cliques)",
        'form_customize': " Personalizar forma",
        'form_transparent_toggle': " Fundo transparente",
        'form_discard': " Descartar esta forma",
        'form_save_all': " Guardar todas as formas",
        'form_discard_all': " Descartar todas as formas",
        'form_guide_title': "Inserir forma - Guia",
        'form_guide': """
📐 Inserir forma em PDF - Guia rápido:

1. Escolher tipo de forma (retângulo, elipse, linha, seta)
2. Clicar na posição desejada
   - Para retângulo/elipse: um clique coloca a forma
   - Para linha/seta: dois cliques para ponto inicial e final
3. Posicionar forma: arrastar com o rato
4. Ajustar tamanho: arrastar nos cantos/bordas
5. Guardar forma: Enter
6. Descartar forma: Esc
7. Outros ajustes: botão direito na forma

Dica: pode ajustar as configurações no menu de contexto.
        """,
        'form_inserted': "{0} inserida na página {1}",
        'form_deleted': "Forma eliminada",
        'form_copied': "Forma copiada",
        'form_pasted': "Forma colada",
        'form_saved': "{0} formas foram inseridas no PDF.\n\nPDF recarregado...",
        'form_saved_voice': "{0} formas guardadas",
        'form_reset': "Forma restaurada ao tamanho predefinido",
        'form_transparent_on': "ativado",
        'form_transparent_off': "desativado",
        'form_transparent_toggled': "Fundo transparente {0}",
        'form_line_cancel': "Desenho de linha cancelado",
        'form_second_click': "Agora clique no ponto final para {0}",
        'mode_replace_form': "Inserir forma",
        'mode_conflict_voice_form': "O modo {0} está ativo. Sair e inserir uma forma?",
        'form_settings_updated': "Configurações de forma atualizadas",
        'form_unknown': "Forma",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Clique na posição inicial",
        'form_line_guide_2': "2. Clique na posição final",
        'form_line_guide_3': "A linha será desenhada entre os dois pontos.",
        'form_line_status_1': "À espera do primeiro clique...",
        'form_line_status_2': "Primeiro ponto definido: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Agora clique no ponto final...",
        'form_line_status_4': "Ambos os pontos definidos.\nClique em 'Concluir' para guardar.",
        'form_line_reset': "Reiniciar",
        'form_line_finish': "Concluir",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Copiar (Cmd+C)",
        'paste': "Colar (Cmd+V)",
        'copied': "Copiado: {0}",
        'no_element_to_copy': "Nenhum elemento selecionado para copiar",
        'no_copied_data': "Não há dados copiados disponíveis",
        'no_valid_position': "Posição inválida para colar",
        'copy_text': "Texto copiado",
        'copy_image': "Imagem copiada",
        'copy_form': "Forma copiada",
        'copy_signature': "Assinatura copiada",
        'element_text': "texto",
        'element_image': "imagem",
        'element_form': "forma",
        'element_signature': "assinatura",
        'element_unknown': "elemento",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Conflito de modo",
        'mode_conflict_message': "O modo '{0}' já está ativo.\n\nDeseja sair dele e {1}?",
        'mode_replace': "Sair do modo e {0}",
        'mode_cancel': "Cancelar",
        'mode_replace_text': "inserir texto",
        'mode_replace_cross': "inserir cruz",
        'mode_replace_signature': "inserir assinatura",
        'mode_replace_image': "inserir imagem",
        'mode_replace_form': "inserir forma",
        'mode_conflict_voice': "O modo {0} está ativo. Sair e inserir texto?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Inserção de texto",
        'active_mode_signature': "Assinatura",
        'active_mode_image': "Imagem",
        'active_mode_form': "Forma",
        'active_mode_and': " e ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Inserir",                    # Hauptmenü
        'insert_another_text': "Inserir texto",          # Vereinfacht
        'insert_another_cross': "Inserir cruz",        # Vereinfacht
        'insert_another_signature_1': "Assinatura 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Assinatura 2",      # Untermenü-Eintrag
        'insert_another_image': "Inserir imagem",         # Vereinfacht
        'insert_another_form_rect': "Retângulo",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Elipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Linha (2 cliques)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Seta (2 cliques)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Guardar {0}",
        'save_dialog_message': "{0} será guardado/a na página {1}.\n\nComo deseja proceder?",
        'save_all': "Guardar todos os {0}",
        'save_single': "Guardar {0}",
        'save_customize': "Personalizar {0}",
        'save_discard': "Descartar {0}",
        'save_continue': "Continuar edição",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Ir para a página {0}",
        'context_rotate': " Rodar página {0}",
        'context_delete': " Eliminar página {0}",
        'context_export': " Exportar página {0}",
        'context_mark_as': " Marcar página como...",
        'context_mark_empty': " Página vazia",
        'context_unmark_empty': " Já não vazia",
        'context_mark_export': " Marcar para exportação",
        'context_unmark_export': " Não exportar",
        'context_batch_actions': " Ações em lote",
        'context_batch_delete_empty': " Eliminar as {0} páginas vazias",
        'context_batch_export_single': " Todas as {0} páginas (um ficheiro)",
        'context_batch_export_split': " Todas as {0} páginas (separadas)",
        'context_drag_start': " Ativar arrastar e soltar",
        'context_drag_stop': " Desativar arrastar e soltar",
        'context_insert': " Inserir",
        'context_insert_pages': " Inserir páginas",
        'context_zoom': "Zoom",
        'discard_mixed': "Descartar {0} {1} e {2} {3}",
        'save_mixed': "Guardar {0} {1} e {2} {3}",
        'discard_texts': "Descartar {0} textos",
        'discard_text_single': "Descartar 1 texto",
        'save_texts': "Guardar {0} textos",
        'save_text_single': "Guardar 1 texto",
        'discard_crosses': "Descartar {0} cruzes",
        'discard_cross_single': "Descartar 1 cruz",
        'save_crosses': "Guardar {0} cruzes",
        'save_cross_single': "Guardar 1 cruz",
        'discard_signatures': "Descartar {0} assinaturas",
        'save_signature_single': "Guardar 1 assinatura",
        'save_signatures': "Guardar {0} assinaturas",
        'discard_images': "Descartar {0} imagens",
        'save_image_single': "Guardar 1 imagem",
        'save_images': "Guardar {0} imagens",
        'discard_forms': "Descartar {0} formas",
        'save_form_single': "Guardar 1 forma",
        'save_forms': "Guardar {0} formas",
        'cross_discard': "Descartar esta cruz",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informação de exportação/importação",
        'export_what': "📋 O que é exportado?",
        'export_general': "Configurações gerais",
        'export_general_items': "• Síntese de voz (ligada/desligada, velocidade)\n• Modo escuro/claro\n• Configurações de cópia de segurança\n• Configurações de OCR",
        'export_image_form': "Configurações de imagem e forma",
        'export_image_form_items': "• Configurações de imagem (proporção, tamanho predefinido)\n• Configurações de forma (espessura da linha, cores)\n• Configurações de assinatura (caminhos, tamanhos, carimbo de data/hora)",
        'export_passwords': "Base de dados de palavras‑passe",
        'export_passwords_items': "• Todas as palavras‑passe de PDF guardadas\n• Opcionalmente encriptadas ou desencriptadas",
        'export_master': "Configurações de palavra‑passe mestre",
        'export_master_items': "• Hash da palavra‑passe mestre\n• Configurações para assinaturas/modelos de texto",
        'export_signatures': "Assinaturas e modelos de texto",
        'export_signatures_items': "• Todos os ficheiros de imagem (assinaturas)\n• Todos os modelos de texto com formatação\n• Marcações privado/público",
        'export_import_warning': "⚠️ Notas importantes",
        'export_import_note': "• Durante a importação, TODAS as configurações atuais são substituídas\n• É necessário reiniciar a aplicação\n• As assinaturas/modelos existentes serão substituídos",
        'export_master_note': "• Se uma palavra‑passe mestre estiver definida, pode escolher:\n  - Desencriptado (palavras‑passe em texto claro)\n  - Encriptado (apenas legível com palavra‑passe mestre)",
        'export_security': "• O ficheiro ZIP exportado contém dados confidenciais\n• Guarde‑o num local seguro (ex. pen USB encriptada)\n• Em caso de perda do ficheiro, as palavras‑passe perdem‑se irreversivelmente",
        'export_format': "📁 Formato de exportação",
        'export_format_desc': "As configurações são guardadas num único ficheiro ZIP:",
        'export_filename': "PDFDarkView_Configurações_AAAAMMDD_HHMMSS.zip",
        'export_success': "Configurações exportadas com sucesso",
        'export_failed': "Falha na exportação",
        'export_import_question': "Deseja reiniciar a aplicação agora?",
        'export_password_question': "Está definida uma palavra‑passe mestre.\n\nDeseja exportar as palavras‑passe desencriptadas?\n(caso contrário, serão exportadas encriptadas)",
        'export_decrypt': "Exportar desencriptadas",
        'export_encrypt': "Exportar encriptadas",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informações",
        'info_title': "Sobre o PDF Dark View",
        'info_version': "Versão",
        'info_author': "Desenvolvido por Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Sobre",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> é um visualizador de PDF acessível, desenvolvido especialmente para pessoas com deficiência visual.</p>

            <p><strong>Principais características:</strong></p>
            <ul>
                <li>Interface de alto contraste e personalizável</li>
                <li>Controlo total por teclado</li>
                <li>Síntese de voz integrada</li>
                <li>OCR para documentos digitalizados</li>
                <li>Ferramentas de edição abrangentes</li>
            </ul>

            <p>Mais de 50 idiomas são suportados – para que os PDFs sejam acessíveis a todos.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funcionalidades",
        'info_features_intro': "O PDF Dark View oferece-lhe as seguintes possibilidades:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Visualização e navegação</strong> – Modo escuro/claro, folhear páginas, zoom, saltar para página</li>
            <li><strong>OCR (reconhecimento de texto)</strong> – Torne documentos digitalizados pesquisáveis e copiáveis</li>
            <li><strong>Edição</strong> – Inserir texto, cruzes, assinaturas, imagens e formas</li>
            <li><strong>Gestão de páginas</strong> – Eliminar, extrair, inserir, mover por arrastar e soltar</li>
            <li><strong>Exportação</strong> – Para Word, Pages ou como texto</li>
            <li><strong>Segurança</strong> – Proteção e gestão por palavra-passe</li>
            <li><strong>Acessibilidade</strong> – Síntese de voz, controlo por teclado, alto contraste</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Utilização",
        'info_accessibility': "♿ Acessibilidade – controlo total por teclado",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Geral</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Abrir PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Procurar</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Alternar modo escuro/claro</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Imprimir</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Sair</div>

        <div class="shortcut-cat">📖 Navegação</div>
        <div class="shortcut-row"><kbd>Teclas de seta</kbd> Folhear página por página</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Ir para página</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Primeira página</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Última página</div>

        <div class="shortcut-cat">✏️ Edição</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Inserir texto</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Eliminar páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extrair páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Inserir páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Mover páginas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rodar página</div>

        <div class="shortcut-cat">🖼️ Mover elementos</div>
        <div class="shortcut-row"><kbd>Teclas de seta</kbd> Mover texto/imagem/assinatura</div>
        <div class="shortcut-row"><kbd>Ctrl+Teclas de seta</kbd> Passos maiores</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Guardar</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Descartar</div>

        <div class="shortcut-cat">🗣️ Síntese de voz</div>
        <div class="shortcut-row"><kbd>F2</kbd> Ativar/desativar síntese de voz</div>
        """,
        'info_contextmenu': "📌 Importante: Todas as funções também estão acessíveis através do menu de contexto (botão direito do rato)!",
        'info_accessibility_hint': "💡 Dica: A síntese de voz (F2) facilita a orientação e fornece feedback sobre menus e diálogos.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licença & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Informações de acordo com § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Alemanha<br>
        E-mail: binhdiez64@gmail.com<br>
        Responsável pelo conteúdo: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Exclusão de responsabilidade</strong><br>
        O software foi desenvolvido com o maior cuidado. Não é dada qualquer garantia quanto à exatidão, integridade e funcionalidade. A utilização é por sua própria conta e risco.<br><br>

        <strong>📄 Licença MIT (utilização privada)</strong><br>
        Direitos de autor (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permitido: utilização gratuita, alterações privadas, cópias pessoais.<br>
        Não permitido: venda, utilização comercial, remoção de avisos de direitos de autor.<br><br>

        <strong>🔧 Componentes de terceiros</strong><br>
        Este software contém componentes sob licenças GPL, AGPL, Apache 2.0, BSD e MIT.<br>
        Ao redistribuir, devem ser cumpridos os respetivos termos de licença.<br><br>

        <strong>🌐 Código Aberto</strong><br>
        O código-fonte está disponível e pode ser visualizado, modificado e redistribuído de acordo com os respetivos termos de licença.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Agradecimentos",
        'info_credits': "Agradecimentos à comunidade de código aberto",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Processamento de PDF</li>
            <li><strong>PyQt5</strong> – Interface gráfica</li>
            <li><strong>Tesseract OCR</strong> – Reconhecimento de texto</li>
            <li><strong>OCRmyPDF</strong> – Integração OCR</li>
            <li><strong>python-docx</strong> – Exportação para Word</li>
            <li><strong>qtawesome</strong> – Ícones</li>
            <li><strong>DeepSeek</strong> – Apoio nas traduções (50+ idiomas)</li>
            <li><strong>Todos os utilizadores</strong> – Pelos valiosos comentários</li>
            <li><strong>A comunidade de código aberto</strong> – Pelas excelentes bibliotecas</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Idiomas",
        'info_languages_header': "🌍 Suporte a idiomas",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>O PDF Dark View suporta atualmente <strong>62 idiomas</strong> – para que o software possa ser usado de forma acessível em todo o mundo.</p>

            <p><strong>📖 Lista completa de idiomas (Status: março de 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Africâner</li>
                    <li>🇦🇱 Albanês (Shqip)</li>
                    <li>🇩🇿 Árabe (العربية)</li>
                    <li>🇮🇩 Balinês (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Birmanês (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bósnio (Bosanski)</li>
                    <li>🇧🇬 Búlgaro (Български)</li>
                    <li>🇨🇳 Chinês (中文)</li>
                    <li>🇩🇰 Dinamarquês (Dansk)</li>
                    <li>🇩🇪 Alemão (Deutsch)</li>
                    <li>🇬🇧 Inglês (English)</li>
                    <li>🇪🇪 Estoniano (Eesti)</li>
                    <li>🇫🇮 Finlandês (Suomi)</li>
                    <li>🇫🇷 Francês (Français)</li>
                    <li>🇬🇷 Grego (Ελληνικά)</li>
                    <li>🇮🇱 Hebraico (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croata (Hrvatski)</li>
                    <li>🇭🇺 Húngaro (Magyar)</li>
                    <li>🇮🇩 Indonésio (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandês (Gaeilge)</li>
                    <li>🇮🇸 Islandês (Íslenska)</li>
                    <li>🇮🇹 Italiano (Italiano)</li>
                    <li>🇯🇵 Japonês (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Coreano (한국어)</li>
                    <li>🇱🇦 Laosiano (ພາສາລາວ)</li>
                    <li>🇱🇻 Letão (Latviešu)</li>
                    <li>🇱🇹 Lituano (Lietuvių)</li>
                    <li>🇱🇺 Luxemburguês (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaio (Bahasa Melayu)</li>
                    <li>🇮🇳 Marata (मराठी)</li>
                    <li>🇲🇳 Mongol (Монгол)</li>
                    <li>🇳🇵 Nepalês (नेपाली)</li>
                    <li>🇳🇱 Holandês (Nederlands)</li>
                    <li>🇳🇴 Norueguês (Norsk)</li>
                    <li>🇦🇫 Pastó (پښتو)</li>
                    <li>🇮🇷 Persa (فارسی)</li>
                    <li>🇵🇱 Polonês (Polski)</li>
                    <li>🇵🇹 Português (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Romeno (Română)</li>
                    <li>🇷🇺 Russo (Русский)</li>
                    <li>🇸🇪 Sueco (Svenska)</li>
                    <li>🇷🇸 Sérvio (Српски)</li>
                    <li>🇸🇰 Eslovaco (Slovenčina)</li>
                    <li>🇸🇮 Esloveno (Slovenščina)</li>
                    <li>🇪🇸 Espanhol (Español)</li>
                    <li>🇹🇿 Suaíli (Kiswahili)</li>
                    <li>🇵🇭 Tagalo (Filipino)</li>
                    <li>🇮🇳 Tâmil (தமிழ்)</li>
                    <li>🇮🇳 Télugo (తెలుగు)</li>
                    <li>🇹🇭 Tailandês (ไทย)</li>
                    <li>🇨🇿 Tcheco (Čeština)</li>
                    <li>🇹🇷 Turco (Türkçe)</li>
                    <li>🇺🇦 Ucraniano (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamita (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Iídiche (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Adicionar seus próprios idiomas:</strong><br>
                Deseja um idioma que ainda não está incluído? Basta colocar seu próprio arquivo de dicionário (<code>sprache_xx.py</code>) ao lado do aplicativo – o software o reconhecerá automaticamente. Se você estiver interessado em uma tradução específica, sinta-se à vontade para entrar em contato comigo.
            </div>

            <p><strong>🙏 Agradecimento especial:</strong> DeepSeek pelo suporte na tradução de todos os dicionários para 62 idiomas.</p>

            <p>📧 Contato para traduções: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Erro",
        'error_occurred': "Ocorreu um erro",
        'error_pdf_load': "Erro ao carregar o PDF",
        'error_pdf_save': "Erro ao guardar o PDF",
        'error_ocr': "Erro durante o reconhecimento de texto",
        'error_no_pdf': "Nenhum PDF carregado",
        'error_page_not_found': "Página não encontrada",
        'error_invalid_range': "Intervalo de páginas inválido",
        'error_file_not_found': "Ficheiro não encontrado",
        'error_permission': "Permissão negada",
        'error_unknown': "Erro desconhecido",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Sucesso",
        'success_operation': "Operação concluída com sucesso",
        'success_saved': "Guardado com sucesso",
        'success_exported': "Exportado com sucesso",
        'success_imported': "Importado com sucesso",
        'success_deleted': "Eliminado com sucesso",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Confirmação",
        'confirm_yes': "Sim",
        'confirm_no': "Não",
        'confirm_ok': "OK",
        'confirm_cancel': "Cancelar",
        'confirm_delete': "Eliminar",
        'confirm_overwrite': "Substituir",
        'confirm_continue': "Continuar",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "A carregar PDF...",
        'progress_saving': "A guardar PDF...",
        'progress_exporting': "A exportar PDF...",
        'progress_processing': "A processar...",
        'progress_wait': "Aguarde, por favor...",
        'progress_preparing': "A preparar...",
        'progress_finalizing': "A finalizar...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Branco",
        'color_black': "Preto",
        'color_red': "Vermelho",
        'color_green': "Verde",
        'color_blue': "Azul",
        'color_yellow': "Amarelo",
        'color_magenta': "Magenta",
        'color_cyan': "Ciano",
        'color_orange': "Laranja",
        'color_gray': "Cinzento",
        'color_custom': "Seletor de cor",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Ficheiro",
        'menu_edit': "&Editar",
        'menu_view': "&Ver",
        'menu_tools': "&Ferramentas",
        'menu_settings': "&Configurações",
        'menu_help': "&Ajuda",
        'menu_language': "🌐 Idioma",
        'menu_guides': "&Guias",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Abrir",
        'file_save_as': "&Guardar como...",
        'file_protect': "&Proteger documento...",
        'file_export': "&Exportar",
        'file_export_pages': "Exportar para Pages",
        'file_export_word': "Exportar para DOCX",
        'file_export_text': "Exportar para TXT",
        'file_print_now': "&Imprimir agora",
        'file_print': "&Imprimir",
        'file_close': "&Fechar",
        'file_quit': "&Sair",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Pesquisar",
        'edit_ocr': " Executar OCR",
        'edit_rotate': "&Rodar página",
        'edit_rotate_all': "&Rodar todas as páginas",
        'edit_delete_pages': "&Eliminar páginas",
        'edit_extract_pages': "&Extrair páginas",
        'edit_insert_pages': "&Inserir páginas",
        'edit_move_pages': "&Mover páginas",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Inserir texto e cruzes",
        'text_insert': " Inserir texto",
        'cross_insert': " Inserir cruz",
        'text_customize': " Personalizar texto",
        'cross_customize': " Personalizar esta cruz",
        'cross_customize_all': " Personalizar todas as cruzes",
        'text_discard': " Descartar este texto / esta cruz",
        'text_discard_all': " Descartar todos os textos e cruzes",
        'text_save_all': " Guardar todos os textos e cruzes",
        'text_guide': " Inserção de texto / modelos - Guia",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Inserir assinatura",
        'signature_settings_menu': " Configurações...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Inserir imagem",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Inserir formas",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Mostrar janela de texto",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Largura da página (predefinido)",
        'view_zoom_two': "&Duas páginas",
        'view_zoom_overview': "&Vista geral (várias páginas)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Acessibilidade",
        'settings_voice': "Síntese de voz",
        'settings_voice_tooltip': "complementa a síntese de voz dos leitores de ecrã com informações adicionais",
        'settings_signature': "&Configurações de assinatura",
        'settings_password': "&Gestor de palavras‑passe",
        'settings_backup': "Criar cópia de segurança antes de alterações",
        'settings_export_import': "&Exportar / importar configurações",
        'settings_export': "&Exportar todas as configurações...",
        'settings_import': "&Importar todas as configurações...",
        'settings_export_info': "&O que é exportado?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "ativada",
        'voice_off': "desativada",
        'voice_toggle': "Síntese de voz {0}",
        'voice_speed': "Velocidade a {0} por cento",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Ferramenta não encontrada:\n{0}\n\nBASE_DIR: {1}\nCertifique‑se de que as ferramentas PDF estão instaladas no diretório {1}.",
        'tool_started': "{0} iniciado",
        'tool_start_failed': "Não foi possível iniciar",
        'process_error_failed_to_start': "Não foi possível iniciar o processo. O ficheiro existe?",
        'process_error_crashed': "O processo bloqueou durante o arranque.",
        'process_error_timeout': "Tempo limite do processo atingido.",
        'process_error_write': "Erro de escrita no processo.",
        'process_error_read': "Erro de leitura do processo.",
        'process_error_unknown': "Erro de processo desconhecido",
        'process_command': "Comando",
        'process_normal_exit': "terminado normalmente",
        'process_crashed': "bloqueado",
        'process_nonzero_exit': "{0} terminado com código de erro {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "A cancelar...",
        'move_cancelling': "Cancelamento de movimento",
        'opening_pdf': "A abrir PDF...",
        'loading_document': "A carregar documento...",
        'pdf_opened': "PDF aberto",
        'pages_found_moving': "{0} páginas encontradas, {1} para mover",
        'creating_backup': "A criar cópia de segurança...",
        'backup_description': "A salvaguardar ficheiro original...",
        'backup_saved_as': "Salvaguardado como: {0}",
        'error_format': "Erro: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView por BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Pesquisa reiniciada",
        'page_header_simple': "=== Página {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Gestor de palavras‑passe – Guia",
        'password_guide_voice': "Guia de gestão de palavras‑passe. Por favor, leia as notas.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Gestor de palavras‑passe – Guia detalhado</strong></p>

        <p><strong>1. Proteção por palavra‑passe para PDF</strong></p>
        <ul>
        <li>Ao abrir um PDF protegido por palavra‑passe, surge uma janela onde pode introduzir a palavra‑passe.</li>
        <li>Pode guardar a palavra‑passe encriptada para não ter de a reintroduzir sempre (caixa "Guardar palavra‑passe").</li>
        <li>Com o botão "Remover palavra‑passe" pode criar uma cópia desencriptada do PDF e eliminar a palavra‑passe da base de dados.</li>
        </ul>

        <p><strong>2. Palavra‑passe mestre</strong></p>
        <ul>
        <li>A palavra‑passe mestre protege o acesso a todas as palavras‑passe de PDF guardadas.</li>
        <li><strong>Configuração:</strong> Vá a "Configurações → Gestor de palavras‑passe → Configurações da palavra‑passe mestre" e clique em "Configurar palavra‑passe mestre". Escolha uma palavra‑passe segura (pelo menos 8 caracteres).</li>
        <li><strong>Alteração:</strong> Após autenticação bem‑sucedida, pode alterar a palavra‑passe mestre.</li>
        <li><strong>Remoção:</strong> Se eliminar a palavra‑passe mestre, TODAS as palavras‑passe guardadas são irreversivelmente apagadas. Pode exportar uma cópia de segurança antes.</li>
        <li>Uma vez por sessão, deve autenticar‑se com a palavra‑passe mestre para aceder a funções protegidas (por exemplo, ver palavras‑passe).</li>
        </ul>

        <p><strong>3. Gestor de palavras‑passe (lista)</strong></p>
        <ul>
        <li>Em "Configurações → Gestor de palavras‑passe" abre uma tabela de todos os PDF guardados com as suas palavras‑passe encriptadas.</li>
        <li><strong>Sem palavra‑passe mestre:</strong> Só pode eliminar entradas – as palavras‑passe permanecem ocultas.</li>
        <li><strong>Com palavra‑passe mestre (autenticado):</strong> Pode ver, copiar, exportar e eliminar palavras‑passe.</li>
        <li><strong>Exportação:</strong> Escolha um formato (JSON, CSV, TXT) e guarde a lista. Se estiver definida uma palavra‑passe mestre, pode decidir se as palavras‑passe são exportadas em texto claro ou ainda encriptadas.</li>
        <li><strong>Importação:</strong> Um ficheiro ZIP exportado anteriormente com todas as configurações (incluindo palavras‑passe) pode ser reimportado através de "Configurações → Exportar/importar configurações". Atenção: os dados existentes serão substituídos!</li>
        </ul>

        <p><strong>4. Gerador de palavras‑passe</strong></p>
        <ul>
        <li>Na janela de diálogo da palavra‑passe (por exemplo, ao proteger um PDF) encontra um botão em forma de dado 🎲 à direita do campo de entrada.</li>
        <li>Clique nele para abrir o gerador de palavras‑passe. Pode definir o comprimento, conjuntos de caracteres (maiúsculas, minúsculas, dígitos, símbolos) e um separador para melhor legibilidade.</li>
        <li>A palavra‑passe gerada pode ser usada diretamente e copiada se necessário.</li>
        </ul>

        <p><strong>5. Notas de segurança importantes</strong></p>
        <ul>
        <li>As palavras‑passe guardadas são armazenadas encriptadas com AES‑256. A chave é derivada da sua palavra‑passe mestre (se definida) ou de um valor fixo (sem palavra‑passe mestre).</li>
        <li>Sem palavra‑passe mestre, as palavras‑passe estão encriptadas, mas a chave está incorporada no programa – um atacante com acesso aos seus ficheiros pode decifrá‑las. Recomenda‑se vivamente o uso de uma palavra‑passe mestre.</li>
        <li>A base de dados de palavras‑passe está no diretório `Data/passwords.json`. Faça cópias de segurança regulares, especialmente antes de remover a palavra‑passe mestre.</li>
        <li>Em caso de perda da palavra‑passe mestre, todas as palavras‑passe guardadas são irrecuperáveis.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Modo de inversão",
        'invert_mode_classic': "Clássico (inverter todas as cores)",
        'invert_mode_smart': "Inteligente (inverter apenas o brilho)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Limiar de escala de cinza",
        'gray_threshold_10': "10% (rigoroso)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Padrão)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (suave)",
        'threshold_changed': "Limiar definido para {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Limiar de escala de cinza – Explicação",
        'threshold_guide_text': "O limiar de escala de cinza determina quais pixéis no modo escuro inteligente são considerados 'cinzentos' e são invertidos.\n\n"
                                "• Um valor baixo (10%) inverte apenas tons de cinza quase perfeitos – os elementos coloridos permanecem completamente preservados.\n"
                                "• Um valor alto (50%) também inverte pixéis ligeiramente coloridos – isto aumenta o contraste, mas pode distorcer as cores.\n\n"
                                "O valor ideal depende do documento. Para documentos puramente de texto, 30–40% é frequentemente ideal, para gráficos coloridos prefira 10–20%.\n\n"
                                "Pode ajustar o valor a qualquer momento através do menu 'Definições' – o PDF será recarregado imediatamente.\n\n"
                                "Nota:\n* Fotos e imagens só podem ser exibidas corretamente no modo claro!\n* As definições de inversão só são exibidas quando o modo escuro está ativado.",
        'threshold_guide_voice': "O limiar de escala de cinza determina o quão fortemente o modo escuro inteligente intervém. Um valor baixo preserva as cores, um valor alto aumenta o contraste.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "A abrir PDF...",
        'progress_loading_document': "A carregar documento...",
        'progress_pdf_opened': "PDF aberto",
        'progress_creating_backup': "A criar cópia de segurança...",
        'progress_backup_description': "A proteger ficheiro original...",
        'progress_backup_created': "Cópia de segurança criada",
        'progress_backup_saved_as': "Guardado como: {0}",
        'progress_analyzing_start': "A iniciar análise...",
        'progress_searching_empty': "A procurar páginas vazias...",
        'progress_page_empty': "A página {0} está vazia",
        'progress_page_keep': "Manter página {0}",
        'progress_analysis_complete': "Análise concluída",
        'progress_empty_found': "Encontradas {0} páginas vazias",
        'progress_current_page': "Página atual",
        'progress_mark_delete': "A marcar para eliminar",
        'progress_range_selected': "Intervalo de páginas {0}-{1}",
        'progress_deleting_pages': "A eliminar {0} páginas",
        'progress_creating_new_pdf': "A criar novo PDF...",
        'progress_transferring_pages': "A transferir páginas",
        'progress_keeping_page': "A página {0} será mantida ({1}/{2})",
        'progress_saving_pdf': "A guardar PDF...",
        'progress_optimizing': "A otimizar tamanho do ficheiro...",
        'progress_finalizing': "A finalizar...",
        'progress_new_size': "Novo tamanho: {0:.2f} MB",
        'progress_cancelling': "A cancelar...",
        'progress_cancel_message': "{0} está a ser cancelado",
        'progress_pages_found_moving': "Encontradas {0} páginas, {1} para mover",

        # OCR-Fortschritt
        'ocr_status_analyzing': "A analisar PDF...",
        'ocr_status_optimizing': "Otimização de imagem em curso...",
        'ocr_status_recognizing': "Reconhecimento de texto em curso...",
        'ocr_status_embedding': "A incorporar texto...",
        'ocr_status_finalizing': "A finalizar PDF...",

        # PDF-Laden
        'progress_preparing': "A preparar...",
        'progress_loading': "A carregar PDF...",

        # Seitenoperationen
        'progress_deleting_title': "A eliminar páginas...",
        'progress_moving_title': "A mover páginas...",
        'pages_found': "Páginas encontradas",
        'progress_creating_new_order': "A criar nova ordem...",
        'progress_sorting_pages': "A ordenar páginas...",
        'progress_moving_to_begin': "Mover {0} páginas para o início",
        'progress_transferring_count': "Transferir {0} páginas",
        'progress_transferring_before_target': "Transferir páginas antes do destino",
        'progress_moving_pages': "Mover {0} páginas",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_protegido_",
        'filename_copy_suffix': "_Copia",
        'filename_page_single': "_Pagina_",
        'filename_page_range': "_Paginas_",
        'filename_export_page': "_Pagina_{0:03}",
        'filename_export_range': "_Paginas_{0}-{1}",
        'filename_export_multiple': "_Paginas_{0}",
        'filename_with_text': "_com_Texto",
        'filename_with_signature': "_com_Assinatura",
        'filename_with_image': "_com_Imagem",
        'filename_with_forms': "_com_Formas",
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
        'view_toggle_navbar': "Mostrar barra de botões",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Não é possível eliminar todas as páginas",
		'pages_cannot_delete_last_page': 'A última página não pode ser eliminada!',
		'pages_cannot_delete_all_pages': 'Deve permanecer pelo menos uma página no documento!',
		'delete_pages_confirm': 'Tem a certeza de que pretende eliminar {0} páginas?',
		'delete_pages_confirm_voice': 'Tem a certeza de que pretende eliminar {0} páginas?',
		'pages_deleted': '{0} páginas foram eliminadas com sucesso.',
		'warning': 'Aviso',
		'error': 'Erro',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nenhum formulário selecionado",
        'form_customized': "Formulário personalizado",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Selecionar",
        'btn_use': "Usar",
        'master_password_for_spasswords': "Para guardar e usar palavras-passe, primeiro tem de configurar uma palavra-passe mestra.\n\nDeseja configurar a palavra-passe mestra agora?",
        'open_saved_dialog_title': "Abrir ficheiro guardado",
        'open_saved_question': "Deseja abrir o ficheiro guardado agora?",
        'password': "Palavra-passe",
        'password_manager_master_required': "O gestor de palavras-passe só está disponível se uma palavra-passe mestra tiver sido configurada.\n\nDeseja configurar a palavra-passe mestra agora?",
        'password_master_required_for_select': "Para ver e selecionar palavras-passe guardadas, tem de se autenticar primeiro com a sua palavra-passe mestra.\n\nDeseja autenticar-se agora?",
        'password_not_available': "A palavra-passe selecionada não está disponível ou não pôde ser descifrada.",
        'password_options_title': "Opções de palavra-passe",
        'password_save_choice_change': "Definir nova palavra-passe",
        'password_save_choice_keep': "Usar palavra-passe existente",
        'password_save_choice_none': "Guardar não encriptado",
        'password_save_hint': "Configure primeiro uma palavra-passe mestra para guardar palavras-passe de forma segura.",
        'password_save_master_required': "Guardar palavra-passe (só possível com palavra-passe mestra)",
        'password_save_question': "O PDF atual está protegido por palavra-passe. Deseja usar a palavra-passe existente, definir uma nova ou guardar não encriptado?",
        'password_select': "Selecionar palavra-passe",
        'password_select_none': "Nenhuma palavra-passe selecionada.\n\nSelecione uma palavra-passe da lista.",
        'password_select_one': "Selecione exatamente uma palavra-passe.\n\nAssinalou várias palavras-passe.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",
        'filename_insert_suffix': "_com_insercao",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_paginas_eliminadas",
        'filename_pages_moved': "_paginas_movidas",
        'filename_rotated_all_suffix': "_todas_as_paginas_rodadas",
        'filename_rotated_suffix': "_pagina_rodada",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configuração dos nomes de ficheiro ao alterar PDF",
        'filename_keep_suffixes': "Manter extensões anteriores (ex., _com_texto)",
        'filename_keep_suffixes_false': "Substituir",
        'filename_keep_suffixes_true': "Manter",
        'filename_preview_label': "Pré-visualização do nome do ficheiro:",
        'filename_preview_overwrite_hint': "Pré-visualização não disponível – o original será sobrescrito.",
        'filename_separator': "Separador entre palavras",
        'filename_separator_none': "Sem separador",
        'filename_separator_space': "Espaço ( )",
        'filename_separator_underscore': "Sublinhado (_)",
        'filename_settings_saved': "Configurações de nome de ficheiro guardadas",
        'filename_settings_title': "Formatação do nome do ficheiro e backup",
        'filename_timestamp_position': "Posição do carimbo de data/hora",
        'filename_timestamp_position_after': "Após o nome base",
        'filename_timestamp_position_before': "Mesmo à frente",
        'filename_timestamp_position_end': "No final",
        'filename_use_timestamp': "Usar carimbo de data/hora",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Comportamento ao alterar:</b><ul><li>Eliminar e inserir páginas</li><li>Inserir texto, assinatura, imagem e formas</li><li>OCR</li></ul></html>",
        'backup_section': "Backup para operações de páginas (Eliminar, Mover)",
        'behavior_info': "Nota: Em 'Sobrescrever original', os carimbos de data/hora e sufixos são ignorados – o ficheiro mantém o seu nome.",
        'behavior_new_file': "Criar sempre um novo ficheiro (com carimbo de data/hora e sufixo)",
        'behavior_overwrite': "Sobrescrever original (nenhum ficheiro novo)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Todas as páginas foram rodadas.\n\nO original permaneceu inalterado.\nNovo ficheiro: {0}",
        'all_pages_rotated_voice': "Todas as páginas rodadas, novo ficheiro criado.",
        'empty_pages_deleted_new_file': "{0} páginas vazias foram eliminadas.\n\nO original permaneceu inalterado.\nNovo ficheiro: {1}",
        'empty_pages_deleted_voice': "{0} páginas vazias eliminadas, novo ficheiro criado.",
        'ocr_keep_original': "Manter original (abrir manualmente mais tarde)",
        'ocr_new_file_question': "O novo PDF pesquisável foi guardado em:\n{0}\n\nDeseja abri-lo agora?",
        'ocr_open_new': "Abrir novo ficheiro OCR",
        'ocr_original_kept': "O ficheiro original permanece aberto. O ficheiro OCR foi guardado.",
        'page_deleted_new_file': "A página {0} foi eliminada.\n\nO original permaneceu inalterado.\nNovo ficheiro: {1}",
        'page_deleted_voice': "Página {0} eliminada, novo ficheiro criado.",
        'page_rotated_new_file': "A página {0} foi rodada.\n\nO original permaneceu inalterado.\nNovo ficheiro: {1}",
        'page_rotated_voice': "Página {0} rodada, novo ficheiro criado.",
        'pages_deleted_new_file': "Foram eliminadas {0} páginas.\n\nO ficheiro original permaneceu inalterado.\nNovo ficheiro: {1}",
        'pages_deleted_new_file_voice': "{0} páginas eliminadas, novo ficheiro criado.",
        'pages_inserted_new_file': "Foram inseridas {0} páginas.\n\nO ficheiro original permaneceu inalterado.\nNovo ficheiro: {1}",
        'pages_inserted_new_file_ask': "Foram inseridas {0} páginas.\n\nO original permaneceu inalterado.\nNovo ficheiro: {1}\n\nDeseja abri-lo agora?",
        'pages_inserted_voice_new': "{0} páginas inseridas, novo ficheiro criado.",
        'pages_moved_new_file': "Foram movidas {0} páginas.\n\nO ficheiro original permaneceu inalterado.\nNovo ficheiro: {1}",
        'pages_moved_new_file_voice': "{0} páginas movidas, novo ficheiro criado.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Não mostrar novamente",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Configuração de backup</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup LIGADO</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Em todas as alterações que sobrescrevem o original</strong> (texto, assinatura, imagem, forma, OCR, rodar, inserir, eliminar/mover páginas) é <strong>automaticamente criado um backup com carimbo de data/hora</strong> antes de aplicar a alteração.</p>
                <p style="margin: 5px 0 5px 20px;">• O backup fica ao lado do ficheiro original (ex., <code>Documento_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Se também tiver ativado a opção <strong>„Sobrescrever original“</strong>, também é criado um backup.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup DESLIGADO</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nenhum backup é criado</strong> – nem ao sobrescrever, nem durante operações de páginas.</p>
                <p style="margin: 5px 0 5px 20px;">• O ficheiro original pode ser perdido irreversivelmente ao ser sobrescrito.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Recomendado apenas para utilizadores experientes!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Dica:</strong> A configuração de backup é independente da opção „Sobrescrever original“. Pode combinar ambas.<br>
                Pode ocultar esta mensagem permanentemente.
            </div>
        </div>
        """,
        'backup_info_title': "Comportamento do backup",
        'backup_info_voice': "Aviso sobre o comportamento do backup em operações de páginas. Backup ligado sobrescreve o original, backup desligado cria novo ficheiro.",
        'show_backup_info': "Informação sobre a configuração de backup",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Não mostrar novamente",
        'overwrite_enable_backup': "Ativar backup (recomendado)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Sobrescrever original</p>
            <p>Se ativar esta opção, as alterações (texto, assinatura, imagem, forma, OCR, rodar, inserir) são <strong>guardadas diretamente no original</strong> – <strong>nenhum ficheiro novo é criado</strong>.</p>
            <p>• O nome do ficheiro permanece inalterado.<br>
            • Os carimbos de data/hora e sufixos são ignorados.<br>
            • <strong>Sem backup, o original pode ser perdido irreversivelmente.</strong></p>
            <p style="color: #FFD700;">Recomendação: Ative adicionalmente a opção de backup para obter cópias de segurança automáticas.</p>
        </div>
        """,
        'overwrite_info_title': "Sobrescrever original",
        'overwrite_info_voice': "Aviso: Sobrescrever original – nenhum ficheiro novo. Backup recomendado.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Foram inseridas {0} páginas.\n\nO ficheiro original foi sobrescrito.\nFoi criado um backup.",
        'pages_inserted_overwrite_no_backup': "Foram inseridas {0} páginas.\n\nO ficheiro original foi sobrescrito.\nNÃO foi criado nenhum backup.",
        'texts_saved_overwrite_with_backup': "As alterações foram guardadas no original.\n\nFoi criado um backup.",
        'texts_saved_overwrite_no_backup': "As alterações foram guardadas no original.\n\nNÃO foi criado nenhum backup.",
        'texts_crosses_saved_new_file': "{0} {1} e {2} {3} foram inseridos.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",
        'texts_saved_new_file': "{0} {1} foram inseridos.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",
        'crosses_saved_new_file': "{0} {1} foram inseridos.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",
        'elements_saved_new_file': "{0} elementos foram inseridos.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",
        'signatures_saved_overwrite_with_backup': "A(s) assinatura(s) foi/foram guardada(s) no original.\n\nFoi criado um backup.",
        'signatures_saved_overwrite_no_backup': "A(s) assinatura(s) foi/foram guardada(s) no original.\n\nNÃO foi criado nenhum backup.",
        'images_saved_overwrite_with_backup': "A(s) imagem(ns) foi/foram guardada(s) no original.\n\nFoi criado um backup.",
        'images_saved_overwrite_no_backup': "A(s) imagem(ns) foi/foram guardada(s) no original.\n\nNÃO foi criado nenhum backup.",
        'forms_saved_overwrite_with_backup': "A(s) forma(s) foi/foram guardada(s) no original.\n\nFoi criado um backup.",
        'forms_saved_overwrite_no_backup': "A(s) forma(s) foi/foram guardada(s) no original.\n\nNÃO foi criado nenhum backup.",
        'signatures_saved_new_file': "Foram inseridas {0} assinaturas.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",
        'images_saved_new_file': "Foram inseridas {0} imagens.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",
        'forms_saved_new_file': "Foram inseridas {0} formas.\n\nO ficheiro original permaneceu inalterado.\nFoi criado um novo ficheiro.\n\nA carregar o novo PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Aviso: Este PDF contém páginas rodadas. O posicionamento pode estar incorreto.",
        'page_rotated_warning_title': "Página rodada detetada",
        'page_rotated_warning_message': "A página atual {0} está rodada {1}°.\n\nInserir elementos em páginas rodadas não é suportado.\n\nDeseja rodar a página para a posição vertical agora?",
        'page_rotated_warning_voice': "Aviso: A página está rodada. Por favor, rode-a primeiro.",
        'paste_on_rotated_page_simple_warning': "Inserção na página {0} impossível!\n\nEsta página está rodada {1}°.\n\nPor favor, rode primeiro a página para 0° (Menu: Editar → Alinhar página).\n\nAviso:\nO elemento anteriormente copiado será perdido se não guardar antes de rodar a página.",
        'paste_on_rotated_page_voice': "Inserção cancelada. A página está rodada. Por favor, alinhe primeiro a página.",
        'page_rotated_cancel': "Cancelar",
        'page_rotated_rotate_until_upright': "Rodar página repetidamente (até ficar vertical)",
        'page_rotated_now_upright': "A página está agora vertical. Pode agora inserir.",
        'page_rotated_still_not_upright': "Não foi possível rodar a página para a posição vertical. Por favor, corrija manualmente.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Ajuda: Corrigir páginas rodadas",
        'help_rotated_pages_voice': "A ajuda para corrigir páginas rodadas está a abrir.",
        'btn_help': "Ajuda",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problema: Página rodada – A inserção não funciona corretamente</p>

            <p>Se a inserção de textos, assinaturas ou formas numa página rodada não funcionar corretamente, pode corrigir a página com um editor de PDF externo.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solução com ferramenta externa (ex., Pré-visualização macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exportar página</strong><br>
                &nbsp;&nbsp;Clique no menu <strong>Ficheiro → Exportar como páginas</strong> ou utilize outro método para guardar a página desejada como um único PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Abrir página num programa externo</strong><br>
                &nbsp;&nbsp;Abra o PDF exportado num editor de PDF (ex., <strong>Pré-visualização macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rodar página</strong><br>
                &nbsp;&nbsp;Rode a página de modo a que fique vertical (na Pré-visualização: <strong>Ferramentas → Rodar</strong> ou <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Guardar</strong><br>
                &nbsp;&nbsp;Guarde a página corrigida (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Voltar a inserir a página no documento original</strong><br>
                &nbsp;&nbsp;Volte ao PDFDarkView e insira a página corrigida na posição desejada:<br>
                &nbsp;&nbsp;<strong>Editar → Inserir páginas</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativa: Rodar página no original</p>
                <p style="margin: 5px 0 5px 20px;">• Utilize a função de rotação integrada (<strong>Editar → Rodar página</strong>) para corrigir a página passo a passo.<br>
                • Após cada rotação, pode verificar se a inserção agora funciona.<br>
                • Esta é frequentemente a solução mais rápida – experimente primeiro!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Dica:</strong> Se encontrar frequentemente páginas rodadas, pode ocultar permanentemente o aviso no diálogo de inserção.<br>
                O posicionamento pode então estar incorreto – utilize esta opção apenas se conhecer as consequências.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Alinhar páginas",
        'menu_rotate_normalize_tooltip': "Rodar página ou repor para 0°",
        'normalize_current_page': "Trazer a página atual para a posição vertical (definir para 0°)",
        'normalize_all_pages': "Trazer todas as páginas para a posição vertical (definir para 0°)",
        'page_normalized': "A página {0} foi definida para a posição vertical.",
        'all_pages_normalized': "Todas as páginas foram definidas para a posição vertical.",
        'page_already_upright': "A página {0} já está vertical.",
        'all_pages_already_upright': "Todas as páginas já estão verticais.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>O PDF não contém texto pesquisável.</p><p>Deseja efetuar OCR para exportar para {0}?</p>",
        'export_ocr_voice': "O PDF não contém texto. É necessário OCR para exportar para {0}.",
        'export_no_ocr_possible': "Exportação sem OCR não é possível. Por favor, efetue OCR através do menu.",
        'ocr_failed_export_not_possible': "O OCR falhou. Não é possível efetuar a exportação.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "O PDF será aberto na Pré-visualização. Inicie aí o processo de impressão.",
        'print_preview_manual': "O PDF foi aberto. Execute o comando de impressão manualmente (ex., Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Fundir PDFs",
        'merge_pdfs': "Fundir PDFs",
        'merge_progress_title': "A fundir PDFs...",
        'merge_pdfs_list': "PDFs por ordem (Arraste e largue para ordenar)",
        'merge_add_pdf': "Adicionar PDF",
        'merge_remove': "Remover",
        'merge_move_up': "Para cima",
        'merge_move_down': "Para baixo",
        'merge_pdfs_info': "💡 Dica: Pode alterar a ordem arrastando e largando",
        'merge_no_pdfs': "Nenhum PDF selecionado. Clique em 'Adicionar PDF'.",
        'merge_info': "{0} PDFs selecionados (cerca de {1} páginas)",
        'merge_open_file': "Abrir ficheiro",
        'merge_merge': "Fundir",
        'merge_error': "Erro ao fundir",
        'merge_min_two_pdfs_error': "Selecione pelo menos dois ficheiros PDF para fundir.",
        'merge_select_pdfs': "Selecionar PDFs para fundir",
        'merge_error_file': "Erro ao processar",
        'merge_cancelled': "A fusão foi cancelada",
        'merge_preparing': "A preparar...",
        'merge_processing': "A processar PDF {0} de {1}",
        'merge_saving': "A guardar PDF fundido...",
        'merge_complete': "Concluído!",
        'merge_success_title': "Fusão bem-sucedida",
        'merge_success_voice': "{0} PDFs foram fundidos com sucesso.",
        'merge_success_message': "{0} PDFs foram fundidos com sucesso.\n\nO novo documento tem agora {1} páginas.\n\nNovo ficheiro:\n{2}\n\nLocalização de gravação:\n{3}\n{2}\n\nDeseja abrir este PDF?",
        'replace_file_title': "Substituir ficheiro?",
        'replace_file_message': "Já existe um PDF aberto. Deseja substituí-lo pelo novo ficheiro?",
        'btn_yes': "Sim",
        'btn_no': "Não",
        'filename_merge_suffix': "fundido",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "A abrir {0}...",
        'progress_merge_reading': "A ler {0}...",
        'progress_merge_adding': "A adicionar {0} páginas...",
        'progress_merge_optimizing': "A otimizar PDF...",
        'progress_merge_writing': "A escrever PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "fechar o PDF",
        'action_close_window': "fechar a janela",
        'action_open_new_pdf': "abrir um novo PDF",
        'action_quit_app': "sair da aplicação",
        'changes_saved': "As alterações foram guardadas.",
        'file_close_title': "Fechar ficheiro PDF",
        'save_before_action': "As alterações devem ser guardadas antes de {0}? Sim ou Não?",
        'save_before_action_voice': "As alterações devem ser guardadas antes de {0}? Sim ou Não?",
        'save_before_close_question': "As alterações devem ser guardadas antes de fechar? Sim ou Não?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF pesquisável criado:\n\n{0}\n\n<b>tente novamente se necessário",
        "ocr_rotate_title": "Alinhar páginas antes do OCR",
        "ocr_rotate_question": "O PDF contém páginas rodadas.\nDeseja alinhar todas as páginas a 0° antes do OCR?\nIsso melhora significativamente o reconhecimento de texto.",
        "ocr_rotate_yes": "Sim, alinhar",
        "ocr_rotate_no": "Não, iniciar OCR diretamente",
        "ocr_rotate_voice": "O PDF contém páginas rodadas. Todas as páginas devem ser alinhadas antes do OCR?",
        "ocr_not_performed_message": "Nenhum texto presente. Por favor, execute OCR (menu \"Editar\" → \"Executar OCR\" ou tecla Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Configurações de OCR",
        "ocr_language_btn": "Selecionar idioma do OCR",
        "ocr_language": "Idioma(s) do OCR",
        "ocr_language_current": "Idioma atual:",
        "ocr_param_info": "Informação sobre o parâmetro",

        "ocr_force_ocr_label": "Forçar OCR",
        "ocr_deskew_label": "Corrigir inclinação",
        "ocr_clean_label": "Limpar imagem",
        "ocr_oversample_label": "Resolução (DPI)",
        "ocr_pagesegmode_label": "Segmentação de página",
        "ocr_oem_label": "Modo do motor OCR",
        "ocr_optimize_label": "Compressão do PDF",
        "ocr_jobs_label": "Processos paralelos",
        "ocr_verbose_label": "Detalhe do log",

        "ocr_force_ocr_tooltip": "Forçar OCR em cada página, mesmo que o texto já exista",
        "ocr_deskew_tooltip": "Alinhar automaticamente digitalizações inclinadas",
        "ocr_clean_tooltip": "Remover ruído e artefactos da imagem",
        "ocr_oversample_tooltip": "Ampliar imagem antes do OCR para este DPI",
        "ocr_pagesegmode_tooltip": "Determina como a página é dividida em áreas de texto",
        "ocr_oem_tooltip": "Seleciona o motor OCR do Tesseract",
        "ocr_optimize_tooltip": "Nível de compressão do PDF de saída",
        "ocr_jobs_tooltip": "Número de processos OCR paralelos",
        "ocr_verbose_tooltip": "Nível de detalhe da saída do log",
        "ocr_settings_explain_btn": "Explicação",

        "ocr_force_ocr_explain": "Força o reconhecimento de texto em <b>cada</b> página, mesmo que já contenha texto.\n\nRecomendação: <b>Ativado</b> para PDFs digitalizados, <b>Desativado</b> para PDFs nativos com texto já existente.",

        "ocr_deskew_explain": "Corrige digitalizações ligeiramente inclinadas (até cerca de 5°).\n\nRecomendação: <b>Ativado</b> para documentos digitalizados, <b>Desativado</b> se as páginas já estiverem perfeitamente direitas.",

        "ocr_clean_explain": "Remove ruído, pontos e pequenos artefactos da imagem.\n<b>IMPORTANTE:</b> Para textos árabes, tailandeses ou vietnamitas com sinais diacríticos (pontos acima/abaixo das letras), esta opção deve ser <b>desativada</b>, caso contrário, caracteres importantes podem ser perdidos.",

        "ocr_oversample_explain": "Amplia a imagem <b>antes</b> do reconhecimento de texto para o DPI especificado.<br><br>• <b>72-150 DPI:</b> Muito rápido, mas baixa taxa de reconhecimento<br>• <b>200-300 DPI:</b> Intervalo ótimo (Padrão: 300)<br>• <b>400+ DPI:</b> Reconhecimento apenas ligeiramente melhor, mas ficheiros significativamente maiores<br><br>Recomendação: 300 DPI para escritas complexas (árabe, chinês, japonês), 200 DPI para línguas ocidentais.",

        "ocr_pagesegmode_explain": "Determina como o Tesseract divide a página em áreas de texto.\n\n• <b>3 - Automático (Padrão):</b> Bom para layouts mistos\n• <b>4 - Coluna única:</b> Para textos de coluna única\n• <b>5 - Bloco vertical:</b> Para escritas verticais (japonês, chinês)\n• <b>6 - Bloco de texto uniforme:</b> Ótimo para texto contínuo sem colunas\n• <b>11 - Imagem bruta:</b> Para más digitalizações / escrita manual\n\nRecomendação: <b>6</b> para documentos de texto simples, <b>3</b> para layouts complexos.",

        "ocr_oem_explain": "Seleciona o motor OCR do Tesseract.\n\n• <b>0 - Legacy:</b> Motor antigo (rápido, mas menos preciso)\n• <b>1 - LSTM:</b> Motor neural (mais lento, mas mais preciso)\n• <b>2 - Legacy + LSTM:</b> Combina ambos os resultados\n• <b>3 - Padrão (LSTM preferido):</b> Melhor escolha para a maioria dos casos\n\nRecomendação: <b>3</b> para máxima precisão de reconhecimento.",

        "ocr_optimize_explain": "Comprime o PDF de saída.\n\n• <b>0:</b> Sem otimização (processamento mais rápido)\n• <b>1:</b> Otimização leve (bom compromisso)\n• <b>2:</b> Otimização moderada\n• <b>3:</b> Otimização forte (ficheiro mais pequeno, mas mais lento)\n\nRecomendação: <b>1</b> para uso diário.",

        "ocr_jobs_explain": "Número de processos paralelos para OCR.\n\n• <b>1:</b> Lento, mas menor consumo de memória\n• <b>4-8:</b> Ótimo para processadores multi-core modernos\n• <b>12+:</b> Processamento apenas ligeiramente mais rápido com alto consumo de memória\n\nRecomendação: Número de núcleos de CPU (ex.: <b>4</b> em sistemas de 4 núcleos).",

        "ocr_verbose_explain": "Nível de detalhe da saída do log na consola.\n\n• <b>0:</b> Sem saída\n• <b>1:</b> Progresso e mensagens de estado\n• <b>2:</b> Saída detalhada\n• <b>3:</b> Saída de depuração completa (muito extensa)\n\nRecomendação: <b>1</b> para operação normal.",

        "ocr_reset_title": "Configurações redefinidas",
        "ocr_reset_message": "Todas as configurações de OCR foram redefinidas para os valores padrão.",
        "info_tooltip": "Mais informações sobre este parâmetro",
        "ocr_reset_defaults": "Redefinir para o padrão",

        "ocr_psm_0": "Automático (motor Legacy)",
        "ocr_psm_1": "Deteção automática de colunas",
        "ocr_psm_3": "Automático (Padrão)",
        "ocr_psm_4": "Coluna única",
        "ocr_psm_5": "Bloco vertical",
        "ocr_psm_6": "Bloco de texto uniforme",
        "ocr_psm_7": "Linha de texto única",
        "ocr_psm_8": "Palavra única",
        "ocr_psm_11": "Imagem bruta (sem análise de layout)",

        "ocr_oem_0": "Motor Legacy (rápido)",
        "ocr_oem_1": "Motor LSTM (neural, preciso)",
        "ocr_oem_2": "Legacy + LSTM combinado",
        "ocr_oem_3": "Padrão (LSTM preferido)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Idioma(s) do OCR...",
        "ocr_language_title": "Selecionar idioma(s) do OCR",
        "ocr_language_instruction": "Selecione o(s) idioma(s) para o reconhecimento de texto (OCR).\nAtenção: Vários idiomas vão em detrimento do desempenho e precisão!\nObterá os melhores resultados se selecionar apenas um idioma.",
        "ocr_language_predefined": "Combinações predefinidas",
        "ocr_language_custom": "Personalizado...",
        "ocr_language_selected": "Idiomas OCR selecionados",
        "ocr_language_changed": "Idioma OCR alterado para {0}",
        "ocr_language_auto_detect": "Os idiomas disponíveis são detetados automaticamente.",
        "ocr_language_none_found": "Nenhum dado de idioma do Tesseract encontrado! Por favor, instale os pacotes de idioma (ex.: 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Seleção de idioma personalizada",
        "ocr_language_available": "Idiomas disponíveis (instalados):",
        "ocr_language_select_hint": "Selecione um ou mais idiomas:",
        "ocr_language_confirm": "Aplicar",
        "ocr_language_reset": "Redefinir para o padrão (deu+eng+vie)",
        "ocr_language_priorities": "Idiomas recomendados (pré-instalados):",

        "select_all_languages": "Selecionar tudo",
        "clear_all_languages": "Limpar seleção",
        "install_language_packs": "Instalar pacotes de idioma em falta...",
        "install_hint": "💡 Dica: Nem todos os idiomas estão instalados no seu sistema. Através deste botão obterá ajuda para a instalação.",
        "ocr_language_install_title": "Instalação de pacotes de idioma do Tesseract",

        "ocr_missing_languages": "Pacotes de idioma OCR em falta",
        "ocr_missing_languages_message": "Os seguintes idiomas selecionados não estão instalados no seu sistema:\n\n{0}\n\nPor favor, instale os pacotes de idioma em falta (consulte a ajuda em 'Ajuda de instalação').\n\nDeseja abrir a ajuda de instalação agora?",
        "ocr_missing_languages_voice": "Pacotes de idioma em falta. Por favor, instale os idiomas em falta.",
        "ocr_install_help_now": "Abrir ajuda",
        "ocr_continue_anyway": "Tentar mesmo assim",
        "ocr_language_error_title": "Erro de idioma OCR",
        "ocr_language_error_message": "Erro durante o reconhecimento de texto: {0}\n\nPor favor, verifique as suas configurações de idioma OCR (Configurações → Idioma OCR).",
        "ocr_install_help_button": "Ajuda de instalação",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalar pacotes de idioma Tesseract</p>

        <p>Para que o OCR funcione num idioma específico, os dados de idioma correspondentes devem estar instalados no seu sistema. Siga as instruções para o seu sistema operativo:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Abra o <strong>Terminal</strong> (Finder → Programas → Utilitários → Terminal).</li>
        <li>Instale todos os idiomas disponíveis com:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Isto pode demorar alguns minutos.)</li>
        <li>Ou apenas idiomas individuais (ex.: vietnamita):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Com as versões atuais do Homebrew, pode ser necessário transferir manualmente o <code>*.traineddata</code> (ver abaixo).</li>
        <li>Após a instalação: Feche este diálogo e reabra a seleção de idioma OCR – os novos idiomas aparecerão automaticamente.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Abra um terminal (Ctrl+Alt+T).</li>
        <li>Instale o idioma desejado, por exemplo, para vietnamita:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Códigos de idioma importantes: <code>deu</code> (alemão), <code>eng</code> (inglês), <code>vie</code> (vietnamita), <code>spa</code> (espanhol), <code>fra</code> (francês), <code>ita</code> (italiano), <code>nld</code> (holandês), <code>fin</code> (finlandês), <code>swe</code> (sueco), <code>nor</code> (norueguês).</li>
        <li>Mostrar todos os pacotes disponíveis:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Transfira os ficheiros <code>*.traineddata</code> pretendidos de:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ex.: <code>vie.traineddata</code> para vietnamita).</li>
        <li>Copie os ficheiros para a pasta de idiomas do Tesseract, geralmente:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Ajuste de acordo com a instalação individual.)</li>
        <li>Reinicie a aplicação (ou reabra a seleção de idioma OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativa para todos os sistemas</p>
        <ul>
        <li>Instale o <strong>OCRmyPDF</strong> e o <strong>Tesseract</strong> com um gestor de pacotes à sua escolha. A maioria das instalações já contém alguns idiomas padrão (inglês, alemão, francês).</li>
        <li>Os idiomas em falta podem ser instalados a qualquer momento – a seleção de idioma OCR lista apenas os idiomas realmente existentes.</li>
        </ul>

        <hr>
        <p><b>✅ Após a instalação:</b> Não é necessário reiniciar a aplicação – os idiomas recentemente adicionados aparecerão imediatamente na lista.</p>
        <p><b>📖 Ajuda com códigos de idioma:</b> Uma lista completa está disponível na <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">documentação do Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Tipos de letra Noto Sans",
        "info_noto_font_voice": "Guia de instalação dos tipos de letra Noto Sans",
        "btn_info_noto_font_install": "Informação do tipo de letra",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Como instalar os tipos de letra Noto gratuitos do Google</h2>

        <p>Os <strong>tipos de letra Noto</strong> são uma família de tipos de letra open source do Google. O seu objetivo é não ver <em>"nenhum tofu"</em> (ou seja, sem caixas vazias □) e exibir corretamente cada caráter do padrão Unicode. São o complemento ideal para aplicações que precisam de exibir textos em muitas línguas diferentes.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalação no macOS</h3>

        <p><strong>Método 1: Com o Homebrew (para utilizadores avançados)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Método 2: Através do "Font Book" (Recomendado)</strong></p>

        <ol>
        <li>Transfira o pacote de tipos de letra oficial:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extraia o ficheiro ZIP</li>
        <li>Copie os ficheiros para <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalação no Windows (10 e 11)</h3>

        <p><strong>Método 1: Microsoft Store (Recomendado)</strong><br>
        Procure por "Google Noto Fonts" ou "Noto Sans" e clique em <strong>Instalar</strong>.</p>

        <p><strong>Método 2: Instalação manual</strong></p>

        <ol>
        <li>Transferir:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extrair ZIP</li>
        <li>Selecione os ficheiros .ttf / .otf</li>
        <li>Clique com o botão direito → <strong>Instalar</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ou<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nome\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalação no Linux</h3>

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

        <p>Verificação:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Gerir marcadores",
        "bookmark_add": "Adicionar marcador",
        "bookmark_add_tooltip": "Guardar página atual como marcador",
        "bookmark_remove": "Remover marcador",
        "bookmark_remove_tooltip": "Eliminar o marcador marcado",
        "bookmark_remove_all": "Remover todos",
        "bookmark_remove_all_tooltip": "Eliminar todos os marcadores deste PDF",
        "bookmark_jump": "Ir para o marcador",
        "bookmark_jump_tooltip": "Ir para a página selecionada",
        "bookmark_name": "Nome",
        "bookmark_page": "Página",
        "bookmark_no_bookmarks": "Nenhum marcador presente.\nClique em 'Adicionar' para guardar a página atual como marcador.",
        "bookmark_added": "Marcador para a página {0} adicionado: {1}",
        "bookmark_removed": "Marcador removido: {0}",
        "bookmark_all_removed": "Todos os marcadores foram removidos.",
        "bookmark_name_default": "Página {0}",
        "bookmark_name_prompt": "Nome para o marcador:\n(texto longo será abreviado para 50 caracteres)",
        "bookmark_name_prompt_title": "Nome do marcador",
        "bookmark_confirm_remove_all": "Tem a certeza de que deseja remover todos os {0} marcadores?",
        "menu_bookmarks": "Marcadores",
        "bookmark_manage": "Gerir marcadores",
        "bookmark_next": "Próximo marcador",
        "bookmark_prev": "Marcador anterior",
        "bookmark_page_display": "Página {0}",
        "bookmark_exists": "Já existe um marcador para esta página com este nome.",
        "bookmark_select_first": "Por favor, selecione primeiro um marcador.",
        "bookmark_confirm_remove": "Tem a certeza de que deseja remover o marcador 'Página {0}: {1}'?",
        "bookmark_jumped_to": "Saltou para o marcador '{0}' na página {1}.",
        "bookmark_jumped_to_voice": "Marcador {0}, página {1}",
        "btn_close": "Fechar",

        "bookmark_list": "Os seus marcadores",
        "bookmark_rename": "Renomear marcador",
        "bookmark_rename_tooltip": "Alterar o nome do marcador selecionado",
        "bookmark_rename_title": "Renomear marcador",
        "bookmark_rename_prompt": "Novo nome para o marcador na página {0}:\n(máx. 50 caracteres)",
        "bookmark_renamed": "O marcador '{0}' foi renomeado para '{1}'.",
        "bookmark_item_tooltip": "Página {0}: {1}\nDuplo clique para saltar",
        "bookmark_name_exists_question": "Já existe um marcador com o nome '{0}' nesta página.\nRenomear mesmo assim?",

        "context_bookmarks": "Marcadores",
        "context_bookmark_add_here": "Adicionar marcador para esta página",
        "context_bookmarks_existing": "Marcadores existentes:",
        "context_bookmarks_jump": "Ir para o marcador:",
        "context_bookmarks_none": "Nenhum marcador presente",
        "context_bookmarks_clear_all": "Remover todos os {0} marcadores",

        "bookmark_search_placeholder": "Pesquisar marcadores... (nome ou página)",
        "bookmark_search_results": "%d marcadores encontrados para \"%s\"",
        "bookmark_no_search_results": "Nenhum marcador encontrado para \"%s\"",
        "bookmark_no_search_results_label": "Nenhum resultado para \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Editar metadados do PDF",
        "metadata_title": "Título",
        "metadata_title_placeholder": "Título do documento",
        "metadata_title_tooltip": "O título do documento (exibido na barra de título)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Nome do autor",
        "metadata_author_tooltip": "O criador do documento",
        "metadata_subject": "Assunto",
        "metadata_subject_placeholder": "Assunto do documento",
        "metadata_subject_tooltip": "Uma breve descrição do conteúdo",
        "metadata_keywords": "Palavras-chave",
        "metadata_keywords_placeholder": "Palavras-chave separadas por vírgulas",
        "metadata_keywords_tooltip": "Palavras-chave para categorizar o documento",
        "metadata_creator": "Criador",
        "metadata_creator_placeholder": "Aplicação que criou o PDF",
        "metadata_creator_tooltip": "O software com o qual o documento foi criado",
        "metadata_producer": "Produtor",
        "metadata_producer_placeholder": "Aplicação que converteu o PDF",
        "metadata_producer_tooltip": "O software que converteu o PDF",
        "metadata_creation_date": "Data de criação",
        "metadata_creation_date_tooltip": "A data de criação do documento",
        "metadata_mod_date": "Data de modificação",
        "metadata_mod_date_tooltip": "A data da última modificação",
        "metadata_pdf_info": "📄 Informação do PDF",
        "metadata_pages": "Número de páginas",
        "metadata_file_size": "Tamanho do ficheiro",
        "metadata_pdf_version": "Versão do PDF",
        "metadata_encrypted": "Encriptado",
        "metadata_encrypted_yes": "Sim (protegido por palavra-passe)",
        "metadata_encrypted_no": "Não",
        "metadata_reload": "📂 Recarregar do PDF",
        "metadata_reset": "Descartar alterações",
        "metadata_reloaded": "Os metadados foram recarregados do PDF.",
        "metadata_reset_done": "Todos os campos de metadados foram redefinidos.",
        "metadata_no_file": "Nenhum ficheiro PDF carregado.",
        "metadata_save_error": "Erro ao guardar os metadados",
        "metadata_saved": "Os metadados foram guardados com sucesso.",
        "metadata_pdf_version_unknown": "PDF (desconhecido)",
        "metadata_saved_message": "Os metadados foram guardados com sucesso.",
        "metadata_saved_voice": "Metadados guardados.",

        "metadata_custom": "🔧 Metadados personalizados",
        "metadata_custom_placeholder": "{\n  \"meu_campo\": \"meu_valor\",\n  \"outro_campo\": 123\n}",
        "metadata_custom_tooltip": "Formato JSON para metadados personalizados (opcional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Modelo \"{0}\" selecionado - Duplo clique para inserir",
        "text_use_template": "Utilizar bloco de texto",
        "text_type": "Tipo",
        "text_search_templates": "Pesquisar blocos de texto...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informação de exportação / importação",
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

        <h3>📦 O que é exportado? (Visão geral)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Configurações gerais da aplicação</span></li>
            <li class="detail">• Modo escuro/claro</li>
            <li class="detail">• Inversão do modo escuro para imagens</li>
            <li class="detail">• Valor limite de cinza</li>
            <li class="detail">• Idioma</li>
            <li class="detail">• Geometria da janela</li>
            <li class="detail">• Modo de zoom</li>
            <li class="detail">• Navegação (Barra de navegação visível)</li>
            <li class="detail">• Saída de voz (ligado/desligado)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Configurações de backup</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nomeação de ficheiros (Timestamp, Separador, Sufixos)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Configurações para inserções de</span></li>
            <li class="detail">• Assinaturas</li>
            <li class="detail">• Texto e blocos de texto</li>
            <li class="detail">• Cruzes, imagens e formas</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Configurações de OCR</span></li>
            <li class="detail">• Idioma</li>
            <li class="detail">• Forçar OCR · Modo de página</li>
            <li class="detail">• Pré-processamento de imagem: Corrigir inclinação, Limpar, Sobreamostragem</li>
            <li class="detail">• Número de tarefas paralelas</li>
            <li class="detail">• Modo de inversão</li>
            <li class="detail">• Valor limite de cinza</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Marcadores</span></li>
            <li class="detail">• Todos os marcadores por ficheiro PDF (Página, Nome, Hora de criação)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Base de dados de palavras-passe</span></li>
            <li class="detail">• Palavras-passe de PDF guardadas (opcionalmente encriptadas ou texto simples)</li>
            <li class="detail">• Hash da palavra-passe mestra (se definida)</li>
            <li class="detail">• Dados de verificação</li>
        </ul>

        <h4>⚠️ Notas importantes</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Ao importar:</strong>
            <ul>
                <li><span class="warning">➜ TODAS as configurações atuais serão completamente substituídas</span></li>
                <li>• É obrigatório reiniciar a aplicação</li>
                <li>• As assinaturas, blocos de texto e marcadores existentes serão substituídos</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Palavra-passe mestra e modo de exportação:</strong>
            <ul>
                <li>• Quando a palavra-passe mestra está ativa, pode escolher:</li>
                <li>  - <span style="color: #98FB98;"><strong>Desencriptado</strong></span> (as palavras-passe estão em texto simples no ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Encriptado</strong></span> (apenas legível com a palavra-passe mestra no sistema de destino)</li>
                <li>• O hash da palavra-passe mestra é <strong>sempre</strong> armazenado encriptado</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Aviso de segurança:</strong>
            <ul>
                <li>• O ficheiro ZIP exportado contém dados sensíveis (<strong>palavras-passe, marcadores, assinaturas</strong>)</li>
                <li>• Por favor, guarde-o num local seguro (ex.: pen USB encriptada, gestor de palavras-passe)</li>
                <li>• Se o ficheiro for perdido, as palavras-passe de PDF guardadas serão perdidas irremediavelmente</li>
            </ul>
        </div>

        <h4>📁 Formato de exportação</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            As configurações são guardadas num único ficheiro ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Este ZIP contém o <code>settings.json</code> completo (da sua configuração), bem como possíveis ficheiros de imagem de assinatura incorporados e palavras-passe encriptadas.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Assinaturas - Guia",
        'signature_guide_html': """
        📝 <strong>Assinaturas - Guia rápido</strong><br>
        <ul>
        <li>Definir palavra-passe mestre</li>
        <li>Configurar assinaturas no menu <em>Definições</em> (tamanho, carimbo de data/hora, …)</li>
        <li>Inserir com <strong>CLIQUE DIREITO</strong> na posição desejada (palavra-passe mestre necessária uma vez por sessão)</li>
        <li>Mover assinatura com o rato ou teclas de seta</li>
        <li>Inserir várias assinaturas consecutivas</li>
        <li>Personalizar cada assinatura individualmente</li>
        <li>Rejeitar assinatura única</li>
        <li>Guardar / rejeitar todas as assinaturas de uma vez</li>
        <li>Alternativamente, também pode ser utilizada a barra de menu.</li>
        </ul>
        """,
        'signature_guide_voice': "Guia rápido para assinaturas. Definir palavra-passe mestre. Configurar assinaturas nas definições. Inserir com clique direito.",

        'image_guide_title': "Inserir imagens - Guia",
        'image_guide_html': """
        📷 <strong>Inserir imagens em PDF - Guia rápido</strong><br>
        <ol>
        <li>Clique direito na posição desejada</li>
        <li><em>„Inserir imagem“</em> → Selecionar imagem</li>
        <li>Posicionar imagem: Arrastar com o rato</li>
        <li>Ajustar tamanho: Arrastar nos cantos/bordas</li>
        <li>Manter proporção: Tecla <strong>[A]</strong></li>
        <li>Mais ajustes: Clique direito na imagem</li>
        </ol>
        <p><strong>Dica:</strong> No menu de contexto, pode ajustar as definições.</p>
        """,
        'image_guide_voice': "Guia rápido para imagens. Clique direito, inserir imagem, selecionar. Posicionar com rato, ajustar tamanho nos cantos. Proporção com tecla A.",

        'form_guide_title': "Inserir formas - Guia",
        'form_guide_html': """
        📐 <strong>Inserir formas em PDF - Guia rápido</strong><br>
        <ol>
        <li>Selecionar tipo de forma (retângulo, elipse, linha, seta)</li>
        <li>Clicar na posição:
            <ul>
            <li>Para retângulo/elipse: Um clique posiciona a forma</li>
            <li>Para linha/seta: Dois cliques para ponto inicial e final</li>
            </ul>
        </li>
        <li>Posicionar forma: Arrastar com o rato</li>
        <li>Ajustar tamanho: Arrastar nos cantos/bordas</li>
        <li>Guardar forma: <strong>Enter</strong></li>
        <li>Rejeitar forma: <strong>ESC</strong></li>
        <li>Mais ajustes: Clique direito na forma</li>
        </ol>
        <p><strong>Dica:</strong> No menu de contexto, pode ajustar as definições.</p>
        """,
        'form_guide_voice': "Guia rápido para formas. Selecionar tipo de forma. Para retângulo ou elipse clicar uma vez, para linha ou seta duas vezes. Posicionar com rato, ajustar tamanho nos cantos. Guardar com Enter, rejeitar com Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "anterior",
        "btn_next_result": "seguinte",
        "ocr_text_window": "Janela de texto OCR",
        "bookmark_existing": "Marcadores existentes",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Comparação OCR Mac - Windows",
        'ocr_method_mac_win_title': "Diferenças OCR entre Mac e Windows",
        'ocr_method_mac_win_voice': "Mac é melhor",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Diferenças entre macOS e Windows</strong></p>

        <p><strong>macOS (recomendado)</strong></p>
        <p>Ferramenta:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultado:</p>
        <ul>
        <li>Um PDF pesquisável com texto incorporado que preserva amplamente o layout original.</li>
        </ul>
        <p>Vantagens:</p>
        <ul>
        <li>Excelente qualidade de reconhecimento de texto (mesmo em páginas tortas).</li>
        <li>Preservação de gráficos vetoriais e fontes.</li>
        <li>Barra de progresso GUI através de avaliação de subprocesso.</li>
        <li>Controlo total sobre todos os parâmetros OCR (Deskew, Clean, Oversample, otimização).</li>
        <li>A pesquisa de texto está diretamente disponível na janela principal (vista PDF).</li>
        </ul>
        <p>Desvantagens:</p>
        <ul>
        <li>Requer ferramentas de sistema adicionais (ocrmypdf, Ghostscript, unpaper, pngquant – incluídas no pacote da aplicação).</li>
        <li>Tratamento de erros mais complexo (deadlocks, timeouts).</li>
        </ul>

        <p><strong>Windows (alternativa estável)</strong></p>
        <p>Ferramenta:</p>
        <ul>
        <li>pytesseract (ligação direta ao Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultado:</p>
        <ul>
        <li>Um PDF pesquisável que visualmente corresponde a um PDF de imagem, mas é pesquisável através do texto transparente.</li>
        </ul>
        <p>Vantagens:</p>
        <ul>
        <li>Nenhuma me vem à mente agora.</li>
        </ul>
        <p>Desvantagens:</p>
        <ul>
        <li>O PDF é essencialmente uma imagem com texto invisível; o layout pode desviar-se ligeiramente em documentos complexos (colunas, tabelas).</li>
        <li>Sem correção automática de inclinação (--deskew) ou limpeza de imagem (--clean).</li>
        <li>A barra de progresso GUI é atualizada apenas aproximadamente com base no número de páginas processadas.</li>
        <li>A velocidade OCR é ligeiramente mais lenta (pois cada página é processada individualmente).</li>
        <li>A pesquisa de texto é redirecionada para a janela de texto OCR.</li>
        </ul>

        <p><strong>Características comuns</strong></p>
        <ul>
        <li>Ambos os métodos criam um PDF pesquisável no mesmo diretório que o ficheiro de origem.</li>
        <li>As definições OCR (idioma, DPI, modo de segmentação de página, modo do motor OCR) podem ser configuradas através do OCRSettingsDialog e são válidas em ambas as implementações.</li>
        </ul>

        <p><strong>Recomendação:</strong></p>
        <ul>
        <li>macOS: O binário ocrmypdf fornece os melhores resultados – Compre um Mac e use a versão (PDFDarkView para Macs com chip Apple Silicon ou Intel). Os resultados OCR são melhores do que no Windows!</li>
        <li>Windows: Use a solução pytesseract. É estável e fornece qualidade totalmente suficiente para a maioria dos documentos.</li>
        </ul>

        <p><strong>Nota importante:</strong></p>
        <ul>
        <li>Ambas as versões estão totalmente integradas na interface do utilizador – o utilizador não nota qualquer diferença.</li>
        <li>O programa decide automaticamente qual o motor OCR a utilizar com base no sistema operativo.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Criar assinatura (a partir de digitalização)",
        "signature_create_title": "Selecionar assinatura digitalizada (PDF/imagem)",
        "image_pdf_filter": "Imagens e PDF",
        "signature_pdf_empty": "O PDF não contém páginas.",
        "signature_created_success": "Assinatura criada com sucesso: {0}",
        "signature_create_error": "Erro ao criar a assinatura:\n{0}",
        "rembg_missing": "rembg não está instalado.\nPor favor instale: pip install rembg\nErro: {0}",
        "signature_name_title": "Nome do ficheiro para a assinatura",
        "signature_name_message": "Por favor, insira um nome de ficheiro para a nova assinatura (será guardada como PNG com fundo transparente):",
        "signature_name_label": "Nome do ficheiro:",
        "signature_name_voice": "Insira o nome do ficheiro para a assinatura",
        "signature_processing": "Processamento em curso...",
        "signature_creation_title": "A criar assinatura",
        "signature_overwrite_warning": "O ficheiro '{0}' já existe. Sobrescrever?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Preparar PDF para assinatura",
        "signature_prepare_instruction":"Por favor, selecione um PDF que contenha numa única página uma assinatura digitalizada.\n\nPara um reconhecimento ideal, certifique-se de que:\n• A assinatura está escrita com tinta preta (caneta esferográfica ou caneta de ponta fina) em papel branco.\n• A assinatura está no terço superior de uma página A4 de outra forma vazia.\n• O PDF foi digitalizado com pelo menos 300 dpi.\n• A assinatura é clara e não demasiado fina.\n• Não existem padrões de fundo ou linhas perturbadoras.",
        "signature_prepare_voice":"Por favor, selecione um PDF com uma assinatura digitalizada. Preste atenção à boa qualidade e contraste.",
        "sig_thickness_label":"Espessura da linha:",
        "sig_thickness_normal":"Normal (fina)",
        "sig_thickness_bold":"Negrito (recomendado)",
        "sig_thickness_very_bold":"Muito negrito",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Adicionar idiomas GUI e OCR - Guia",
        'language_guide_title': "Adicionar idiomas GUI e OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Descarregue o ficheiro de tradução pretendido <code>translations_xy.py</code> de<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        e coloque-o no seguinte diretório:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Abra o seu navegador web.</li>
        <li>Vá para: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Procure no lado direito do ecrã por "Releases" e selecione o marcado com <strong>"latest"</strong>.</li>
        <li>Na página de lançamento seguinte, descarregue o ficheiro <code>Source Code.zip</code> no fundo.</li>
        <li>Descompacte o ficheiro ZIP.</li>
        <li>Procure na pasta descompactada todos os ficheiros de idioma de que necessita e copie-os para o diretório:<br/>
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
        "menu_watermark":"Inserir marca de água",
        "fullpage_text_watermark_title":"Texto como marca de água",
        "fullpage_image_watermark_title":"Imagem como marca de água",
        "filename_with_watermark":"_com_marca_de_agua",
        "watermark_text":"Texto:",
        "watermark_text_placeholder":"Seu texto de marca de água...",
        "watermark_font_family":"Fonte:",
        "watermark_font_size":"Tamanho da fonte:",
        "watermark_format":"Formatação:",
        "watermark_bold":"Negrito",
        "watermark_italic":"Itálico",
        "watermark_color":"Cor:",
        "watermark_choose_color":"Escolher cor...",
        "watermark_opacity":"Opacidade / Transparência:",
        "watermark_direction":"Direção de leitura:",
        "watermark_direction_l_r":"Esquerda → Direita",
        "watermark_direction_bl_tr":"Inferior esquerdo → Superior direito",
        "watermark_direction_tl_br":"Superior esquerdo → Inferior",
        "watermark_direction_b_t":"Inferior → Superior",
        "watermark_direction_t_b":"Superior → Inferior",
        "watermark_preview":"Pré-visualização:",
        "watermark_preview_sample":"Texto de exemplo",
        "watermark_empty_text":"Por favor, insira um texto.",
        "watermark_applied":"A marca de água foi aplicada a todas as páginas.",
        "watermark_saved":"Marca de água guardada.",
        "image_scale":"Tamanho:",
        "image_preview":"Pré-visualização da imagem:",
        "no_image_selected":"Nenhuma imagem selecionada",
        "browse":"Procurar...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redações",
        "redact_add_black": "Redação (preto)",
        "redact_add_white": "Redação (branco / apagar)",
        "redact_added_black": "Redação preta adicionada",
        "redact_added_white": "Redação branca adicionada",
        "redact_apply_all": "Aplicar todas as redações e guardar",
        "redact_discard_all": "Descartar todas as redações",
        "redact_discard": "Descartar esta redação",
        "no_redactions": "Nenhuma redação",
        "redact_confirm_title": "Aplicar redações permanentemente",
        "redact_confirm_message": "Aviso: As áreas marcadas serão permanentemente eliminadas (preto ou branco).\nSerá criada uma cópia de segurança (se ativada).\n\nContinuar?",
        "redact_apply": "Sim, redigir agora",
        "redact_saved": "{0} redação(ões) aplicada(s) e guardada(s) com sucesso.",
        "redact_saved_voice": "{0} redação(ões) aplicada(s)",
        "redact_error": "Erro durante a redação",
        "filename_redacted":"_redigido",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Inserir números de página',
        'page_numbers_format': 'Formato do número:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arábico)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romano minúsculo)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romano maiúsculo)',
        'page_numbers_format_letter': 'A, B, C ... (letras)',
        'page_numbers_format_custom': 'Personalizado',
        'page_numbers_custom_pattern': 'Padrão:',
        'page_numbers_custom_placeholder': 'ex. "Página {nummer}" ou "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Use {nummer} para o número de página atual e {total} para o total',
        'page_numbers_position': 'Posição:',
        'page_numbers_pos_tl': 'Superior esquerdo',
        'page_numbers_pos_tc': 'Superior central',
        'page_numbers_pos_tr': 'Superior direito',
        'page_numbers_pos_ml': 'Meio esquerdo',
        'page_numbers_pos_mc': 'Centrado',
        'page_numbers_pos_mr': 'Meio direito',
        'page_numbers_pos_bl': 'Inferior esquerdo',
        'page_numbers_pos_bc': 'Inferior central',
        'page_numbers_pos_br': 'Inferior direito',
        'page_numbers_margins': 'Margens:',
        'page_numbers_margin_x': 'Distância horizontal:',
        'page_numbers_margin_y': 'Distância vertical:',
        'page_numbers_range': 'Intervalo de páginas:',
        'page_numbers_all_pages': 'Todas as páginas',
        'page_numbers_custom_range': 'Intervalo personalizado',
        'page_numbers_from': 'De:',
        'page_numbers_to': 'Até:',
        'page_numbers_progress': 'A inserir números de página...',
        'page_numbers_start': 'A iniciar a inserção de números de página...',
        'page_numbers_cancel': 'Inserção de números de página cancelada',
        'page_numbers_success': 'Os números de página foram adicionados com sucesso.\n\nDeseja abrir o novo PDF?\n\n{0}',
        'page_numbers_complete': 'Números de página adicionados',
        'page_numbers_error_format': 'Erro ao inserir números de página: {0}',
        'page_numbers_content_type': 'Tipo de conteúdo:',
        'page_numbers_tab_simple': 'Número simples',
        'page_numbers_tab_range': 'Página X de Y',
        'page_numbers_tab_date': 'Data',
        'page_numbers_tab_custom': 'Texto livre',
        'page_numbers_range_format': 'Formato:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Página {aktuell} de {gesamt}',
        'page_numbers_range_custom': 'Personalizado',
        'page_numbers_range_placeholder': 'ex. "Página {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formato de data:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 de janeiro de 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Personalizado',
        'page_numbers_date_placeholder': 'ex. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posição:',
        'page_numbers_date_before': 'Data antes do número de página',
        'page_numbers_date_after': 'Data depois do número de página',
        'page_numbers_date_only': 'Apenas data (sem número de página)',
        'page_numbers_custom_text': 'Texto personalizado:',
        'page_numbers_custom_placeholder_text': 'Use {seite} para o número de página e {gesamt} para o total\nex. "Confidencial - Página {seite}" ou "{seite} de {gesamt}"',
        "filename_with_page_number":"_com_numero_de_pagina",
        "filename_with_page_declaration":"_com_declaracao_de_pagina",
        "filename_with_pagenumber":"_com_numero_de_pagina",
        "filename_with_date":"_com_data",
        "filename_with_my_page_declaration":"_com_declaracao_personalizada",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Alterações não guardadas",
        "unsaved_changes_message_darkmode": "Existem inserções não guardadas.\nDeseja guardá-las antes de alternar?",
        "save_and_switch": "Guardar e alternar",
        "discard_and_switch": "Alternar agora",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exportar páginas como imagens',
        'export_images_menu': 'Exportar como imagens (PNG/JPEG)',
        'export_images_format': 'Formato de imagem:',
        'export_images_dpi': 'Resolução (DPI):',
        'export_images_quality': 'Qualidade JPEG:',
        'export_images_range': 'Intervalo de páginas:',
        'export_images_all_pages': 'Todas as páginas',
        'export_images_custom_range': 'Intervalo personalizado',
        'export_images_from': 'De:',
        'export_images_to': 'Até:',
        'export_images_options': 'Opções:',
        'export_images_single_files': 'Cada página como ficheiro separado',
        'export_images_subfolder': 'Exportar para subpasta',
        'export_images_subfolder_info': 'Para a subpasta "nomePDF_imagens"',
        'export_images_same_folder': 'Na mesma pasta que o PDF',
        'export_images_apply_darkmode': 'Aplicar definições do PDFDarkView (Modo escuro)',
        'export_images_target_folder': 'Pasta de destino:',
        'export_images_browse': 'Procurar...',
        'export_images_preview': 'Pré-visualização:',
        'export_images_preview_info': 'Selecione as definições para a exportação',
        'export_images_preview_info_detail': '{0} páginas como {1}\nResolução: {2} DPI\nNome do ficheiro: {3}\n{4}',
        'export_images_select_folder': 'Selecione a pasta de destino',
        'export_images_start': 'A iniciar a exportação de imagens...',
        'export_images_progress': 'A exportar imagens...',
        'export_images_saving': 'A guardar página {0} de {1}...',
        'export_images_success': 'Exportação bem-sucedida!\n\n{0} imagens foram guardadas em:\n{1}',
        'export_images_complete': 'Exportação de imagens concluída',
        'export_images_open_folder': '📁 Abrir pasta',
        'export_images_cancel': 'Exportação de imagens cancelada',
        'export_images_error_format': 'Erro ao exportar imagens: {0}',
        'export_images_pdf2image_missing': 'A biblioteca "pdf2image" não está instalada.\n\nPor favor, instale-a com:\npip install pdf2image\n\nPara Windows, também precisa do Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Conversão PDF/A para arquivamento a longo prazo',
        'pdfa_menu': 'Conversão PDF/A (adequado para arquivo)',
        'pdfa_info': 'Converte o PDF para o formato PDF/A.\n\nO PDF/A é especialmente concebido para arquivamento a longo prazo e garante que o documento seja exibido corretamente no futuro.',
        'pdfa_standard': 'Norma PDF/A:',
        'pdfa_standard_select': 'Versão:',
        'pdfa_1': 'PDF/A-1 (simples, amplamente compatível)',
        'pdfa_2': 'PDF/A-2 (moderno, melhor compressão)',
        'pdfa_3': 'PDF/A-3 (versão mais recente, permite anexos)',
        'pdfa_standards_explanation': '📖 Explicação das normas:\n\n'
            '• PDF/A-1: Básico, compatível com sistemas mais antigos (cerca de 2005)\n'
            '• PDF/A-2: Mais moderno, melhor compressão, suporte a transparência (cerca de 2011)\n'
            '• PDF/A-3: Versão mais recente, permite a incorporação de anexos (cerca de 2013)\n\n'
            'Recomendação: PDF/A-2 é um bom compromisso entre compatibilidade e funcionalidades modernas.',
        'pdfa_options': 'Opções:',
        'pdfa_compress_enable': 'Comprimir PDF (ficheiro mais pequeno)',
        'pdfa_metadata_preserve': 'Preservar metadados (título, autor, etc.)',
        'pdfa_target_folder': 'Pasta de destino:',
        'pdfa_browse': 'Procurar...',
        'pdfa_select_folder': 'Selecione a pasta de destino',
        'pdfa_ocr_info_unknown': '🔍 Não foi possível verificar o conteúdo do texto.',
        'pdfa_ocr_info_not_needed': '✅ Texto disponível - OCR não é necessário.\nO PDF/A pode ser criado diretamente.',
        'pdfa_ocr_info_recommended': '⚠️ Não foi encontrado texto suficiente.\n\nPara PDFs pesquisáveis, recomendamos executar o OCR primeiro.\nNota: O PDF/A funciona sem OCR - mas o texto não será pesquisável.',
        'pdfa_ocr_info_error': '❌ Erro ao verificar: {0}',
        'pdfa_start': 'A iniciar a conversão PDF/A...',
        'pdfa_progress': 'Conversão PDF/A em curso...',
        'pdfa_success': 'Conversão PDF/A bem-sucedida!\n\nGuardado como:\n{0}\n\nDeseja abrir o novo PDF?',
        'pdfa_complete': 'Conversão PDF/A concluída',
        'pdfa_cancel': 'Conversão PDF/A cancelada',
        'pdfa_error_format': 'Erro durante a conversão PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'A biblioteca "ocrmypdf" não está instalada.\n\nPor favor, instale-a com:\npip install ocrmypdf',
        'btn_convert': 'Converter',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Otimizar PDF (reduzir tamanho do ficheiro)',
        'optimize_menu': 'Otimizar PDF (tamanho do ficheiro)',
        'optimize_info': 'Reduz o tamanho do ficheiro PDF através de vários métodos de otimização.\n\nQuanto maior o nível de compressão, menor o ficheiro - com possível perda de qualidade nas imagens.',
        'optimize_level': 'Nível de compressão:',
        'optimize_level_low': 'Baixo (rápido, pouca poupança)',
        'optimize_level_medium': 'Médio (bom compromisso)',
        'optimize_level_high': 'Alto (grande poupança)',
        'optimize_level_maximum': 'Máximo (poupança máxima, lento)',
        'optimize_level_explanation': 'Recomendação: "Médio" é um bom compromisso entre velocidade e tamanho do ficheiro.',
        'optimize_options': 'Opções:',
        'optimize_compress_images': 'Comprimir imagens (reduzir qualidade JPEG)',
        'optimize_clean_objects': 'Remover objetos não utilizados',
        'optimize_preserve_metadata': 'Preservar metadados (título, autor, etc.)',
        'optimize_image_quality': 'Qualidade da imagem:',
        'optimize_range': 'Intervalo de páginas:',
        'optimize_all_pages': 'Todas as páginas',
        'optimize_custom_range': 'Intervalo personalizado',
        'optimize_from': 'De:',
        'optimize_to': 'Até:',
        'optimize_target_folder': 'Pasta de destino:',
        'optimize_browse': 'Procurar...',
        'optimize_select_folder': 'Selecione a pasta de destino',
        'optimize_info_box': 'Informação',
        'optimize_info_text': 'A otimização pode demorar vários minutos para PDFs grandes.\n\nAs imagens são guardadas com qualidade reduzida, o que pode reduzir significativamente o tamanho do ficheiro.',
        'optimize_start': 'A iniciar a otimização do PDF...',
        'optimize_progress': 'A otimizar PDF...',
        'optimize_cancel': 'Otimização do PDF cancelada',
        'optimize_complete': 'Otimização do PDF concluída',
        'optimize_error_format': 'Erro durante a otimização do PDF:\n\n{0}',
        'optimize_success_message': 'Otimização do PDF bem-sucedida!\n\nGuardado como:\n{0}\n\nAntes: {1}\nDepois: {2}\nPoupança: {3:.1f}%\n\n{4}\n\nDeseja abrir o PDF otimizado?',
        'optimize_success_message_no_size': 'Otimização do PDF bem-sucedida!\n\nGuardado como:\n{0}\n\nInformação de tamanho não disponível.\n\nDeseja abrir o PDF otimizado?',
        'optimize_result_positive': 'O ficheiro foi reduzido em {0:.1f}%.',
        'optimize_result_zero': 'Nenhuma alteração no tamanho do ficheiro.',
        'optimize_result_negative': 'O ficheiro aumentou {0:.1f}%.\nA otimização foi ignorada, o ficheiro original foi preservado.',
        'btn_optimize': 'Iniciar otimização',
        'filename_optimize_low_suffix': '_otimizado_baixo',
        'filename_optimize_medium_suffix': '_otimizado',
        'filename_optimize_high_suffix': '_otimizado_alto',
        'filename_optimize_maximum_suffix': '_otimizado_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Cortar PDF',
        'crop_menu': 'Cortar PDF (Crop)',
        'crop_range': 'Aplicar a:',
        'crop_all_pages': 'Todas as páginas',
        'crop_current_page': 'Apenas a página atual',
        'crop_values': 'Valores de corte (em pontos):',
        'crop_left': 'Esquerda:',
        'crop_right': 'Direita:',
        'crop_top': 'Superior:',
        'crop_bottom': 'Inferior:',
        'crop_presets': 'Predefinições:',
        'crop_preset_white': 'Detetar margens brancas',
        'crop_reset': 'Repor',
        'crop_mouse_hint': '🖱️ Arraste um retângulo para selecionar aproximadamente a área.\nDepois pode ajustar os valores com precisão nas SpinBoxes.\nO ajuste manual com o rato não é possível.',
        'crop_apply': 'Cortar',
        'crop_scope_all': 'Todas as páginas',
        'crop_scope_current': 'Página atual',
        'crop_new_size': 'Novo tamanho: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nenhum PDF carregado',
        'crop_preview_error': 'Erro ao carregar a pré-visualização',
        'crop_start': 'A iniciar o corte...',
        'crop_progress': 'A cortar PDF...',
        'crop_success': 'PDF cortado com sucesso!\n\nGuardado como:\n{0}\n\nDeseja abrir o PDF cortado?',
        'crop_complete': 'Corte concluído',
        'crop_cancel': 'Corte cancelado',
        'crop_error_format': 'Erro durante o corte:\n\n{0}',
        'filename_crop_suffix': '_cortado',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Achatar PDF (Flatten)',
        'flatten_menu': 'Achatar PDF (Flatten)',
        'flatten_info': 'Achatar um PDF "queima" todos os elementos editáveis no conteúdo da página.\n\nDepois disso, os campos de formulário, anotações, textos, cruzes, assinaturas, imagens e formas já não são editáveis individualmente.',
        'flatten_explanation_title': '📖 Para que serve isto?',
        'flatten_explanation_text': 'O achatamento é necessário nas seguintes situações:\n\n'
            '• 📄 Pretende preparar o documento para impressão\n'
            '• 🔒 Pretende impedir que alguém altere os campos de formulário\n'
            '• 📎 Pretende "incorporar" permanentemente anotações e comentários no documento\n'
            '• 🖼️ Pretende ancorar permanentemente textos, cruzes, assinaturas, imagens e formas no documento\n'
            '• 📦 Pretende preparar o ficheiro para arquivamento\n\n'
            'O achatamento torna o PDF mais pequeno e evita que os elementos sejam movidos ou eliminados acidentalmente.',
        'flatten_what_title': 'O que é achatado?',
        'flatten_what_list': '• ✅ Campos de formulário (campos de texto, caixas de verificação, botões)\n'
            '• ✅ Anotações (comentários, realces, notas)\n'
            '• ✅ Sobreposições (textos, cruzes, assinaturas, imagens, formas)',
        'flatten_options': 'Opções:',
        'flatten_forms': 'Achatar campos de formulário',
        'flatten_annotations': 'Achatar anotações',
        'flatten_overlays': 'Achatar sobreposições (textos, cruzes, assinaturas, imagens, formas)',
        'flatten_target_folder': 'Pasta de destino:',
        'flatten_browse': 'Procurar...',
        'flatten_select_folder': 'Selecione a pasta de destino',
        'flatten_warning': '⚠️ Importante: O achatamento é um processo irreversível!\n\nApós o achatamento, os elementos editáveis já não podem ser alterados ou eliminados individualmente.\nCrie uma cópia de segurança antecipadamente, se necessário.',
        'flatten_apply': 'Achatar',
        'flatten_start': 'A iniciar o achatamento...',
        'flatten_progress': 'A achatar PDF...',
        'flatten_success': 'PDF achatado com sucesso!\n\nGuardado como:\n{0}\n\nDeseja abrir o PDF achatado?',
        'flatten_complete': 'Achatamento concluído',
        'flatten_cancel': 'Achatamento cancelado',
        'flatten_error_format': 'Erro durante o achatamento:\n\n{0}',
        'filename_flatten_suffix': '_achatado',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Sobreposição de PDF (Overlay)',
        'overlay_menu': 'Sobreposição de PDF (Overlay)',
        'overlay_info': 'Coloca um PDF (sobreposição) sobre outro PDF.\n\nO PDF de sobreposição é colocado sobre o PDF base. Isto é útil para marcas de água, logótipos, cabeçalhos ou carimbos.',
        'overlay_explanation_title': '📖 Para que serve isto?',
        'overlay_explanation_text': 'A sobreposição é necessária nas seguintes situações:\n\n'
            '• 🏢 Colocar um logótipo de empresa como marca de água em cada página\n'
            '• 📄 Colocar um cabeçalho num PDF vazio\n'
            '• 🖊️ Colocar uma sobreposição de carimbo num documento\n'
            '• 🔖 Colocar uma marca de água em todas as páginas\n'
            '• 📑 Colocar uma sobreposição de formulário num modelo',
        'overlay_type': 'Tipo de sobreposição:',
        'overlay_type_fullpage': 'Página inteira (cobrindo)',
        'overlay_type_transparent': 'Página inteira (transparente - recomendado)',
        'overlay_type_stamp': 'Carimbo (posicionável)',
        'overlay_type_info_fullpage': '📄 O PDF de sobreposição é colocado exatamente sobre toda a página.\nO fundo branco pode ser removido para que apenas o conteúdo fique visível.',
        'overlay_type_info_transparent': '🔍 O PDF de sobreposição é colocado sobre toda a página com fundo transparente.\nO fundo branco é removido automaticamente - ideal para marcas de água e logótipos!',
        'overlay_type_info_stamp': '🖊️ O PDF de sobreposição é posicionado e dimensionado como um carimbo.\nPerfeito para logótipos, carimbos ou assinaturas em posições específicas.',
        'overlay_remove_background': 'Remover fundo branco:',
        'overlay_remove_background_enable': 'Remover o fundo branco do PDF de sobreposição (torna a sobreposição transparente)',
        'overlay_remove_background_tooltip': 'Remove as áreas brancas do PDF de sobreposição para que o texto subjacente fique visível.',
        'overlay_threshold': 'Valor de limiar:',
        'overlay_threshold_hint': '(1-254, mais alto = mais branco é removido)',
        'overlay_select_file': 'Selecionar PDF de sobreposição:',
        'overlay_file_placeholder': 'Por favor, selecione um ficheiro PDF para a sobreposição',
        'overlay_browse': 'Procurar...',
        'overlay_select_overlay': 'Selecionar PDF de sobreposição',
        'overlay_range': 'Intervalo de páginas:',
        'overlay_all_pages': 'Todas as páginas',
        'overlay_custom_range': 'Intervalo personalizado',
        'overlay_from': 'De:',
        'overlay_to': 'Até:',
        'overlay_position': 'Posição:',
        'overlay_position_center': 'Centro',
        'overlay_position_top_left': 'Superior esquerdo',
        'overlay_position_top_right': 'Superior direito',
        'overlay_position_bottom_left': 'Inferior esquerdo',
        'overlay_position_bottom_right': 'Inferior direito',
        'overlay_size': 'Tamanho:',
        'overlay_size_original': 'Tamanho original',
        'overlay_size_fit_page': 'Ajustar à página',
        'overlay_size_custom': 'Personalizado (%)',
        'overlay_opacity': 'Transparência:',
        'overlay_target_folder': 'Pasta de destino:',
        'overlay_browse_folder': 'Procurar...',
        'overlay_select_folder': 'Selecione a pasta de destino',
        'overlay_warning': '⚠️ Nota: O PDF de sobreposição é colocado sobre o PDF base e "queimado" nele.\n\nOs elementos do PDF de sobreposição já não podem ser editados individualmente após o salvamento.',
        'overlay_apply': 'Sobrepor',
        'overlay_start': 'A iniciar a sobreposição...',
        'overlay_progress': 'A sobrepor PDF...',
        'overlay_success': 'PDF sobreposto com sucesso!\n\nGuardado como:\n{0}\n\nDeseja abrir o PDF sobreposto?',
        'overlay_complete': 'Sobreposição concluída',
        'overlay_cancel': 'Sobreposição cancelada',
        'overlay_error_format': 'Erro durante a sobreposição:\n\n{0}',
        'overlay_no_file': 'Nenhum PDF de sobreposição selecionado.\n\nPor favor, selecione um ficheiro PDF para sobrepor.',
        'filename_overlay_suffix': '_sobreposto',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extrair imagens do PDF',
        'extract_images_menu': 'Extrair todas as imagens',
        'extract_images_info': 'Extrai todas as imagens do PDF e guarda-as como ficheiros separados.\n\nAs imagens são guardadas no seu formato original ou convertidas para um formato selecionado.',
        'extract_images_format': 'Formato de imagem:',
        'extract_images_quality': 'Qualidade JPEG:',
        'extract_images_options': 'Opções:',
        'extract_images_subfolder': 'Extrair para subpasta ("nomePDF_imagens")',
        'extract_images_unique': 'Apenas imagens únicas (evitar duplicados)',
        'extract_images_range': 'Intervalo de páginas:',
        'extract_images_all_pages': 'Todas as páginas',
        'extract_images_custom_range': 'Intervalo personalizado',
        'extract_images_from': 'De:',
        'extract_images_to': 'Até:',
        'extract_images_target_folder': 'Pasta de destino:',
        'extract_images_browse': 'Procurar...',
        'extract_images_select_folder': 'Selecione a pasta de destino',
        'extract_images_info_box': 'Informação',
        'extract_images_info_text': 'A extração pode demorar vários minutos para PDFs grandes.\n\nAs imagens são guardadas com o seu nome original (página_imagem).',
        'extract_images_extract': 'Extrair',
        'extract_images_start': 'A iniciar a extração...',
        'extract_images_progress': 'A extrair imagens...',
        'extract_images_success': '✅ Imagens extraídas com sucesso!\n\n{0} imagens foram guardadas em:\n{1}',
        'extract_images_complete': 'Extração de imagens concluída',
        'extract_images_cancel': 'Extração cancelada',
        'extract_images_error_format': 'Erro ao extrair imagens:\n\n{0}',
        'extract_images_open_folder': '📁 Abrir pasta',
        'extract_images_no_images': 'Nenhuma imagem encontrada no PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Várias páginas numa página (N-Up)',
        'nup_menu': 'Várias páginas numa página (N-Up)',
        'nup_info': 'Organiza várias páginas PDF numa página.\n\nIdeal para impressões compactas, resumos ou folhetos.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Pré-visualização:',
        'nup_preview_info': '{0} páginas → {1} páginas por folha → {2} folhas\nLayout: {3}',
        'nup_order': 'Ordem:',
        'nup_order_horizontal': 'Horizontal (linha a linha)',
        'nup_order_vertical': 'Vertical (coluna a coluna)',
        'nup_order_horizontal_reverse': 'Horizontal inverso',
        'nup_order_vertical_reverse': 'Vertical inverso',
        'nup_range': 'Intervalo de páginas:',
        'nup_all_pages': 'Todas as páginas',
        'nup_custom_range': 'Intervalo personalizado',
        'nup_from': 'De:',
        'nup_to': 'Até:',
        'nup_options': 'Opções:',
        'nup_margins': 'Margens:',
        'nup_margin_between': 'Espaçamento entre páginas:',
        'nup_page_numbers': 'Inserir números de página',
        'nup_target_folder': 'Pasta de destino:',
        'nup_browse': 'Procurar...',
        'nup_select_folder': 'Selecione a pasta de destino',
        'nup_create': 'Criar',
        'nup_start': 'A iniciar N-Up...',
        'nup_progress': 'A criar N-Up...',
        'nup_success': 'N-Up criado com sucesso!\n\nGuardado como:\n{0}\n\nDeseja abrir o novo PDF?',
        'nup_complete': 'N-Up concluído',
        'nup_cancel': 'N-Up cancelado',
        'nup_error_format': 'Erro durante N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Alterar tamanho da página',
        'pagesize_menu': 'Alterar tamanho da página',
        'pagesize_info': 'Altera o tamanho da página do PDF.\n\nO conteúdo é automaticamente ajustado ao novo tamanho.',
        'pagesize_format': 'Formato:',
        'pagesize_select': 'Selecione um formato standard:',
        'pagesize_custom': 'Tamanho personalizado:',
        'pagesize_width': 'Largura:',
        'pagesize_height': 'Altura:',
        'pagesize_orientation': 'Orientação:',
        'pagesize_portrait': 'Retrato',
        'pagesize_landscape': 'Paisagem',
        'pagesize_scale_options': 'Opções de escala:',
        'pagesize_fit': 'Ajustar (manter proporção)',
        'pagesize_stretch': 'Esticar (distorcer)',
        'pagesize_center': 'Centrar (tamanho original)',
        'pagesize_range': 'Intervalo de páginas:',
        'pagesize_all_pages': 'Todas as páginas',
        'pagesize_custom_range': 'Intervalo personalizado',
        'pagesize_from': 'De:',
        'pagesize_to': 'Até:',
        'pagesize_target_folder': 'Pasta de destino:',
        'pagesize_browse': 'Procurar...',
        'pagesize_select_folder': 'Selecione a pasta de destino',
        'pagesize_apply': 'Aplicar',
        'pagesize_start': 'A iniciar a alteração do tamanho da página...',
        'pagesize_progress': 'A alterar tamanho da página...',
        'pagesize_success': 'Tamanho da página alterado com sucesso!\n\nGuardado como:\n{0}\n\nDeseja abrir o novo PDF?',
        'pagesize_complete': 'Alteração do tamanho da página concluída',
        'pagesize_cancel': 'Alteração do tamanho da página cancelada',
        'pagesize_error_format': 'Erro ao alterar o tamanho da página:\n\n{0}',
        'pagesize_preview_info': 'Novo tamanho: {0} x {1} pt',
        'filename_pagesize_suffix': '_novo_tamanho',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informação do PDF',
        'pdf_info_menu': 'Mostrar informação do PDF',
        'pdf_info_voice': 'A mostrar informação do PDF',
        'pdf_info_error': 'Erro ao mostrar informação do PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Mostrar atalhos de teclado",
        "shortcuts_dialog_title": "Atalhos de teclado",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FICHEIRO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Abrir PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Fechar PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Guardar como...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Proteger documento</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Imprimir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Imprimir imediatamente (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Sair da aplicação</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORTAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportar como Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportar como DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportar como TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportar como imagens (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extrair imagens</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PROCESSAMENTO DE DOCUMENTOS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Várias páginas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Conversão PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Achatar PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Sobrepor PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Otimizar PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDITAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Pesquisar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Adicionar marcador</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Gerir marcadores</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Próximo marcador</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Marcador anterior</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Executar OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 GESTÃO DE PÁGINAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rodar página atual</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rodar todas as páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizar página atual</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizar todas as páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Eliminar páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extrair páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Inserir páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Mover páginas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Fundir PDFs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Alterar tamanho da página</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INSERIR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Inserir texto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Inserir cruz</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Inserir assinatura 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Inserir assinatura 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Inserir imagem</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Inserir retângulo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Inserir elipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Inserir linha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Inserir seta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Inserir números de página</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Marca de água de texto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Marca de água de imagem</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDAÇÕES</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redação (preto)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redação (branco)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Aplicar todas as redações</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANÇADO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Cortar PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Editar metadados</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Alternar modo Escuro/Claro</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Mostrar janela de texto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Largura da página (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Duas páginas (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Resumo (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DEFINIÇÕES</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Gestão de palavras-passe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Definições de OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Definições de assinatura</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatação de nomes de ficheiros</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exportar definições</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importar definições</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMAÇÃO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Mostrar informação do PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Ativar/desativar saída de voz</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Focar barra de menus</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nova versão disponível",
        "update_available_message": "Há uma nova versão <b>{0}</b>.\n\nVisite a página de lançamento para baixar a atualização:\n{1}",
        "update_available_voice": "Nova versão {0} disponível. Baixe a atualização da página do GitHub.",
        "update_open_release": "Abrir página de lançamento",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Baixar todas as traduções",
        "ask_download_all_translations": """Além do alemão, inglês e vietnamita, há {total_languages} outros idiomas de interface disponíveis.\n\nDevem ser fornecidos / atualizados?\n\nNota:\nIdiomas desnecessários podem ser excluídos manualmente mais tarde no diretório:\n{translations_path}
        \nSe cancelar, pode baixar os idiomas de interface mais tarde através do menu 'Ferramentas → Atualizar traduções'.""",
        "menu_update_translations": "Atualizar traduções",
        "translations_updated": "Traduções atualizadas",
        "translations_update_success": "{} traduções foram atualizadas com sucesso ({} novas, {} atualizadas).",
        "translations_update_error": "Erro ao atualizar traduções",
        "translations_update_no_changes": "Todas as traduções já estão atualizadas.",
        "translations_update_offline": "Sem conexão com a Internet. Não foi possível atualizar as traduções.",
        "translations_update_in_progress": "Traduções estão sendo atualizadas em segundo plano...",
        "translations_downloading": "Baixando traduções...",
        "translations_path_hint": "Diretório do usuário para traduções",
        "translations_update_not_available_title": "Atualização não disponível",
        "translations_update_not_available_message": """A atualização de traduções está disponível apenas na versão instalada.\n\nNo modo de desenvolvimento, as traduções já estão atualizadas.""",
        "translations_update_no_internet_title": "Sem conexão com a Internet",
        "translations_update_no_internet_message": """Não foi possível estabelecer conexão com a Internet.\n\nAs traduções não podem ser baixadas do GitHub.\n\nSoluções possíveis:
        • Verifique sua conexão com a Internet
        • Desative temporariamente qualquer firewall
        • Tente novamente mais tarde
        \nVocê também pode baixar as traduções manualmente do GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "A atualização já está em andamento",
        "btn_retry": "Tentar novamente",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Bem-vindo ao PDF Dark View",
        "welcome_title_not_supported": "Bem-vindo ao PDF Dark View",
        "welcome_message": "Bem-vindo ao PDF Dark View!\n\nO idioma do seu sistema foi detectado como '{language}'.\nDeseja usar este idioma para a interface do usuário?\n\nVocê pode alterar o idioma a qualquer momento em 'Configurações → Idioma'.",
        "welcome_message_language_not_available": "Bem-vindo ao PDF Dark View!\n\nO idioma do seu sistema foi detectado como '{language}'.\nEste idioma ainda não está instalado.\n\nDeseja baixar agora as traduções para {language} do GitHub?\n\n(O idioma será então usado automaticamente para a interface do usuário.)",
        "welcome_message_language_not_supported": "Bem-vindo ao PDF Dark View!\n\nO idioma do seu sistema foi detectado como '{language}'.\nInfelizmente, ainda não há traduções para este idioma.\n\nA interface do usuário será exibida em {fallback_language}.\n\nVocê pode alterar o idioma a qualquer momento em 'Configurações → Idioma'.\nSe desejar, você também pode contribuir com uma tradução para o seu idioma:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Sim, usar idioma do sistema",
        "welcome_keep_english": "Não, manter inglês",
        "welcome_download_language": "Sim, baixar {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "O programa está sendo encerrado",

    }

