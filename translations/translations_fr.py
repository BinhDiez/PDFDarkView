
# ============================================
# translations_fr.py - Dictionnaire français
# Complètement trié par catégories
# Commentaires en allemand pour cohérence
# ============================================

def load_french_strings():
    """Charge toutes les chaînes françaises"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View par BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Ouvrir PDF",
        'btn_text_window': "Texte OCR",
        'btn_first': "Première page",
        'btn_prev': "Page précédente",
        'btn_next': "Page suivante",
        'btn_last': "Dernière page",
        'btn_print': "Imprimer",
        'btn_darkmode_light': "Mode clair",
        'btn_darkmode_dark': "Mode sombre",
        'btn_delete_pages': "Supprimer pages",
        'btn_extract_pages': "Extraire pages",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Annuler",
        'btn_save': "Enregistrer",
        'btn_close': "Fermer",
        'btn_delete': "Supprimer",
        'btn_delete_all': "Tout supprimer",
        'btn_copy': "Copier",
        'btn_export': "Exporter",
        'btn_show': "Afficher mdp",
        'btn_hide': "Cacher mdp",
        'btn_authenticate': "S'authentifier",
        'btn_settings': "Paramètres",
        'btn_protect': "Protéger",
        'btn_remove_password': "Enlever mot de passe",
        'btn_manage': "Gestionnaire mots de passe",
        'btn_retry': "Réessayer",
        'btn_select_all': "Tout sélectionner",
        'btn_clear_selection': "Effacer sélection",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Page {0} sur {1}",
        'page_count': "sur {0}",
        'goto_page': "Aller à la page",
        'page_simple': "Page {0}",
        'full_view_page': "Vue pleine page {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Entrer terme + Entrée",
        'search_results': "Résultats : {0} sur {1}",
        'search_nav_hint': "Entrée : suivant  (Maj+Entrée : précédent)",
        'search_no_results': "Aucun résultat",
        'search_error': "Erreur de recherche",
        'search_active': "Champ de recherche activé",
        'search_closed': "Recherche terminée",
        'search_position': "Page {0} {1}",
        'search_pos_top': "tout en haut",
        'search_pos_upper': "en haut",
        'search_pos_middle': "milieu",
        'search_pos_lower': "en bas",
        'search_pos_bottom': "tout en bas",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Reconnaissance de texte terminée avec succès !",
        'ocr_success_title': "OCR réussi",
        'ocr_success_message': "Le document est maintenant interrogeable.",
        'ocr_failed': "Échec OCR",
        'ocr_in_progress': "OCR en cours",
        'ocr_preparing': "Préparation du PDF...",
        'ocr_analyzing': "Analyse du PDF...",
        'ocr_optimizing': "Optimisation d'image...",
        'ocr_recognizing': "Reconnaissance de texte...",
        'ocr_embedding': "Intégration du texte...",
        'ocr_finalizing': "Finalisation du PDF...",
        'ocr_not_available': "OCR non disponible",
        'ocr_install_message': "Outils OCR introuvables.\n\nVeuillez installer :\n• Tesseract : brew install tesseract\n• OCRmyPDF : pip install ocrmypdf",
        'ocr_required': "OCR nécessaire",
        'ocr_question': "Le PDF ne contient pas de texte interrogeable.\nVoulez‑vous lancer l’OCR pour permettre {0} ?",
        'ocr_perform': "Lancer OCR",
        'ocr_later': "Plus tard",
        'ocr_starting': "Lancement OCR garanti...",
        'ocr_success_voice': "OCR réussi. Le PDF est maintenant interrogeable.",
        'ocr_partial_success': "L’OCR a été effectué, mais des problèmes sont survenus lors du remplacement.\n\nLa version interrogeable a été enregistrée sous :\n{0}\n\nErreur : {1}",
        'ocr_partial_title': "OCR partiellement réussi",
        'ocr_partial_voice': "OCR effectué, mais remplacement échoué.",
        'original_file': "Fichier original :",
        'old_size': "Ancienne taille :    {0} octets",
        'new_size': "Nouvelle taille : {0} octets",
        'size_change': "Changement : {0}{1} octets",
        'backup_created_file': "Sauvegarde créée :\n{0}",
        'backup_not_created': "Sauvegarde : non créée (paramètre désactivé)",
        'page_header': "=== Page {0} ===\n{1}\n",
        'scanned_page_header': "=== Page {0} (numérisée) ===\n[Cette page ne contient que du texte scanné]\n[Veuillez effectuer l’OCR manuellement]\n",
        'scanned_warning': "⚠️ TEXTE NUMÉRISÉ - OCR NÉCESSAIRE",
        'guaranteed_title': "PDF interrogeable créé",
        'guaranteed_message': "<b>Version interrogeable garantie créée !</b>\n\nL’OCR automatique ayant échoué, un PDF alternatif interrogeable a été créé :\n\n{0}\n\n<b>Ce fichier contient :</b>\n• Texte extrait (si disponible)\n• Indications pour les pages scannées\n• Il est entièrement interrogeable",
        'guaranteed_voice': "PDF interrogeable garanti créé.",
        'instruction_title': "INSTRUCTION POUR OCR",
        'instruction_file': "Fichier original : {0}",
        'instruction_text': "La reconnaissance automatique de texte (OCR) a échoué.\nVeuillez effectuer l’OCR manuellement :\n\n1. AVEC OCRmyPDF (ligne de commande) :\n   ocrmypdf --force-ocr \"[FICHIER]\" \"sortie.pdf\"\n\n2. AVEC ADOBE ACROBAT (macOS/Windows) :\n   • Ouvrir le PDF dans Acrobat\n   • Outils > Modifier le PDF\n   • Choisir 'Reconnaître le texte'\n\n3. AVEC APERÇU (macOS) :\n   • Ouvrir le PDF dans Aperçu\n   • Fichier > Exporter...\n   • Filtre Quartz : 'Reduce File Size'\n   • Activer 'Effectuer l’OCR'\n\n4. SERVICES EN LIGNE :\n   • smallpdf.com/fr/ocr-pdf\n   • ilovepdf.com/fr/ocr-pdf\n   • adobe.com/fr/acrobat/online/pdf-to-word.html",
        'instruction_created': "Instruction OCR créée",
        'instruction_created_message': "Une instruction détaillée a été créée :\n\n{0}\n\nVeuillez suivre les étapes pour l’OCR manuel.",
        'instruction_created_voice': "Instruction OCR créée.",
        'ocr_impossible': "OCR impossible",
        'ocr_impossible_message': "Impossible d’effectuer l’OCR.\n\nVeuillez traiter '{0}' manuellement avec un logiciel d’OCR.",
        'ocr_impossible_voice': "OCR impossible. Veuillez traiter manuellement.",
        'emergency_title': "OCR d’urgence",
        'emergency_message': "Un PDF d’urgence a été créé :\n\n{0}\n\nVeuillez traiter ce fichier manuellement avec l’OCR.",
        'emergency_voice': "PDF d’urgence créé. Veuillez effectuer l’OCR manuellement.",
        'critical_error': "Erreur critique",
        'critical_error_message': "Impossible de démarrer l’OCR.\n\nVeuillez redémarrer le programme et\nvérifier l’installation de l’OCR.",
        'critical_error_voice': "Erreur OCR critique",
        'ocr_question_html': "<p>Le PDF ne contient pas de texte interrogeable.<p>Voulez‑vous lancer l’OCR pour permettre <b>{0}</b> ?</p>",
        'ocr_question_voice': "OCR nécessaire. Le PDF ne contient pas de texte interrogeable. Voulez‑vous lancer l’OCR pour permettre {0} ?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "aucun PDF chargé",
        'no_pdf_message': "Aucun PDF n’est chargé",
        'pdf_not_found': "Fichier PDF introuvable",
        'file_size': "Taille du fichier",
        'bytes': "octets",
        'kb': "Ko",
        'mb': "Mo",
        'backup_created': "Sauvegarde créée",
        'backup_disabled': "Sauvegarde désactivée",
        'backup_activated': "Création de sauvegarde activée",
        'backup_deactivated': "Création de sauvegarde désactivée",
        'backup_status': "Sauvegarde : {0}",
        'backup_on': "✔ activée",
        'backup_off': "✘ désactivée",
        'close_pdf': "Fermeture PDF : {0}",
        'pdf_not_found_format': "Fichier PDF introuvable : {0}",
        'error_pdf_load_format': "Erreur lors du chargement du PDF : {0}",
        'load_failed_format': "Chargement échoué :\n{0}",
        'decrypted_suffix': "(déchiffré)",
        'decryption_failed': "Déchiffrement échoué.",
        'decryption_error': "Erreur lors du déchiffrement",
        'decryption_success': "Déchiffrement réussi",
        'decryption_success_message': "Le PDF a été déchiffré et enregistré sous :\n\n{0}",
        'decryption_success_voice': "PDF déchiffré et enregistré.",
        'password_remove_error': "Erreur lors de la suppression du mot de passe",
        'save_unencrypted': "Enregistrer PDF non chiffré sous",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Enregistrer sous...",
        'save_copy': "Enregistrer une copie",
        'save_success': "PDF enregistré sous : {0}",
        'save_encrypted': "PDF protégé enregistré sous : {0}",
        'save_error': "Impossible d’enregistrer le PDF",
        'encryption_question': "Voulez‑vous protéger le PDF par mot de passe ?",
        'encryption_yes': "Oui",
        'encryption_no': "Non",
        'encryption_cancel': "Annuler",
        'save_cancel': "Enregistrement annulé",
        'save_encrypted_voice': "Fichier chiffré et enregistré.",
        'save_success_voice': "Le fichier PDF a été enregistré non chiffré.",
        'save_error_format': "Impossible d’enregistrer le PDF :\n{0}",
        'export_pages_success': "Export Pages réussi",
        'export_pages_error': "Échec export Pages",
        'export_pages_error_format': "Échec export Pages : {0}",
        'export_word_success': "Export Word réussi",
        'export_word_error': "Échec export Word",
        'export_word_error_format': "Échec export Word : {0}",
        'export_text_success': "Export texte réussi",
        'export_text_error': "Échec export texte",
        'export_text_error_format': "Échec export texte : {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Mot de passe requis",
        'password_enter': "Veuillez entrer le mot de passe",
        'password_confirm': "Confirmer le mot de passe",
        'password_new': "Nouveau mot de passe",
        'password_current': "Mot de passe actuel",
        'password_save': "Enregistrer le mot de passe (chiffré)",
        'password_saved': "✓ Mot de passe pour ce fichier enregistré",
        'password_wrong': "Mot de passe incorrect",
        'password_mismatch': "Les mots de passe ne correspondent pas",
        'password_too_short': "Mot de passe trop court",
        'password_min_length': "Le mot de passe doit comporter au moins 4 caractères",
        'password_strength': "Force du mot de passe",
        'password_strength_very_weak': "Très faible",
        'password_strength_weak': "Faible",
        'password_strength_medium': "Moyen",
        'password_strength_strong': "Fort",
        'password_strength_very_strong': "Très fort",
        'password_char_count': "({0} caractères)",
        'password_match': "✓ Correspondance",
        'password_no_match': "✗ Les mots de passe ne correspondent pas",
        'password_show': "Afficher",
        'password_hide': "Cacher",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Gestionnaire mots de passe",
        'password_table_filename': "Nom de fichier",
        'password_table_password': "Mot de passe",
        'password_count': "{0} mot{1} de passe enregistré{2}",
        # Anpassung: Für Französisch müssen wir maskuline/Plural-Formen handhaben.
        # Wir verwenden zwei Platzhalter: {0} = Anzahl, {1} = "s" für Plural, {2} = "s" für Adjektiv?
        # Der Einfachheit halber hier eine vereinfachte Form:
        # 'password_count': "{0} mot de passe enregistré{1}",
        # mit {1} = "s" im Plural. Wir passen den Code in tr() an? – Nein, wir lassen es erstmal so.
        # Eigentlich müssen wir für Plural die Keys _plural nutzen, aber hier belassen wir es vorerst.
        'password_count_singular': "",
        'password_count_plural': "s",
        'password_none': "Aucun mot de passe enregistré",
        'password_copied': "{0} mot{1} de passe copié{2}",
        'password_copied_singular': "",
        'password_copied_plural': "s",
        'password_delete_confirm': "Voulez‑vous vraiment supprimer le mot de passe pour '{0}' ?",
        'password_delete_multiple': "Voulez‑vous vraiment supprimer les {0} mots de passe sélectionnés ?",
        'password_delete_all_confirm': "Voulez‑vous vraiment supprimer les {0} mots de passe enregistrés ?",
        'password_deleted': "{0} mot{1} de passe supprimé{2}",
        'password_deleted_singular': "",
        'password_deleted_plural': "s",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "s",
        'password_all_deleted': "Tous les mots de passe ont été supprimés",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Générateur de mot de passe",
        'generator_generated': "Mot de passe généré :",
        'generator_regenerate': "Regénérer",
        'generator_copy': "Copier",
        'generator_use': "Utiliser",
        'generator_settings': "Paramètres",
        'generator_length': "Longueur :",
        'generator_group_every': "Séparateur tous les",
        'generator_group_chars': "caractères.   Séparateur :",
        'generator_uppercase': "Majuscules (A-Z)",
        'generator_lowercase': "Minuscules (a-z)",
        'generator_digits': "Chiffres (0-9)",
        'generator_symbols': "Symboles (!@#$%^&*)",
        'generator_exclude': "Exclus :",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Mot de passe maître requis",
        'master_password_setup': "Configurer mot de passe maître",
        'master_password_change': "Changer mot de passe maître",
        'master_password_enter': "Veuillez entrer votre mot de passe maître",
        'master_password_choose': "Choisissez un mot de passe maître fort (au moins 8 caractères)",
        'master_password_new': "Veuillez entrer votre nouveau mot de passe maître",
        'master_password_confirm': "Confirmer le mot de passe",
        'master_password_authenticate': "S'authentifier",
        'master_password_success': "Mot de passe maître configuré avec succès.",
        'master_password_changed': "Mot de passe maître modifié avec succès.",
        'master_password_removed': "Mot de passe maître et tous les mots de passe supprimés.",
        'master_password_remove': "Supprimer mot de passe maître",
        'master_password_remove_confirm': "Êtes‑vous SÛR de vouloir supprimer TOUS les mots de passe ?\n\nCette action est IRRÉVERSIBLE !",
        'master_password_export_before': "Voulez‑vous d’abord exporter une sauvegarde ?",
        'master_password_export_delete': "Exporter & supprimer",
        'master_password_delete_now': "Supprimer maintenant",
        'master_password_for_signatures': "Pour utiliser les signatures, vous devez configurer un mot de passe maître.\n\nVoulez‑vous configurer un mot de passe maître maintenant ?",
        'master_password_for_private': "Pour utiliser les modèles de texte privés, vous devez configurer un mot de passe maître.\n\nVoulez‑vous configurer un mot de passe maître maintenant ?",
        'master_password_info': """
            <b>🔐 SANS MOT DE PASSE MAÎTRE :</b><br>
            • Pas d’affichage, copie ni export des mots de passe possible<br>
            • La suppression des mots de passe est toujours possible (même sans mot de passe maître)<br><br>

            <b>🔐 AVEC MOT DE PASSE MAÎTRE :</b><br>
            • Toutes les fonctions disponibles après authentification<br>
            • Les mots de passe sont chiffrés avec le mot de passe maître<br>
            • Longueur minimale : 8 caractères<br>
            • Stockage sécurisé par hachage SHA-256<br><br>

            <b>IMPORTANT :</b><br>
            • En cas de perte du mot de passe maître : mots de passe irrécupérables<br>
            • Lors de la suppression du mot de passe maître : TOUS les mots de passe sont effacés<br>
            • Option d’export disponible avant suppression<br>
            • Le mot de passe maître peut être modifié à tout moment
        """,
        'signature_auth_disabled': "Désactiver la demande de mot de passe pour les signatures",
        'template_auth_disabled': "Désactiver la demande de mot de passe pour les modèles privés",
        'master_password_for_signatures_settings': "Pour utiliser les signatures, vous devez configurer un mot de passe maître.\n\nAllez dans Paramètres – Gestionnaire de mots de passe",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Protéger le PDF",
        'protect_info': "Le fichier '{0}' sera protégé par mot de passe.",
        'protect_instruction': "Veuillez saisir deux fois le mot de passe souhaité pour protéger le document, ou utilisez le générateur de mot de passe à droite du champ de saisie.",
        'protect_success': "Le PDF a été protégé avec succès et enregistré sous :\n{0}\n\nMot de passe : {1}\n\nVoulez‑vous ouvrir le PDF protégé maintenant ?",
        'protect_open': "Oui",
        'protect_skip': "Non",
        'protect_error': "Erreur lors de la protection du PDF",
        'protect_open_title': "ouvrir PDF protégé",
        'protect_question': "Terminé. Voulez‑vous ouvrir le PDF protégé maintenant ? Oui ou Non ?",
        'password_cancel': "Dialogue de mot de passe annulé",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Supprimer des pages",
        'pages_extract': "Extraire des pages",
        'pages_insert': "Insérer des pages",
        'pages_move': "Déplacer des pages",
        'pages_delete_options': "Options de suppression",
        'pages_delete_empty': "Supprimer toutes les pages vides",
        'pages_delete_current': "Supprimer la page actuelle",
        'pages_delete_range': "Supprimer une plage de pages",
        'pages_extract_options': "Options d’extraction",
        'pages_extract_current': "Extraire la page actuelle",
        'pages_extract_range': "Extraire une plage de pages",
        'pages_insert_position': "Position d’insertion",
        'pages_insert_before': "Insérer avant la page :",
        'pages_insert_select': "Choisir un PDF",
        'pages_insert_none': "Aucun PDF sélectionné",
        'pages_move_source': "Pages à déplacer",
        'pages_move_from': "De la page :",
        'pages_move_to': "À la page :",
        'pages_move_target': "Position cible",
        'pages_move_before': "Déplacer avant la page :",
        'pages_move_hint': "Note : page 1 = début, {0} = fin",
        'pages_range_invalid': "La page de début doit être inférieure ou égale à la page de fin.",
        'pages_position_invalid': "La position cible ne doit pas se trouver dans la plage à déplacer.",
        'pages_no_pdf_selected': "Aucun PDF sélectionné.",
        'pages_deleted': "{0} pages ont été supprimées.",
        'pages_extracted': "Extrait : {0}\nEnregistré sous : {1}\nTaille du fichier : {2:.1f} Ko",
        'pages_inserted': "{0} pages insérées",
        'pages_moved': "{0} pages ont été déplacées.",
        'pages_deleted_none': "Aucune page supprimée.",
        'pages_delete_progress': "Suppression des pages...",
        'pages_deleted_with_backup': "{0} pages ont été supprimées.\n\nSauvegarde : {1}",
        'pages_deleted_voice': "Une sauvegarde a été créée et {0} pages supprimées.",
        'info': "Info",
        'error_dialog_creation': "Impossible de créer la boîte de dialogue",
        'extract_page_single': "Extraire la page {0}",
        'extract_page_range': "Extraire les pages {0}–{1}",
        'extract_success_voice': "Pages extraites avec succès",
        'extract_error_format': "Erreur lors de l’extraction : {0}",
        'pages_inserted_voice': "{0} pages insérées.",
        'insert_error_format': "Erreur lors de l’insertion : {0}",
        'pages_move_progress': "Déplacement des pages...",
        'pages_moved_with_backup': "{0} pages ont été déplacées.\n\nSauvegarde : {1}",
        'move_success_title': "Déplacement réussi",
        'pages_moved_voice': "{0} pages déplacées avec succès",
        'mark_removed': "Marquage retiré de la page {0}",
        'mark_empty': "Page {0} marquée comme vide",
        'mark_export_removed': "Marquage d’export retiré de la page {0}",
        'mark_export': "Page {0} marquée pour export",
        'no_empty_pages': "Aucune page vide marquée pour suppression",
        'delete_empty_confirm': "Voulez‑vous supprimer les {0} pages vides marquées ?",
        'delete_empty_confirm_voice': "Supprimer maintenant les {0} pages vides marquées ? Oui ou Non.",
        'empty_pages_deleted': "{0} pages vides supprimées",
        'no_export_pages': "Aucune page marquée pour export",
        'overwrite_title': "Remplacer le fichier existant",
        'overwrite_question': "Le fichier\n\n{0}\n\nexiste déjà.\nVoulez‑vous le remplacer ?",
        'overwrite_voice': "Remplacer le fichier existant ? Oui ou Non.",
        'page_skipped': "Page {0} ignorée",
        'export_complete': "Export terminé.",
        'export_complete_voice': "L’export est terminé.",
        'no_pages_exported': "Aucune page exportée",
        'export_cancelled': "Export annulé",
        'pages_exported': "{0} pages exportées vers {1}",
        'export_page_title': "Exporter la page",
        'page_exported': "Page {0} exportée vers {1}",
        'export_error': "Erreur lors de l’export",
        'export_marked_title': "Exporter les pages marquées",
        'rotate_all_title': "pivoter toutes les pages",
        'rotate_all_question': "Voulez‑vous faire pivoter toutes les pages de 90° vers la droite ?",
        'rotate_all_voice': "Voulez‑vous faire pivoter toutes les pages de 90° vers la droite ? Oui ou Non ?",
        'all_pages_rotated': "Toutes les pages pivotées",
        'page_rotated': "Page {0} pivotée",
        'rotate_error': "Impossible de pivoter la page",
        'delete_page_confirm': "Voulez‑vous supprimer la page {0} ?",
        'delete_page_confirm_voice': "Voulez‑vous vraiment supprimer la page {0} ? Oui ou Non.",
        'page_deleted': "Page {0} supprimée",
        'delete_error': "Impossible de supprimer la page",
        'pages_deleted_voice': "{0} pages supprimées",
        'pages_exported_split': "{0} pages ont été exportées avec succès.",
        'pages_skipped': "{0} pages ont été ignorées.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extraire pages (avancé)",
        'pdf_splitter_title': "Splitter & Extractor PDF",
        'pdf_splitter_load': " Sélectionner fichier PDF",
        'pdf_splitter_info': "Veuillez choisir une option pour votre document PDF",
        'pdf_splitter_basic': "Opérations de base",
        'pdf_splitter_single': "Diviser en pages individuelles",
        'pdf_splitter_range': "Extraire les pages :",
        'pdf_splitter_range_placeholder': "ex. 1-3,5,7-9",
        'pdf_splitter_clean': "Opérations de nettoyage",
        'pdf_splitter_remove_empty': "Supprimer toutes les pages vides",
        'pdf_splitter_remove': "Supprimer la plage de pages :",
        'pdf_splitter_remove_placeholder': "ex. 2,4-6",
        'pdf_splitter_process': "Traiter le PDF",
        'pdf_splitter_loaded': "PDF chargé. Veuillez choisir une option",
        'pdf_read_error': "Impossible de lire le PDF",
        'pages': "Pages",
        'pages_created': "Pages créées",
        'range_empty': "Veuillez entrer une plage de pages",
        'range_invalid': "Plage de pages invalide",
        'range_created': "Nouveau PDF avec les pages sélectionnées créé :\n{0}",
        'empty_removed': "{0} pages vides supprimées.\nSortie : {1}",
        'remove_empty': "Veuillez entrer les pages à supprimer",
        'remove_invalid': "Pages à supprimer invalides",
        'remove_done': "PDF nettoyé créé :\n{0}",
        'open_folder': "Ouvrir le dossier",
        'show_in_finder': "Afficher dans le Finder",
        'pdf_splitter_no_pdf': "Veuillez d’abord charger un fichier PDF.",
        'process_error': "Erreur lors du traitement du PDF",
        'pages_created_voice': "{0} pages ont été créées",
        'range_created_voice': "PDF avec les pages sélectionnées a été créé",
        'empty_removed_voice': "{0} pages vides ont été supprimées",
        'remove_done_voice': "PDF nettoyé créé",
        'pdf_splitter_split_groups': "Chaque groupe contigu dans un fichier séparé",
        'range_created_single': "Nouveau PDF créé :\n{0}",
        'range_created_multiple': "{0} fichiers PDF ont été créés.",
        'range_created_voice_single': "Un PDF avec les pages sélectionnées a été créé",
        'range_created_voice_multiple': "{0} fichiers PDF ont été créés",
        'empty_removed_none_left': "Aucune page restante",
        'empty_removed_all_empty': "Toutes les pages ont été reconnues comme vides et seraient supprimées. Aucun fichier n’a été créé.",
        'preview_single': "Aperçu : {0}",
        'preview_enter_range': "Veuillez entrer une plage de pages.",
        'preview_invalid_range': "Plage de pages invalide.",
        'preview_file': "Aperçu : {0}",
        'preview_files': "Aperçu : {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Démarrage de l’impression",
        'print_sent': "Travail d’impression envoyé",
        'print_now': "Imprimer maintenant",
        'print_error': "Erreur lors de l’impression directe",
        'print_limited': "Fonction d’impression limitée sur ce système",
        'print_error_format': "Erreur lors de l’impression directe : {0}",
        'warning': "Avis",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Passer en mode clair",
        'mode_switch_to_dark': "Passer en mode sombre",
        'mode_dark_activated': "Mode sombre activé",
        'mode_light_activated': "Mode clair activé",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Pleine page",
        'zoom_two_pages': "Deux pages côte à côte",
        'zoom_overview': "Mode aperçu",
        'zoom_cannot_during_search': "Zoom impossible pendant la recherche",
        'zoom_exit_first': "Veuillez d’abord quitter le zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Glisser‑déposer activé",
        'drag_disabled': "Glisser‑déposer désactivé",
        'drag_page_grab': "Saisie de la page {0}",
        'drag_page_dropped': "Page {0} insérée à la position {1}",
        'drag_position_invalid': "Position invalide",
        'drag_same_position': "La page {0} reste à la position {0}",
        'drag_error': "Erreur lors du déplacement",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Saisie de texte avec formatage avancé et gestionnaire de modèles",
        'text_templates': "Modèles de texte disponibles :",
        'text_name': "Nom",
        'text_preview': "Aperçu du texte",
        'text_enter': "Texte :",
        'text_font_size': "Taille de police :",
        'text_formatting': "Formatage :",
        'text_bold': "Gras",
        'text_italic': "Italique",
        'text_underline': "Souligné",
        'text_alignment': "Alignement :",
        'text_left': "Gauche",
        'text_center': "Centré",
        'text_right': "Droite",
        'text_color': "Couleur du texte :",
        'text_opacity': "Opacité :",
        'text_word_wrap': "Retour à la ligne :",
        'text_auto': "Automatique",
        'text_page_width_95': "Largeur de page (95%)",
        'text_page_width_85': "Très large (85%)",
        'text_page_width_75': "Plus large (75%)",
        'text_page_width_60': "Large (60%)",
        'text_page_width_50': "Moyen (50%)",
        'text_page_width_30': "Étroit (30%)",
        'text_page_width_20': "Plus étroit (20%)",
        'text_page_width_10': "Très étroit (10%)",
        'text_no_wrap': "Pas de retour",
        'text_private': "Modèle de texte privé (nécessite authentification)",
        'text_preview_label': "Aperçu :",
        'text_preview_placeholder': "Un aperçu du texte s’affichera ici...",
        'text_no_text': "(Aucun texte)",
        'text_save_template': "💾 Enregistrer comme modèle",
        'text_delete_template': "🗑 Supprimer le modèle sélectionné",
        'text_show_private': "Afficher privés",
        'text_hide_private': "Masquer privés",
        'text_use': "✅ Utiliser le texte",
        'text_saved': "Modèle de texte enregistré sous :\n{0}",
        'text_saved_voice': "Modèle de texte enregistré",
        'text_deleted': "Modèle de texte supprimé",
        'text_no_text_to_save': "Aucun texte à enregistrer.",
        'text_no_templates': "Aucun modèle de texte trouvé",
        'text_private_master_required': "Les modèles privés ne peuvent être utilisés que si un mot de passe maître est configuré.\n\nVoulez‑vous configurer un mot de passe maître maintenant ?",
        'text_filename': "Nom de fichier pour le modèle (sans 'Text_' et '.txt') :",
        'text_filename_hint': "Exemple : 'Téléphone Maison' sera enregistré comme 'Text_Téléphone Maison.txt'",
        'text_save_hint': "Le modèle de texte sera automatiquement enregistré avec son formatage.",
        'text_guide_title': "Saisie de texte - Guide",
        'text_delete_confirm': "Voulez‑vous vraiment supprimer le modèle de texte ?\n\nFichier : {0}\nTexte : {1}...",
        'text_make_public': "Marquer comme public",
        'text_make_private': "Marquer comme privé",
        'text_privacy_changed': "Statut de confidentialité modifié",
        'text_private_always': "Privés toujours visibles (paramètre)",
        'text_mode_required': "Veuillez d’abord activer le mode texte",
        'text_continue_editing': "Continuer l’édition – curseur en fin de texte",
        'text_no_input': "Aucun texte saisi – texte annulé",
        'save_dialog_question': "Comment souhaitez‑vous procéder ?",
        'text_save_question': "Enregistrer tous les textes et croix, ajuster, continuer l’édition ou annuler ?",
        'copy_cross': "Croix copiée",
        'paste_cross': "Croix collée",
        'paste_text': "Texte collé",
        'cross_discarded': "Croix annulée",
        'all_discarded': "Tout annulé",
        'text_discarded': "Texte annulé",
        'no_texts_to_save': "Aucun texte à enregistrer",
        'no_valid_texts': "Aucun texte valide à enregistrer",
        'text_word_singular': "texte",
        'text_word_plural': "textes",
        'cross_word_singular': "croix",
        'cross_word_plural': "croix",
        'texts_saved_title': "Textes enregistrés",
        'texts_crosses_saved': "{0} {1} et {2} {3} ont été insérés dans le PDF.\n\nPDF rechargé...",
        'texts_crosses_saved_voice': "{0} {1} et {2} {3} enregistrés.",
        'texts_saved': "{0} {1} ont été insérés dans le PDF.\n\nPDF rechargé...",
        'texts_saved_voice': "{0} {1} enregistrés.",
        'crosses_saved': "{0} {1} ont été insérés dans le PDF.\n\nPDF rechargé...",
        'crosses_saved_voice': "{0} {1} enregistrés.",
        'elements_saved': "{0} éléments ont été insérés dans le PDF.\n\nPDF rechargé...",
        'elements_saved_voice': "{0} éléments enregistrés.",
        'text_window_load_error': "Impossible de charger la fenêtre de texte",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Saisie de texte et modèles – Guide détaillé**

        **1. Insérer et modifier du texte**
        - Clic droit à l’endroit souhaité dans le document et choisissez "Insérer du texte".
        - Une boîte de dialogue s’ouvre où vous pouvez saisir et formater votre texte :
        • Taille de police, Gras, Italique, Souligné
        • Couleur du texte (libre choix)
        • Transparence (opacité) via curseur
        • Retour à la ligne (différentes largeurs, p. ex. largeur de page, étroit, sans retour)
        - Après validation, le texte apparaît à la position cliquée. Vous pouvez le déplacer avec la souris ou les touches fléchées.
        - Double‑clic sur le texte ouvre le mode édition ; Échap le quitte.

        **2. Gérer les modèles de texte**
        - Dans la boîte de dialogue, vous voyez à gauche la liste de tous les modèles enregistrés.
        - **Enregistrer un modèle :** Saisissez votre texte, formatez‑le et cliquez sur "💾 Enregistrer comme modèle". Entrez un nom de fichier (sans extension).
        - **Charger un modèle :** Cliquez sur le nom souhaité dans la liste. Le texte et le formatage sont repris et peuvent être ajustés si nécessaire.
        - **Supprimer :** Clic droit sur un modèle pour le supprimer ou changer son statut privé/public.

        **3. Modèles privés (mot de passe maître)**
        - Si vous avez configuré un mot de passe maître (dans Paramètres → Gestionnaire de mots de passe), vous pouvez marquer les modèles comme "privé".
        - Cochez la case "Modèle de texte privé" dans la boîte de dialogue avant d’enregistrer.
        - Les modèles privés ne sont affichés dans la liste qu’après avoir saisi votre mot de passe maître une fois par session (authentification via l’icône cadenas ou au premier accès).
        - Ainsi vous protégez les modèles confidentiels contre tout accès non autorisé.

        **4. Insérer des croix**
        - Via le menu contextuel, vous pouvez aussi insérer une croix graphique (par exemple pour des cases à cocher).
        - La taille, l’épaisseur de trait et la couleur des croix peuvent être ajustées globalement dans les paramètres (menu "Paramètres" → "Réglages croix").
        - Clic droit sur une croix existante pour la modifier individuellement.

        **5. Actions groupées**
        - Si vous avez placé plusieurs textes ou croix sur une page, vous pouvez tous les enregistrer ou les annuler ensemble via le menu contextuel (clic droit en mode texte).
        - Lors de l’enregistrement, tous les éléments sont incorporés dans le PDF et restent sous forme de graphiques vectoriels.

        **6. Raccourcis clavier en mode texte**
        - Touches fléchées : déplacer l’élément
        - Ctrl+Flèches : pas plus grands
        - Entrée : ouvrir la boîte de dialogue d’enregistrement (tout enregistrer / ajuster / annuler)
        - Échap : annuler l’élément courant
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Saisie de texte et modèles – Guide détaillé</strong></p>

        <p><strong>1. Insérer et modifier du texte</strong></p>
        <ul>
        <li>Clic droit à l’endroit souhaité dans le document et choisissez "Insérer du texte".</li>
        <li>Une boîte de dialogue s’ouvre où vous pouvez saisir et formater votre texte :<br/>
        • Taille de police, Gras, Italique, Souligné<br/>
        • Couleur du texte (libre choix)<br/>
        • Transparence (opacité) via curseur<br/>
        • Retour à la ligne (différentes largeurs, p. ex. largeur de page, étroit, sans retour)</li>
        <li>Après validation, le texte apparaît à la position cliquée. Vous pouvez le déplacer avec la souris ou les touches fléchées.</li>
        <li>Double‑clic sur le texte ouvre le mode édition ; Échap le quitte.</li>
        </ul>

        <p><strong>2. Gérer les modèles de texte</strong></p>
        <ul>
        <li>Dans la boîte de dialogue, vous voyez à gauche la liste de tous les modèles enregistrés.</li>
        <li><strong>Enregistrer un modèle :</strong> Saisissez votre texte, formatez‑le et cliquez sur "💾 Enregistrer comme modèle". Entrez un nom de fichier (sans extension).</li>
        <li><strong>Charger un modèle :</strong> Cliquez sur le nom souhaité dans la liste. Le texte et le formatage sont repris et peuvent être ajustés si nécessaire.</li>
        <li><strong>Supprimer :</strong> Clic droit sur un modèle pour le supprimer ou changer son statut privé/public.</li>
        </ul>

        <p><strong>3. Modèles privés (mot de passe maître)</strong></p>
        <ul>
        <li>Si vous avez configuré un mot de passe maître (dans Paramètres → Gestionnaire de mots de passe), vous pouvez marquer les modèles comme "privé".</li>
        <li>Cochez la case "Modèle de texte privé" dans la boîte de dialogue avant d’enregistrer.</li>
        <li>Les modèles privés ne sont affichés dans la liste qu’après avoir saisi votre mot de passe maître une fois par session (authentification via l’icône cadenas ou au premier accès).</li>
        <li>Ainsi vous protégez les modèles confidentiels contre tout accès non autorisé.</li>
        </ul>

        <p><strong>4. Insérer des croix</strong></p>
        <ul>
        <li>Via le menu contextuel, vous pouvez aussi insérer une croix graphique (par exemple pour des cases à cocher).</li>
        <li>La taille, l’épaisseur de trait et la couleur des croix peuvent être ajustées globalement dans les paramètres (menu "Paramètres" → "Réglages croix").</li>
        <li>Clic droit sur une croix existante pour la modifier individuellement.</li>
        </ul>

        <p><strong>5. Actions groupées</strong></p>
        <ul>
        <li>Si vous avez placé plusieurs textes ou croix sur une page, vous pouvez tous les enregistrer ou les annuler ensemble via le menu contextuel (clic droit en mode texte).</li>
        <li>Lors de l’enregistrement, tous les éléments sont incorporés dans le PDF et restent sous forme de graphiques vectoriels.</li>
        </ul>

        <p><strong>6. Raccourcis clavier en mode texte</strong></p>
        <ul>
        <li>Touches fléchées : déplacer l’élément</li>
        <li>Ctrl+Flèches : pas plus grands</li>
        <li>Entrée : ouvrir la boîte de dialogue d’enregistrement (tout enregistrer / ajuster / annuler)</li>
        <li>Échap : annuler l’élément courant</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Réglages des croix",
        'cross_properties': "Propriétés de la croix",
        'cross_size': "Taille (px) :",
        'cross_line_width': "Épaisseur du trait :",
        'cross_color': "Couleur :",
        'cross_choose_color': "Choisir",
        'cross_fine_tuning': "Ajustement fin à l’enregistrement (pixels)",
        'cross_offset_x': "Décalage X :",
        'cross_offset_y': "Décalage Y :",
        'cross_offset_x_tooltip': "Valeurs négatives déplacent la croix vers la gauche, positives vers la droite",
        'cross_offset_y_tooltip': "Valeurs négatives déplacent la croix vers le haut, positives vers le bas",
        'cross_preview': "Aperçu",
        'cross_save': "Appliquer les réglages",
        'cross_customized': "Croix personnalisée",
        'cross_settings_applied': "Réglages de croix enregistrés.\nTaille : {0}px, Épaisseur : {1}px\n{2}",
        'cross_updated_count': "{0} croix existantes ont été mises à jour.",
        'cross_no_crosses': "Aucune croix existante trouvée.",
        'cross_settings_applied_all': "Réglages de croix appliqués à toutes les {0} croix",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Réglages des signatures",
        'signature_1': "Signature 1",
        'signature_2': "Signature 2",
        'signature_select': "Choisir une signature",
        'signature_add': "➕ Ajouter une nouvelle signature...",
        'signature_size': "Taille pour signature {0} (%) :",
        'signature_common': "Réglages généraux",
        'signature_timestamp': "Ajouter automatiquement l’horodatage",
        'signature_location': "Lieu par défaut :",
        'signature_timestamp_size': "Taille police horodatage :",
        'signature_no_files': "-- Aucune signature trouvée --",
        'signature_insert': "Insérer une signature",
        'signature_insert_1': "Insérer signature 1",
        'signature_insert_2': "Insérer signature 2",
        'signature_customize': " Personnaliser la signature",
        'signature_discard': " Annuler cette signature",
        'signature_save_all': " Enregistrer toutes les signatures",
        'signature_discard_all': " Annuler toutes les signatures",
        'signature_guide_title': "Signatures - Guide",
        'signature_guide': """
📝 Signatures - Guide rapide

- Configurer le mot de passe maître
- Paramétrer les signatures dans le menu Paramètres
  (taille, horodatage ...)
- Insérer avec CLIC DROIT à l’endroit souhaité
  (mot de passe maître requis une fois par session)
- Déplacer la signature avec la souris ou les touches fléchées
- Plusieurs signatures peuvent être insérées à la suite
- Chaque signature peut être personnalisée individuellement
- Annuler une signature
- Enregistrer / annuler toutes les signatures d’un coup
- On peut aussi utiliser la barre de menu.
        """,
        'signature_placeholder': "Aucun aperçu disponible",
        'signature_info': "Signature {0} : {1}×{2} px ({3}% de {4}×{5})",
        'signature_info_placeholder': "Paramètres pour signature {0}",
        'signature_inserted': "Signature {0} insérée à la page {1}",
        'signature_deleted': "Signature supprimée",
        'signature_copied': "Signature copiée",
        'signature_pasted': "Signature {0} collée",
        'signature_saved': "{0} signatures ont été insérées dans le PDF.\n\nPDF rechargé...",
        'signature_saved_voice': "{0} signatures enregistrées",
        'mode_replace_signature_format': "Quitter le mode et insérer signature {0}",
        'mode_conflict_voice_signature': "Le mode {0} est actif. Quitter et insérer une signature ?",
        'signature_not_configured': "Signature {0} non configurée",
        'signature_file_not_found': "Fichier de signature introuvable",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Aucune signature copiée disponible",
        'no_signatures_to_save': "Aucune signature à enregistrer",
        'signature_save_question': "Enregistrer toutes les signatures, ajuster ou annuler celle‑ci ?",
        'signatures_saved_title': "Signatures enregistrées",
        'signatures_saved': "{0} signatures ont été insérées dans le PDF.\n\nPDF rechargé...",
        'signatures_saved_voice': "{0} signatures enregistrées.",
        'all_signatures_discarded': "Toutes les signatures annulées",
        'signature_settings_saved': "Réglages de signature enregistrés",
        'signature_cancelled': "Signature annulée",
        'signature_active_title': "Signature active",
        'signature_replace_question': "Une signature est déjà active.\n\nVoulez‑vous remplacer la signature actuelle ?",
        'signature_replace': "Remplacer la signature",
        'signature_replace_voice': "Remplacer la signature actuelle ou annuler ?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Réglages d’image",
        'image_common': "Réglages généraux d’image",
        'image_keep_aspect': "Conserver les proportions lors du déplacement",
        'image_default_size': "Taille par défaut (%) :",
        'image_dark_invert': "Inverser les images en mode sombre",
        'image_dark_invert_tooltip': "Activé : les images sont inversées pour une meilleure visibilité",
        'image_fine_tuning': "Ajustement fin (pixels)",
        'image_offset_x': "Décalage X :",
        'image_offset_y': "Décalage Y :",
        'image_offset_x_tooltip': "Valeurs négatives déplacent l’image vers la gauche, positives vers la droite",
        'image_offset_y_tooltip': "Valeurs négatives déplacent l’image vers le haut, positives vers le bas",
        'image_select': "Choisir une image",
        'image_insert': "Insérer une image",
        'image_customize': " Personnaliser l’image",
        'image_aspect': " Conserver les proportions",
        'image_discard': " Annuler cette image",
        'image_save_all': " Enregistrer toutes les images",
        'image_discard_all': " Annuler toutes les images",
        'image_filter': "Images",
        'image_guide_title': "Insérer une image - Guide",
        'image_guide': """
📷 Insérer une image dans un PDF - Guide rapide :

1. Clic droit à l’endroit souhaité
2. "Insérer une image" → choisir l’image
3. Positionner l’image : glisser avec la souris
4. Ajuster la taille : tirer sur les coins/côtés
5. Conserver les proportions : touche [A]
6. Autres ajustements : clic droit sur l’image

Astuce : vous pouvez ajuster les paramètres dans le menu contextuel.
        """,
        'image_inserted': "Image {0} insérée à la page {1}",
        'image_deleted': "Image annulée",
        'image_copied': "Image copiée",
        'image_pasted': "Image collée",
        'image_saved': "{0} images ont été insérées dans le PDF.\n\nPDF rechargé...",
        'image_saved_voice': "{0} images enregistrées",
        'image_aspect_on': "activé",
        'image_aspect_off': "désactivé",
        'image_aspect_toggle': "Conserver les proportions {0}",
        'image_reset': "Image remise à la taille d’origine",
        'image_replaced': "Image remplacée",
        'image_invalid': "Image non valide",
        'mode_replace_image': "Insérer une image",
        'mode_conflict_voice_image': "Le mode {0} est actif. Quitter et insérer une image ?",
        'image_active_title': "Image active",
        'image_replace_question': "Une image est déjà active.\n\nVoulez‑vous remplacer l’image actuelle ?",
        'image_replace': "Remplacer l’image",
        'image_replace_voice': "Remplacer l’image actuelle ou annuler ?",
        'image_filter_all': "Images (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Tous les fichiers (*.*)",
        'no_copied_image': "Aucune image copiée disponible",
        'image_discarded': "Image annulée",
        'image_save_question': "Enregistrer toutes les images, ajuster ou annuler celle‑ci ?",
        'no_images_to_save': "Aucune image à enregistrer",
        'no_valid_images': "Aucune image valide à enregistrer",
        'images_saved_title': "Images enregistrées",
        'images_saved': "{0} images ont été insérées dans le PDF.\n\nPDF rechargé...",
        'images_saved_voice': "{0} images enregistrées.",
        'all_images_discarded': "Toutes les images annulées",
        'image_settings_updated': "Réglages d’image mis à jour",
        'image_replace_title': "Choisir une nouvelle image",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Réglages des formes",
        'form_basic': "Réglages de base",
        'form_default_type': "Type de forme par défaut :",
        'form_rectangle': "Rectangle",
        'form_ellipse': "Ellipse",
        'form_line': "Ligne",
        'form_arrow': "Flèche",
        'form_line_width': "Épaisseur du trait :",
        'form_colors': "Couleurs",
        'form_line_color': "Couleur du trait :",
        'form_fill_color': "Couleur de remplissage :",
        'form_choose_color': "Choisir",
        'form_transparent': "Arrière‑plan transparent (ligne seule)",
        'form_filled': "rempli",
        'form_dark_mode': "Mode sombre",
        'form_dark_invert': "Inverser les couleurs en mode sombre",
        'form_fine_tuning': "Ajustement fin (pixels)",
        'form_offset_x': "Décalage X :",
        'form_offset_y': "Décalage Y :",
        'form_offset_x_tooltip': "Valeurs négatives déplacent la forme vers la gauche, positives vers la droite",
        'form_offset_y_tooltip': "Valeurs négatives déplacent la forme vers le haut, positives vers le bas",
        'form_preview': "Aperçu",
        'form_insert': "Insérer une forme",
        'form_rectangle_insert': "Rectangle",
        'form_ellipse_insert': "Ellipse/Cercle",
        'form_line_insert': "Ligne (2 clics)",
        'form_arrow_insert': "Flèche (2 clics)",
        'form_customize': " Personnaliser la forme",
        'form_transparent_toggle': " Arrière‑plan transparent",
        'form_discard': " Annuler cette forme",
        'form_save_all': " Enregistrer toutes les formes",
        'form_discard_all': " Annuler toutes les formes",
        'form_guide_title': "Insérer une forme - Guide",
        'form_guide': """
📐 Insérer une forme dans un PDF - Guide rapide :

1. Choisir le type de forme (rectangle, ellipse, ligne, flèche)
2. Cliquer à la position souhaitée
   - Pour rectangle/ellipse : un clic place la forme
   - Pour ligne/flèche : deux clics pour point départ et fin
3. Positionner la forme : glisser avec la souris
4. Ajuster la taille : tirer sur les coins/côtés
5. Enregistrer la forme : Entrée
6. Annuler la forme : Échap
7. Autres ajustements : clic droit sur la forme

Astuce : vous pouvez ajuster les paramètres dans le menu contextuel.
        """,
        'form_inserted': "{0} insérée à la page {1}",
        'form_deleted': "Forme supprimée",
        'form_copied': "Forme copiée",
        'form_pasted': "Forme collée",
        'form_saved': "{0} formes ont été insérées dans le PDF.\n\nPDF rechargé...",
        'form_saved_voice': "{0} formes enregistrées",
        'form_reset': "Forme remise à la taille par défaut",
        'form_transparent_on': "activé",
        'form_transparent_off': "désactivé",
        'form_transparent_toggled': "Arrière‑plan transparent {0}",
        'form_line_cancel': "Tracé de ligne annulé",
        'form_second_click': "Cliquez maintenant le point final pour {0}",
        'mode_replace_form': "Insérer une forme",
        'mode_conflict_voice_form': "Le mode {0} est actif. Quitter et insérer une forme ?",
        'form_settings_updated': "Réglages de forme mis à jour",
        'form_unknown': "Forme",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Cliquez sur la position de départ",
        'form_line_guide_2': "2. Cliquez sur la position de fin",
        'form_line_guide_3': "La ligne sera tracée entre ces deux points.",
        'form_line_status_1': "En attente du premier clic...",
        'form_line_status_2': "Premier point défini : ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Cliquez maintenant le point final...",
        'form_line_status_4': "Les deux points sont définis.\nCliquez sur 'Terminer' pour enregistrer.",
        'form_line_reset': "Réinitialiser",
        'form_line_finish': "Terminer",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Copier (Cmd+C)",
        'paste': "Coller (Cmd+V)",
        'copied': "Copié : {0}",
        'no_element_to_copy': "Aucun élément sélectionné à copier",
        'no_copied_data': "Aucune donnée copiée disponible",
        'no_valid_position': "Position invalide pour coller",
        'copy_text': "Texte copié",
        'copy_image': "Image copiée",
        'copy_form': "Forme copiée",
        'copy_signature': "Signature copiée",
        'element_text': "texte",
        'element_image': "image",
        'element_form': "forme",
        'element_signature': "signature",
        'element_unknown': "élément",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Conflit de mode",
        'mode_conflict_message': "Le mode '{0}' est déjà actif.\n\nVoulez‑vous le quitter et {1} ?",
        'mode_replace': "Quitter le mode et {0}",
        'mode_cancel': "Annuler",
        'mode_replace_text': "insérer du texte",
        'mode_replace_cross': "insérer une croix",
        'mode_replace_signature': "insérer une signature",
        'mode_replace_image': "insérer une image",
        'mode_replace_form': "insérer une forme",
        'mode_conflict_voice': "Le mode {0} est actif. Quitter et insérer du texte ?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Saisie texte",
        'active_mode_signature': "Signature",
        'active_mode_image': "Image",
        'active_mode_form': "Forme",
        'active_mode_and': " et ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Insérer",                    # Hauptmenü
        'insert_another_text': "Insérer du texte",          # Vereinfacht
        'insert_another_cross': "Insérer une croix",        # Vereinfacht
        'insert_another_signature_1': "Signature 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Signature 2",      # Untermenü-Eintrag
        'insert_another_image': "Insérer une image",         # Vereinfacht
        'insert_another_form_rect': "Rectangle",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Ligne (2 clics)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Flèche (2 clics)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Enregistrer {0}",
        'save_dialog_message': "{0} sera enregistré(e) à la page {1}.\n\nComment souhaitez‑vous procéder ?",
        'save_all': "Enregistrer tou(te)s les {0}",
        'save_single': "Enregistrer {0}",
        'save_customize': "Personnaliser {0}",
        'save_discard': "Annuler {0}",
        'save_continue': "Continuer l’édition",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Aller à la page {0}",
        'context_rotate': " Pivoter la page {0}",
        'context_delete': " Supprimer la page {0}",
        'context_export': " Exporter la page {0}",
        'context_mark_as': " Marquer la page comme...",
        'context_mark_empty': " Page vide",
        'context_unmark_empty': " Plus vide",
        'context_mark_export': " Marquer pour export",
        'context_unmark_export': " Ne plus exporter",
        'context_batch_actions': " Actions groupées",
        'context_batch_delete_empty': " Supprimer les {0} pages vides",
        'context_batch_export_single': " Toutes les {0} pages (un seul fichier)",
        'context_batch_export_split': " Toutes les {0} pages (fichiers séparés)",
        'context_drag_start': " Activer glisser‑déposer",
        'context_drag_stop': " Désactiver glisser‑déposer",
        'context_insert': " Insérer",
        'context_insert_pages': " Insérer des pages",
        'context_zoom': "Zoom",
        'discard_mixed': "Annuler {0} {1} et {2} {3}",
        'save_mixed': "Enregistrer {0} {1} et {2} {3}",
        'discard_texts': "Annuler {0} textes",
        'discard_text_single': "Annuler 1 texte",
        'save_texts': "Enregistrer {0} textes",
        'save_text_single': "Enregistrer 1 texte",
        'discard_crosses': "Annuler {0} croix",
        'discard_cross_single': "Annuler 1 croix",
        'save_crosses': "Enregistrer {0} croix",
        'save_cross_single': "Enregistrer 1 croix",
        'discard_signatures': "Annuler {0} signatures",
        'save_signature_single': "Enregistrer 1 signature",
        'save_signatures': "Enregistrer {0} signatures",
        'discard_images': "Annuler {0} images",
        'save_image_single': "Enregistrer 1 image",
        'save_images': "Enregistrer {0} images",
        'discard_forms': "Annuler {0} formes",
        'save_form_single': "Enregistrer 1 forme",
        'save_forms': "Enregistrer {0} formes",
        'cross_discard': "Annuler cette croix",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informations Export / Import",
        'export_what': "📋 Qu’est‑ce qui est exporté ?",
        'export_general': "Paramètres généraux",
        'export_general_items': "• Synthèse vocale (on/off, vitesse)\n• Mode sombre/clair\n• Paramètres de sauvegarde\n• Paramètres OCR",
        'export_image_form': "Paramètres images et formes",
        'export_image_form_items': "• Réglages images (proportions, taille par défaut)\n• Réglages formes (épaisseur trait, couleurs)\n• Réglages signatures (chemins, tailles, horodatage)",
        'export_passwords': "Base de données des mots de passe",
        'export_passwords_items': "• Tous les mots de passe PDF enregistrés\n• Au choix chiffrés ou déchiffrés",
        'export_master': "Paramètres du mot de passe maître",
        'export_master_items': "• Hachage du mot de passe maître\n• Réglages pour signatures/modèles de texte",
        'export_signatures': "Signatures et modèles de texte",
        'export_signatures_items': "• Tous les fichiers image (signatures)\n• Tous les modèles de texte avec formatage\n• Marquages privé/public",
        'export_import_warning': "⚠️ Remarques importantes",
        'export_import_note': "• Lors de l’import, TOUS les paramètres actuels sont écrasés\n• Un redémarrage de l’application est nécessaire\n• Les signatures/modèles existants seront remplacés",
        'export_master_note': "• Si un mot de passe maître est défini, vous pouvez choisir :\n  - Déchiffré (mots de passe en clair)\n  - Chiffré (lisibles seulement avec le mot de passe maître)",
        'export_security': "• Le fichier ZIP exporté contient des données confidentielles\n• Conservez‑le en lieu sûr (p. ex. clé USB chiffrée)\n• En cas de perte du fichier, les mots de passe sont définitivement perdus",
        'export_format': "📁 Format d’export",
        'export_format_desc': "Les paramètres sont enregistrés dans un seul fichier ZIP :",
        'export_filename': "PDFDarkView_Settings_AAAAMMJJ_HHMMSS.zip",
        'export_success': "Paramètres exportés avec succès",
        'export_failed': "Échec de l’export",
        'export_import_question': "Voulez‑vous redémarrer l’application maintenant ?",
        'export_password_question': "Un mot de passe maître est défini.\n\nVoulez‑vous exporter les mots de passe déchiffrés ?\n(sinon ils seront exportés chiffrés)",
        'export_decrypt': "Exporter déchiffré",
        'export_encrypt': "Exporter chiffré",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Infos",
        'info_title': "À propos de PDF Dark View",
        'info_version': "Version",
        'info_author': "Développé par Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "À propos",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> est un lecteur PDF accessible, développé spécialement pour les personnes malvoyantes.</p>

            <p><strong>Fonctionnalités clés :</strong></p>
            <ul>
                <li>Interface contrastée et personnalisable</li>
                <li>Contrôle complet par clavier</li>
                <li>Synthèse vocale intégrée</li>
                <li>OCR pour les documents scannés</li>
                <li>Outils d'édition complets</li>
            </ul>

            <p>Plus de 50 langues sont prises en charge – pour que les PDF soient accessibles à tous.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Fonctionnalités",
        'info_features_intro': "PDF Dark View vous offre les possibilités suivantes :",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Affichage et navigation</strong> – Mode sombre/clair, parcourir les pages, zoom, aller à la page</li>
            <li><strong>OCR (reconnaissance de texte)</strong> – Rendre les documents scannés consultables et copiables</li>
            <li><strong>Édition</strong> – Insérer du texte, des croix, des signatures, des images et des formes</li>
            <li><strong>Gestion des pages</strong> – Supprimer, extraire, insérer, déplacer par glisser-déposer</li>
            <li><strong>Exportation</strong> – Vers Word, Pages ou en texte</li>
            <li><strong>Sécurité</strong> – Protection et gestion par mot de passe</li>
            <li><strong>Accessibilité</strong> – Synthèse vocale, contrôle par clavier, contraste élevé</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Utilisation",
        'info_accessibility': "♿ Accessibilité – contrôle complet par clavier",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Général</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Ouvrir PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Rechercher</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Basculer mode sombre/clair</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Imprimer</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Quitter</div>

        <div class="shortcut-cat">📖 Navigation</div>
        <div class="shortcut-row"><kbd>Touches fléchées</kbd> Parcourir page par page</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Aller à la page</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Première page</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Dernière page</div>

        <div class="shortcut-cat">✏️ Édition</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Insérer du texte</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Supprimer des pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extraire des pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Insérer des pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Déplacer des pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Pivoter la page</div>

        <div class="shortcut-cat">🖼️ Déplacer des éléments</div>
        <div class="shortcut-row"><kbd>Touches fléchées</kbd> Déplacer texte/image/signature</div>
        <div class="shortcut-row"><kbd>Ctrl+Touches fléchées</kbd> Pas plus grands</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Enregistrer</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Annuler</div>

        <div class="shortcut-cat">🗣️ Synthèse vocale</div>
        <div class="shortcut-row"><kbd>F2</kbd> Activer/désactiver la synthèse vocale</div>
        """,
        'info_contextmenu': "📌 Important : Toutes les fonctions sont également accessibles via le menu contextuel (clic droit de la souris) !",
        'info_accessibility_hint': "💡 Astuce : La synthèse vocale (F2) facilite l'orientation et fournit un retour sur les menus et les dialogues.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licence & Mentions légales",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 MENTIONS LÉGALES</strong><br>
        Informations conformément au § 5 TMG :<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Allemagne<br>
        E-mail : binhdiez64@gmail.com<br>
        Responsable du contenu : Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Clause de non-responsabilité</strong><br>
        Le logiciel a été développé avec le plus grand soin. Aucune garantie n'est donnée quant à l'exactitude, l'exhaustivité et la fonctionnalité. L'utilisation se fait à vos propres risques.<br><br>

        <strong>📄 Licence MIT (utilisation privée)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Autorisé : utilisation gratuite, modifications privées, copies personnelles.<br>
        Non autorisé : vente, utilisation commerciale, suppression des mentions de copyright.<br><br>

        <strong>🔧 Composants tiers</strong><br>
        Ce logiciel contient des composants sous licences GPL, AGPL, Apache 2.0, BSD et MIT.<br>
        Lors de la redistribution, les conditions de licence respectives doivent être respectées.<br><br>

        <strong>🌐 Open Source</strong><br>
        Le code source est disponible et peut être consulté, modifié et redistribué conformément aux conditions de licence respectives.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Remerciements",
        'info_credits': "Merci à la communauté open source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Traitement PDF</li>
            <li><strong>PyQt5</strong> – Interface graphique</li>
            <li><strong>Tesseract OCR</strong> – Reconnaissance de texte</li>
            <li><strong>OCRmyPDF</strong> – Intégration OCR</li>
            <li><strong>python-docx</strong> – Exportation Word</li>
            <li><strong>qtawesome</strong> – Icônes</li>
            <li><strong>DeepSeek</strong> – Soutien pour les traductions (50+ langues)</li>
            <li><strong>Tous les utilisateurs</strong> – Pour les précieux retours</li>
            <li><strong>La communauté open source</strong> – Pour les excellentes bibliothèques</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Langues",
        'info_languages_header': "🌍 Prise en charge des langues",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View prend actuellement en charge <strong>62 langues</strong> – afin que le logiciel puisse être utilisé de manière accessible dans le monde entier.</p>

            <p><strong>📖 Liste complète des langues (État : mars 2026) :</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanais (Shqip)</li>
                    <li>🇩🇿 Arabe (العربية)</li>
                    <li>🇮🇩 Balinais (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Birman (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosniaque (Bosanski)</li>
                    <li>🇧🇬 Bulgare (Български)</li>
                    <li>🇨🇳 Chinois (中文)</li>
                    <li>🇩🇰 Danois (Dansk)</li>
                    <li>🇩🇪 Allemand (Deutsch)</li>
                    <li>🇬🇧 Anglais (English)</li>
                    <li>🇪🇪 Estonien (Eesti)</li>
                    <li>🇫🇮 Finnois (Suomi)</li>
                    <li>🇫🇷 Français (Français)</li>
                    <li>🇬🇷 Grec (Ελληνικά)</li>
                    <li>🇮🇱 Hébreu (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croate (Hrvatski)</li>
                    <li>🇭🇺 Hongrois (Magyar)</li>
                    <li>🇮🇩 Indonésien (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandais (Gaeilge)</li>
                    <li>🇮🇸 Islandais (Íslenska)</li>
                    <li>🇮🇹 Italien (Italiano)</li>
                    <li>🇯🇵 Japonais (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Coréen (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Letton (Latviešu)</li>
                    <li>🇱🇹 Lituanien (Lietuvių)</li>
                    <li>🇱🇺 Luxembourgeois (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malais (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongol (Монгол)</li>
                    <li>🇳🇵 Népalais (नेपाली)</li>
                    <li>🇳🇱 Néerlandais (Nederlands)</li>
                    <li>🇳🇴 Norvégien (Norsk)</li>
                    <li>🇦🇫 Pachto (پښتو)</li>
                    <li>🇮🇷 Persan (فارسی)</li>
                    <li>🇵🇱 Polonais (Polski)</li>
                    <li>🇵🇹 Portugais (Português)</li>
                    <li>🇮🇳 Pendjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Roumain (Română)</li>
                    <li>🇷🇺 Russe (Русский)</li>
                    <li>🇸🇪 Suédois (Svenska)</li>
                    <li>🇷🇸 Serbe (Српски)</li>
                    <li>🇸🇰 Slovaque (Slovenčina)</li>
                    <li>🇸🇮 Slovène (Slovenščina)</li>
                    <li>🇪🇸 Espagnol (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamoul (தமிழ்)</li>
                    <li>🇮🇳 Télougou (తెలుగు)</li>
                    <li>🇹🇭 Thaï (ไทย)</li>
                    <li>🇨🇿 Tchèque (Čeština)</li>
                    <li>🇹🇷 Turc (Türkçe)</li>
                    <li>🇺🇦 Ukrainien (Українська)</li>
                    <li>🇵🇰 Ourdou (اردو)</li>
                    <li>🇻🇳 Vietnamien (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Zoulou (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Ajouter vos propres langues :</strong><br>
                Vous souhaitez une langue qui n'est pas encore incluse ? Il vous suffit de placer votre propre fichier de dictionnaire (<code>sprache_xx.py</code>) à côté de l'application – le logiciel le reconnaîtra automatiquement. Si vous êtes intéressé par une traduction spécifique, n'hésitez pas à me contacter.
            </div>

            <p><strong>🙏 Remerciements particuliers :</strong> DeepSeek pour son soutien à la traduction de tous les dictionnaires dans 62 langues.</p>

            <p>📧 Contact pour les traductions : <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Erreur",
        'error_occurred': "Une erreur est survenue",
        'error_pdf_load': "Erreur lors du chargement du PDF",
        'error_pdf_save': "Erreur lors de l’enregistrement du PDF",
        'error_ocr': "Erreur lors de la reconnaissance de texte",
        'error_no_pdf': "Aucun PDF chargé",
        'error_page_not_found': "Page introuvable",
        'error_invalid_range': "Plage de pages invalide",
        'error_file_not_found': "Fichier introuvable",
        'error_permission': "Permission refusée",
        'error_unknown': "Erreur inconnue",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Succès",
        'success_operation': "Opération réussie",
        'success_saved': "Enregistrement réussi",
        'success_exported': "Export réussi",
        'success_imported': "Import réussi",
        'success_deleted': "Suppression réussie",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Confirmation",
        'confirm_yes': "Oui",
        'confirm_no': "Non",
        'confirm_ok': "OK",
        'confirm_cancel': "Annuler",
        'confirm_delete': "Supprimer",
        'confirm_overwrite': "Remplacer",
        'confirm_continue': "Continuer",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Chargement du PDF...",
        'progress_saving': "Enregistrement du PDF...",
        'progress_exporting': "Export du PDF...",
        'progress_processing': "Traitement en cours...",
        'progress_wait': "Veuillez patienter...",
        'progress_preparing': "Préparation...",
        'progress_finalizing': "Finalisation...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Blanc",
        'color_black': "Noir",
        'color_red': "Rouge",
        'color_green': "Vert",
        'color_blue': "Bleu",
        'color_yellow': "Jaune",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Orange",
        'color_gray': "Gris",
        'color_custom': "Choix de couleur",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fichier",
        'menu_edit': "&Édition",
        'menu_view': "&Affichage",
        'menu_tools': "&Outils",
        'menu_settings': "&Paramètres",
        'menu_help': "&Aide",
        'menu_language': "🌐 Langue",
        'menu_guides': "&Guides",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Ouvrir",
        'file_save_as': "&Enregistrer sous...",
        'file_protect': "&Protéger le document...",
        'file_export': "&Exporter",
        'file_export_pages': "Exporter en Pages",
        'file_export_word': "Exporter en DOCX",
        'file_export_text': "Exporter en TXT",
        'file_print_now': "&Imprimer maintenant",
        'file_print': "&Imprimer",
        'file_close': "&Fermer",
        'file_quit': "&Quitter",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Rechercher",
        'edit_ocr': " Lancer OCR",
        'edit_rotate': "&Pivoter la page",
        'edit_rotate_all': "&Pivoter toutes les pages",
        'edit_delete_pages': "&Supprimer des pages",
        'edit_extract_pages': "&Extraire des pages",
        'edit_insert_pages': "&Insérer des pages",
        'edit_move_pages': "&Déplacer des pages",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Insérer texte et croix",
        'text_insert': " Insérer du texte",
        'cross_insert': " Insérer une croix",
        'text_customize': " Personnaliser le texte",
        'cross_customize': " Personnaliser cette croix",
        'cross_customize_all': " Personnaliser toutes les croix",
        'text_discard': " Annuler ce texte / cette croix",
        'text_discard_all': " Annuler tous les textes et croix",
        'text_save_all': " Enregistrer tous les textes et croix",
        'text_guide': " Saisie texte / modèles - Guide",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Insérer une signature",
        'signature_settings_menu': " Paramètres...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Insérer une image",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Insérer des formes",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Afficher la fenêtre texte",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Largeur de page (défaut)",
        'view_zoom_two': "&Deux pages",
        'view_zoom_overview': "&Aperçu (plusieurs pages)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Accessibilité",
        'settings_voice': "Synthèse vocale",
        'settings_voice_tooltip': "complète la synthèse vocale des lecteurs d’écran par des informations supplémentaires",
        'settings_signature': "&Paramètres de signature",
        'settings_password': "&Gestionnaire de mots de passe",
        'settings_backup': "Créer une sauvegarde avant modification",
        'settings_export_import': "&Exporter / importer les paramètres",
        'settings_export': "&Exporter tous les paramètres...",
        'settings_import': "&Importer tous les paramètres...",
        'settings_export_info': "&Qu’est‑ce qui est exporté ?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "activée",
        'voice_off': "désactivée",
        'voice_toggle': "Synthèse vocale {0}",
        'voice_speed': "Vitesse à {0} pour cent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Outil introuvable :\n{0}\n\nBASE_DIR : {1}\nAssurez‑vous que les outils PDF sont installés dans le dossier {1}.",
        'tool_started': "{0} démarré",
        'tool_start_failed': "Impossible de démarrer",
        'process_error_failed_to_start': "Impossible de démarrer le processus. Le fichier existe‑t‑il ?",
        'process_error_crashed': "Le processus a planté au démarrage.",
        'process_error_timeout': "Délai d’attente du processus dépassé.",
        'process_error_write': "Erreur d’écriture vers le processus.",
        'process_error_read': "Erreur de lecture du processus.",
        'process_error_unknown': "Erreur de processus inconnue",
        'process_command': "Commande",
        'process_normal_exit': "terminé normalement",
        'process_crashed': "planté",
        'process_nonzero_exit': "{0} s’est terminé avec le code d’erreur {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Annulation en cours...",
        'move_cancelling': "Annulation du déplacement",
        'opening_pdf': "Ouverture du PDF...",
        'loading_document': "Chargement du document...",
        'pdf_opened': "PDF ouvert",
        'pages_found_moving': "{0} pages trouvées, {1} à déplacer",
        'creating_backup': "Création de la sauvegarde...",
        'backup_description': "Sauvegarde du fichier original...",
        'backup_saved_as': "Sauvegardé sous : {0}",
        'error_format': "Erreur : {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Recherche réinitialisée",
        'page_header_simple': "=== Page {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Gestionnaire de mots de passe – Guide",
        'password_guide_voice': "Guide de gestion des mots de passe. Veuillez lire les remarques.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Gestionnaire de mots de passe – Guide détaillé</strong></p>

        <p><strong>1. Protection par mot de passe des PDF</strong></p>
        <ul>
        <li>Lors de l’ouverture d’un PDF protégé par mot de passe, une boîte de dialogue apparaît pour saisir le mot de passe.</li>
        <li>Vous pouvez enregistrer le mot de passe chiffré pour ne pas avoir à le ressaisir à chaque fois (case à cocher « Enregistrer le mot de passe »).</li>
        <li>Avec le bouton « Enlever le mot de passe », vous pouvez créer une copie déchiffrée du PDF et supprimer le mot de passe de la base de données.</li>
        </ul>

        <p><strong>2. Mot de passe maître</strong></p>
        <ul>
        <li>Le mot de passe maître protège l’accès à tous les mots de passe PDF enregistrés.</li>
        <li><strong>Configuration :</strong> Allez dans « Paramètres → Gestionnaire de mots de passe → Paramètres mot de passe maître » et cliquez sur « Configurer mot de passe maître ». Choisissez un mot de passe fort (au moins 8 caractères).</li>
        <li><strong>Changement :</strong> Après authentification réussie, vous pouvez changer le mot de passe maître.</li>
        <li><strong>Suppression :</strong> Si vous supprimez le mot de passe maître, TOUS les mots de passe enregistrés sont définitivement effacés. Vous pouvez exporter une sauvegarde avant.</li>
        <li>Une fois par session, vous devez vous authentifier avec le mot de passe maître pour accéder aux fonctions protégées (par exemple afficher les mots de passe).</li>
        </ul>

        <p><strong>3. Gestionnaire de mots de passe (liste)</strong></p>
        <ul>
        <li>Sous « Paramètres → Gestionnaire de mots de passe », vous ouvrez un tableau de tous les PDF enregistrés avec leurs mots de passe chiffrés.</li>
        <li><strong>Sans mot de passe maître :</strong> Vous pouvez seulement supprimer des entrées – les mots de passe restent cachés.</li>
        <li><strong>Avec mot de passe maître (authentifié) :</strong> Vous pouvez afficher, copier, exporter et supprimer les mots de passe.</li>
        <li><strong>Export :</strong> Choisissez un format (JSON, CSV, TXT) et enregistrez la liste. Si un mot de passe maître est défini, vous pouvez décider si les mots de passe sont exportés en clair ou toujours chiffrés.</li>
        <li><strong>Import :</strong> Un fichier ZIP précédemment exporté avec tous les paramètres (y compris mots de passe) peut être réimporté via « Paramètres → Exporter/importer les paramètres ». Attention : les données existantes seront écrasées !</li>
        </ul>

        <p><strong>4. Générateur de mot de passe</strong></p>
        <ul>
        <li>Dans la boîte de dialogue du mot de passe (par exemple lors de la protection d’un PDF), vous trouvez un bouton en forme de dé 🎲 à droite du champ de saisie.</li>
        <li>Cliquez‑le pour ouvrir le générateur de mot de passe. Vous pouvez régler la longueur, les jeux de caractères (majuscules, minuscules, chiffres, symboles) et un séparateur pour une meilleure lisibilité.</li>
        <li>Le mot de passe généré peut être repris directement et copié si nécessaire.</li>
        </ul>

        <p><strong>5. Remarques de sécurité importantes</strong></p>
        <ul>
        <li>Les mots de passe enregistrés sont stockés chiffrés avec AES‑256. La clé est dérivée de votre mot de passe maître (s’il est défini) ou d’une valeur fixe (sans mot de passe maître).</li>
        <li>Sans mot de passe maître, les mots de passe sont certes chiffrés, mais la clé est incluse dans le programme – un attaquant ayant accès à vos fichiers pourrait les déchiffrer. Nous recommandons donc vivement l’utilisation d’un mot de passe maître.</li>
        <li>La base de données des mots de passe se trouve dans le dossier `Data/passwords.json`. Faites des sauvegardes régulières, surtout avant de supprimer le mot de passe maître.</li>
        <li>En cas de perte du mot de passe maître, tous les mots de passe enregistrés sont définitivement perdus.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mode d'inversion",
        'invert_mode_classic': "Classique (inverser toutes les couleurs)",
        'invert_mode_smart': "Intelligent (inverser uniquement la luminosité)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Seuil de niveaux de gris",
        'gray_threshold_10': "10% (strict)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (doux)",
        'threshold_changed': "Seuil réglé sur {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Seuil de niveaux de gris – Explication",
        'threshold_guide_text': "Le seuil de niveaux de gris détermine quels pixels en mode sombre intelligent sont considérés comme 'gris' et sont inversés.\n\n"
                                "• Une valeur basse (10%) n'inverse que les nuances de gris presque parfaites – les éléments colorés restent entièrement préservés.\n"
                                "• Une valeur élevée (50%) inverse également les pixels légèrement colorés – cela augmente le contraste, mais peut déformer les couleurs.\n\n"
                                "La valeur optimale dépend du document. Pour les documents purement textuels, 30–40% est souvent idéal, pour les graphiques colorés plutôt 10–20%.\n\n"
                                "Vous pouvez ajuster la valeur à tout moment via le menu 'Paramètres' – le PDF sera alors rechargé immédiatement.\n\n"
                                "Remarque :\n* Les photos et images ne peuvent être affichées correctement qu'en mode clair !\n* Les paramètres d'inversion ne sont affichés que lorsque le mode sombre est activé.",
        'threshold_guide_voice': "Le seuil de niveaux de gris détermine à quel point le mode sombre intelligent intervient. Une valeur basse préserve les couleurs, une valeur élevée augmente le contraste.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Ouverture du PDF...",
        'progress_loading_document': "Chargement du document...",
        'progress_pdf_opened': "PDF ouvert",
        'progress_creating_backup': "Création d'une sauvegarde...",
        'progress_backup_description': "Sécurisation du fichier original...",
        'progress_backup_created': "Sauvegarde créée",
        'progress_backup_saved_as': "Enregistré sous : {0}",
        'progress_analyzing_start': "Démarrage de l'analyse...",
        'progress_searching_empty': "Recherche de pages vides...",
        'progress_page_empty': "La page {0} est vide",
        'progress_page_keep': "Conserver la page {0}",
        'progress_analysis_complete': "Analyse terminée",
        'progress_empty_found': "{0} pages vides trouvées",
        'progress_current_page': "Page actuelle",
        'progress_mark_delete': "Marqué pour suppression",
        'progress_range_selected': "Plage de pages {0}-{1}",
        'progress_deleting_pages': "Suppression de {0} pages",
        'progress_creating_new_pdf': "Création d'un nouveau PDF...",
        'progress_transferring_pages': "Transfert des pages",
        'progress_keeping_page': "La page {0} sera conservée ({1}/{2})",
        'progress_saving_pdf': "Enregistrement du PDF...",
        'progress_optimizing': "Optimisation de la taille du fichier...",
        'progress_finalizing': "Finalisation...",
        'progress_new_size': "Nouvelle taille : {0:.2f} MB",
        'progress_cancelling': "Annulation...",
        'progress_cancel_message': "Annulation de {0}",
        'progress_pages_found_moving': "{0} pages trouvées, {1} à déplacer",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analyse du PDF...",
        'ocr_status_optimizing': "Optimisation de l'image en cours...",
        'ocr_status_recognizing': "Reconnaissance de texte en cours...",
        'ocr_status_embedding': "Incorporation du texte...",
        'ocr_status_finalizing': "Finalisation du PDF...",

        # PDF-Laden
        'progress_preparing': "Préparation...",
        'progress_loading': "Chargement du PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Suppression des pages...",
        'progress_moving_title': "Déplacement des pages...",
        'pages_found': "Pages trouvées",
        'progress_creating_new_order': "Création d'un nouvel ordre...",
        'progress_sorting_pages': "Tri des pages...",
        'progress_moving_to_begin': "Déplacer {0} pages au début",
        'progress_transferring_count': "Transférer {0} pages",
        'progress_transferring_before_target': "Transférer les pages avant la cible",
        'progress_moving_pages': "Déplacer {0} pages",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_sauvegarde_",
        'filename_protected_suffix': "_protege_",
        'filename_copy_suffix': "_Copie",
        'filename_page_single': "_Page_",
        'filename_page_range': "_Pages_",
        'filename_export_page': "_Page_{0:03}",
        'filename_export_range': "_Pages_{0}-{1}",
        'filename_export_multiple': "_Pages_{0}",
        'filename_with_text': "_avec_Texte",
        'filename_with_signature': "_avec_Signature",
        'filename_with_image': "_avec_Image",
        'filename_with_forms': "_avec_Formes",
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
        'view_toggle_navbar': "Afficher la barre de boutons",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Impossible de supprimer toutes les pages",
		'pages_cannot_delete_last_page': 'La dernière page ne peut pas être supprimée !',
		'pages_cannot_delete_all_pages': 'Au moins une page doit rester dans le document !',
		'delete_pages_confirm': 'Êtes-vous sûr de vouloir supprimer {0} pages ?',
		'delete_pages_confirm_voice': 'Êtes-vous sûr de vouloir supprimer {0} pages ?',
		'pages_deleted': '{0} pages ont été supprimées avec succès.',
		'warning': 'Avertissement',
		'error': 'Erreur',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Aucun formulaire sélectionné",
        'form_customized': "Formulaire personnalisé",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Sélectionner",
        'btn_use': "Utiliser",
        'master_password_for_spasswords': "Pour stocker et utiliser des mots de passe, vous devez d'abord configurer un mot de passe maître.\n\nVoulez-vous configurer le mot de passe maître maintenant ?",
        'open_saved_dialog_title': "Ouvrir le fichier enregistré",
        'open_saved_question': "Voulez-vous ouvrir le fichier enregistré maintenant ?",
        'password': "Mot de passe",
        'password_manager_master_required': "Le gestionnaire de mots de passe n'est disponible que si un mot de passe maître a été configuré.\n\nVoulez-vous configurer le mot de passe maître maintenant ?",
        'password_master_required_for_select': "Pour afficher et sélectionner les mots de passe enregistrés, vous devez d'abord vous authentifier avec votre mot de passe maître.\n\nVoulez-vous vous authentifier maintenant ?",
        'password_not_available': "Le mot de passe sélectionné n'est pas disponible ou n'a pas pu être déchiffré.",
        'password_options_title': "Options du mot de passe",
        'password_save_choice_change': "Définir un nouveau mot de passe",
        'password_save_choice_keep': "Utiliser le mot de passe existant",
        'password_save_choice_none': "Enregistrer non chiffré",
        'password_save_hint': "Configurez d'abord un mot de passe maître pour stocker les mots de passe en toute sécurité.",
        'password_save_master_required': "Enregistrer le mot de passe (possible uniquement avec mot de passe maître)",
        'password_save_question': "Le PDF actuel est protégé par mot de passe. Voulez-vous utiliser le mot de passe existant, en définir un nouveau ou l'enregistrer non chiffré ?",
        'password_select': "Sélectionner le mot de passe",
        'password_select_none': "Aucun mot de passe sélectionné.\n\nVeuillez sélectionner un mot de passe dans la liste.",
        'password_select_one': "Veuillez sélectionner exactement un mot de passe.\n\nVous avez marqué plusieurs mots de passe.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_sauvegarde",
        'filename_insert_suffix': "_avec_insertion",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_pages_supprimées",
        'filename_pages_moved': "_pages_déplacées",
        'filename_rotated_all_suffix': "_toutes_pages_pivotées",
        'filename_rotated_suffix': "_page_pivotée",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configuration des noms de fichiers lors des modifications du PDF",
        'filename_keep_suffixes': "Conserver les extensions précédentes (ex. _avec_texte)",
        'filename_keep_suffixes_false': "Remplacer",
        'filename_keep_suffixes_true': "Conserver",
        'filename_preview_label': "Aperçu du nom de fichier :",
        'filename_preview_overwrite_hint': "Aperçu non disponible – l'original sera écrasé.",
        'filename_separator': "Séparateur entre les mots",
        'filename_separator_none': "Aucun séparateur",
        'filename_separator_space': "Espace ( )",
        'filename_separator_underscore': "Tiret bas (_)",
        'filename_settings_saved': "Paramètres de nom de fichier enregistrés",
        'filename_settings_title': "Formatage du nom de fichier et sauvegarde",
        'filename_timestamp_position': "Position de l'horodatage",
        'filename_timestamp_position_after': "Après le nom de base",
        'filename_timestamp_position_before': "Tout devant",
        'filename_timestamp_position_end': "À la fin",
        'filename_use_timestamp': "Utiliser l'horodatage",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Comportement lors des modifications :</b><ul><li>Supprimer et insérer des pages</li><li>Insérer du texte, une signature, une image et des formes</li><li>OCR</li></ul></html>",
        'backup_section': "Sauvegarde pour les opérations sur les pages (Supprimer, Déplacer)",
        'behavior_info': "Remarque : Avec 'Écraser l'original', les horodatages et suffixes sont ignorés – le fichier conserve son nom.",
        'behavior_new_file': "Toujours créer un nouveau fichier (avec horodatage et suffixe)",
        'behavior_overwrite': "Écraser l'original (pas de nouveau fichier)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Toutes les pages ont été pivotées.\n\nL'original est resté inchangé.\nNouveau fichier : {0}",
        'all_pages_rotated_voice': "Toutes les pages pivotées, nouveau fichier créé.",
        'empty_pages_deleted_new_file': "{0} pages vides ont été supprimées.\n\nL'original est resté inchangé.\nNouveau fichier : {1}",
        'empty_pages_deleted_voice': "{0} pages vides supprimées, nouveau fichier créé.",
        'ocr_keep_original': "Conserver l'original (ouvrir manuellement plus tard)",
        'ocr_new_file_question': "Le nouveau PDF consultable a été enregistré sous :\n{0}\n\nVoulez-vous l'ouvrir maintenant ?",
        'ocr_open_new': "Ouvrir le nouveau fichier OCR",
        'ocr_original_kept': "Le fichier original reste ouvert. Le fichier OCR a été enregistré.",
        'page_deleted_new_file': "La page {0} a été supprimée.\n\nL'original est resté inchangé.\nNouveau fichier : {1}",
        'page_deleted_voice': "Page {0} supprimée, nouveau fichier créé.",
        'page_rotated_new_file': "La page {0} a été pivotée.\n\nL'original est resté inchangé.\nNouveau fichier : {1}",
        'page_rotated_voice': "Page {0} pivotée, nouveau fichier créé.",
        'pages_deleted_new_file': "{0} pages ont été supprimées.\n\nLe fichier original est resté inchangé.\nNouveau fichier : {1}",
        'pages_deleted_new_file_voice': "{0} pages supprimées, nouveau fichier créé.",
        'pages_inserted_new_file': "{0} pages ont été insérées.\n\nLe fichier original est resté inchangé.\nNouveau fichier : {1}",
        'pages_inserted_new_file_ask': "{0} pages ont été insérées.\n\nL'original est resté inchangé.\nNouveau fichier : {1}\n\nVoulez-vous l'ouvrir maintenant ?",
        'pages_inserted_voice_new': "{0} pages insérées, nouveau fichier créé.",
        'pages_moved_new_file': "{0} pages ont été déplacées.\n\nLe fichier original est resté inchangé.\nNouveau fichier : {1}",
        'pages_moved_new_file_voice': "{0} pages déplacées, nouveau fichier créé.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ne plus afficher",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Paramètre de sauvegarde</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Sauvegarde ACTIVÉE</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Pour toutes les modifications qui écrasent l'original</strong> (texte, signature, image, forme, OCR, pivoter, insérer, supprimer/déplacer des pages), <strong>une sauvegarde avec horodatage est automatiquement créée</strong> avant l'application de la modification.</p>
                <p style="margin: 5px 0 5px 20px;">• La sauvegarde se trouve à côté du fichier original (ex. <code>Document_sauvegarde_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Si vous avez en plus activé l'option <strong>„Écraser l'original“</strong>, une sauvegarde est également créée.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Sauvegarde DÉSACTIVÉE</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Aucune sauvegarde n'est créée</strong> – ni lors de l'écrasement, ni lors des opérations sur les pages.</p>
                <p style="margin: 5px 0 5px 20px;">• Le fichier original peut être perdu de manière irréversible lors de l'écrasement.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Recommandé uniquement pour les utilisateurs expérimentés !</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Astuce :</strong> Le paramètre de sauvegarde est indépendant de l'option „Écraser l'original“. Vous pouvez combiner les deux.<br>
                Vous pouvez masquer définitivement ce message.
            </div>
        </div>
        """,
        'backup_info_title': "Comportement de la sauvegarde",
        'backup_info_voice': "Avis sur le comportement de la sauvegarde lors des opérations sur les pages. Sauvegarde activée écrase l'original, sauvegarde désactivée crée un nouveau fichier.",
        'show_backup_info': "Informations sur le paramètre de sauvegarde",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ne plus afficher",
        'overwrite_enable_backup': "Activer la sauvegarde (recommandé)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Écraser l'original</p>
            <p>Si vous activez cette option, les modifications (texte, signature, image, forme, OCR, pivoter, insérer) sont <strong>enregistrées directement dans l'original</strong> – <strong>aucun nouveau fichier n'est créé</strong>.</p>
            <p>• Le nom du fichier reste inchangé.<br>
            • Les horodatages et suffixes sont ignorés.<br>
            • <strong>Sans sauvegarde, l'original peut être perdu de manière irréversible.</strong></p>
            <p style="color: #FFD700;">Recommandation : Activez également l'option de sauvegarde pour obtenir des copies de sécurité automatiques.</p>
        </div>
        """,
        'overwrite_info_title': "Écraser l'original",
        'overwrite_info_voice': "Avertissement : Écraser l'original – pas de nouveau fichier. Sauvegarde recommandée.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} pages ont été insérées.\n\nLe fichier original a été écrasé.\nUne sauvegarde a été créée.",
        'pages_inserted_overwrite_no_backup': "{0} pages ont été insérées.\n\nLe fichier original a été écrasé.\nAUCUNE sauvegarde n'a été créée.",
        'texts_saved_overwrite_with_backup': "Les modifications ont été enregistrées dans l'original.\n\nUne sauvegarde a été créée.",
        'texts_saved_overwrite_no_backup': "Les modifications ont été enregistrées dans l'original.\n\nAUCUNE sauvegarde n'a été créée.",
        'texts_crosses_saved_new_file': "{0} {1} et {2} {3} ont été insérés.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",
        'texts_saved_new_file': "{0} {1} ont été insérés.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",
        'crosses_saved_new_file': "{0} {1} ont été insérés.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",
        'elements_saved_new_file': "{0} éléments ont été insérés.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",
        'signatures_saved_overwrite_with_backup': "La/les signature(s) a/ont été enregistrée(s) dans l'original.\n\nUne sauvegarde a été créée.",
        'signatures_saved_overwrite_no_backup': "La/les signature(s) a/ont été enregistrée(s) dans l'original.\n\nAUCUNE sauvegarde n'a été créée.",
        'images_saved_overwrite_with_backup': "L'/Les image(s) a/ont été enregistrée(s) dans l'original.\n\nUne sauvegarde a été créée.",
        'images_saved_overwrite_no_backup': "L'/Les image(s) a/ont été enregistrée(s) dans l'original.\n\nAUCUNE sauvegarde n'a été créée.",
        'forms_saved_overwrite_with_backup': "La/Le forme(s) a/ont été enregistrée(s) dans l'original.\n\nUne sauvegarde a été créée.",
        'forms_saved_overwrite_no_backup': "La/Le forme(s) a/ont été enregistrée(s) dans l'original.\n\nAUCUNE sauvegarde n'a été créée.",
        'signatures_saved_new_file': "{0} signatures ont été insérées.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",
        'images_saved_new_file': "{0} images ont été insérées.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",
        'forms_saved_new_file': "{0} formes ont été insérées.\n\nLe fichier original est resté inchangé.\nUn nouveau fichier a été créé.\n\nChargement du nouveau PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Attention : Ce PDF contient des pages pivotées. Le positionnement peut être différent.",
        'page_rotated_warning_title': "Page pivotée détectée",
        'page_rotated_warning_message': "La page actuelle {0} est pivotée de {1}°.\n\nL'insertion d'éléments sur des pages pivotées n'est pas prise en charge.\n\nVoulez-vous pivoter la page maintenant en position verticale ?",
        'page_rotated_warning_voice': "Attention : La page est pivotée. Veuillez d'abord la pivoter.",
        'paste_on_rotated_page_simple_warning': "Insertion sur la page {0} impossible !\n\nCette page est pivotée de {1}°.\n\nVeuillez d'abord pivoter la page à 0° (Menu : Éditer → Aligner la page).\n\nAttention :\nL'élément précédemment copié sera perdu si vous n'enregistrez pas avant de pivoter la page.",
        'paste_on_rotated_page_voice': "Insertion annulée. La page est pivotée. Veuillez d'abord aligner la page.",
        'page_rotated_cancel': "Annuler",
        'page_rotated_rotate_until_upright': "Pivoter la page plusieurs fois (jusqu'à ce qu'elle soit verticale)",
        'page_rotated_now_upright': "La page est maintenant verticale. Vous pouvez maintenant insérer.",
        'page_rotated_still_not_upright': "La page n'a pas pu être pivotée en position verticale. Veuillez corriger manuellement.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Aide : Corriger les pages pivotées",
        'help_rotated_pages_voice': "L'aide pour corriger les pages pivotées s'ouvre.",
        'btn_help': "Aide",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problème : Page pivotée – L'insertion ne fonctionne pas correctement</p>

            <p>Si l'insertion de textes, de signatures ou de formes sur une page pivotée ne fonctionne pas correctement, vous pouvez corriger la page avec un éditeur PDF externe.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solution avec un outil externe (ex. Aperçu macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exporter la page</strong><br>
                &nbsp;&nbsp;Cliquez dans le menu sur <strong>Fichier → Exporter comme pages</strong> ou utilisez une autre méthode pour enregistrer la page souhaitée en tant que PDF unique.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Ouvrir la page dans un programme externe</strong><br>
                &nbsp;&nbsp;Ouvrez le PDF exporté dans un éditeur PDF (ex. <strong>Aperçu macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Pivoter la page</strong><br>
                &nbsp;&nbsp;Pivotez la page pour qu'elle soit verticale (dans Aperçu : <strong>Outils → Pivoter</strong> ou <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Enregistrer</strong><br>
                &nbsp;&nbsp;Enregistrez la page corrigée (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Réinsérer la page dans le document original</strong><br>
                &nbsp;&nbsp;Revenez à PDFDarkView et insérez la page corrigée à la position souhaitée :<br>
                &nbsp;&nbsp;<strong>Éditer → Insérer des pages</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternative : Pivoter la page dans l'original</p>
                <p style="margin: 5px 0 5px 20px;">• Utilisez la fonction de pivotement intégrée (<strong>Éditer → Pivoter la page</strong>) pour corriger la page étape par étape.<br>
                • Après chaque pivotement, vous pouvez vérifier si l'insertion fonctionne maintenant.<br>
                • C'est souvent la solution la plus rapide – essayez-la d'abord !</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Astuce :</strong> Si vous rencontrez fréquemment des pages pivotées, vous pouvez masquer définitivement l'avertissement dans la boîte de dialogue d'insertion.<br>
                Le positionnement peut alors être différent – n'utilisez cette option que si vous en connaissez les conséquences.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Aligner les pages",
        'menu_rotate_normalize_tooltip': "Pivoter la page ou réinitialiser à 0°",
        'normalize_current_page': "Mettre la page actuelle en position verticale (régler à 0°)",
        'normalize_all_pages': "Mettre toutes les pages en position verticale (régler à 0°)",
        'page_normalized': "La page {0} a été mise en position verticale.",
        'all_pages_normalized': "Toutes les pages ont été mises en position verticale.",
        'page_already_upright': "La page {0} est déjà verticale.",
        'all_pages_already_upright': "Toutes les pages sont déjà verticales.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>Le PDF ne contient pas de texte consultable.</p><p>Voulez-vous effectuer une OCR pour exporter vers {0} ?</p>",
        'export_ocr_voice': "Le PDF ne contient pas de texte. Une OCR est requise pour l'exportation vers {0}.",
        'export_no_ocr_possible': "L'exportation sans OCR n'est pas possible. Veuillez effectuer une OCR via le menu.",
        'ocr_failed_export_not_possible': "L'OCR a échoué. L'exportation ne peut pas être effectuée.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "Le PDF s'ouvrira dans Aperçu. Veuillez y lancer le processus d'impression.",
        'print_preview_manual': "Le PDF a été ouvert. Veuillez exécuter la commande d'impression manuellement (ex. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Fusionner les PDF",
        'merge_pdfs': "Fusionner les PDF",
        'merge_progress_title': "Fusion des PDF en cours...",
        'merge_pdfs_list': "PDF dans l'ordre (Glisser-déposer pour trier)",
        'merge_add_pdf': "Ajouter un PDF",
        'merge_remove': "Supprimer",
        'merge_move_up': "Monter",
        'merge_move_down': "Descendre",
        'merge_pdfs_info': "💡 Astuce : Vous pouvez modifier l'ordre par glisser-déposer",
        'merge_no_pdfs': "Aucun PDF sélectionné. Cliquez sur 'Ajouter un PDF'.",
        'merge_info': "{0} PDF sélectionnés (environ {1} pages)",
        'merge_open_file': "Ouvrir le fichier",
        'merge_merge': "Fusionner",
        'merge_error': "Erreur lors de la fusion",
        'merge_min_two_pdfs_error': "Veuillez sélectionner au moins deux fichiers PDF à fusionner.",
        'merge_select_pdfs': "Sélectionner les PDF à fusionner",
        'merge_error_file': "Erreur lors du traitement",
        'merge_cancelled': "La fusion a été annulée",
        'merge_preparing': "Préparation...",
        'merge_processing': "Traitement du PDF {0} sur {1}",
        'merge_saving': "Enregistrement du PDF fusionné...",
        'merge_complete': "Terminé !",
        'merge_success_title': "Fusion réussie",
        'merge_success_voice': "{0} PDF ont été fusionnés avec succès.",
        'merge_success_message': "{0} PDF ont été fusionnés avec succès.\n\nLe nouveau document contient maintenant {1} pages.\n\nNouveau fichier :\n{2}\n\nEmplacement d'enregistrement :\n{3}\n{2}\n\nVoulez-vous ouvrir ce PDF ?",
        'replace_file_title': "Remplacer le fichier ?",
        'replace_file_message': "Un PDF est déjà ouvert. Voulez-vous le remplacer par le nouveau fichier ?",
        'btn_yes': "Oui",
        'btn_no': "Non",
        'filename_merge_suffix': "fusionné",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Ouverture de {0}...",
        'progress_merge_reading': "Lecture de {0}...",
        'progress_merge_adding': "Ajout de {0} pages...",
        'progress_merge_optimizing': "Optimisation du PDF...",
        'progress_merge_writing': "Écriture du PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "la fermeture du PDF",
        'action_close_window': "la fermeture de la fenêtre",
        'action_open_new_pdf': "l'ouverture d'un nouveau PDF",
        'action_quit_app': "la fermeture de l'application",
        'changes_saved': "Les modifications ont été enregistrées.",
        'file_close_title': "Fermer le fichier PDF",
        'save_before_action': "Faut-il enregistrer les modifications avant {0} ? Oui ou Non ?",
        'save_before_action_voice': "Faut-il enregistrer les modifications avant {0} ? Oui ou Non ?",
        'save_before_close_question': "Faut-il enregistrer les modifications avant la fermeture ? Oui ou Non ?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF consultable créé :\n\n{0}\n\n<b>réessayez si nécessaire",
        "ocr_rotate_title": "Alignement des pages avant OCR",
        "ocr_rotate_question": "Le PDF contient des pages pivotées.\nVoulez-vous aligner toutes les pages à 0° avant l'OCR ?\nCela améliore considérablement la reconnaissance de texte.",
        "ocr_rotate_yes": "Oui, aligner",
        "ocr_rotate_no": "Non, démarrer l'OCR directement",
        "ocr_rotate_voice": "Le PDF contient des pages pivotées. Faut-il aligner toutes les pages avant l'OCR ?",
        "ocr_not_performed_message": "Aucun texte présent. Veuillez effectuer une OCR (menu \"Éditer\" → \"Effectuer OCR\" ou touche Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Paramètres OCR",
        "ocr_language_btn": "Sélectionner la langue OCR",
        "ocr_language": "Langue(s) OCR",
        "ocr_language_current": "Langue actuelle :",
        "ocr_param_info": "Informations sur le paramètre",

        "ocr_force_ocr_label": "Forcer l'OCR",
        "ocr_deskew_label": "Corriger l'inclinaison",
        "ocr_clean_label": "Nettoyer l'image",
        "ocr_oversample_label": "Résolution (DPI)",
        "ocr_pagesegmode_label": "Segmentation de page",
        "ocr_oem_label": "Mode moteur OCR",
        "ocr_optimize_label": "Compression PDF",
        "ocr_jobs_label": "Processus parallèles",
        "ocr_verbose_label": "Détail du journal",

        "ocr_force_ocr_tooltip": "Forcer l'OCR sur chaque page, même si du texte existe déjà",
        "ocr_deskew_tooltip": "Aligner automatiquement les scans inclinés",
        "ocr_clean_tooltip": "Supprimer le bruit et les artéfacts de l'image",
        "ocr_oversample_tooltip": "Agrandir l'image avant l'OCR à ce DPI",
        "ocr_pagesegmode_tooltip": "Détermine comment la page est divisée en zones de texte",
        "ocr_oem_tooltip": "Sélectionne le moteur OCR de Tesseract",
        "ocr_optimize_tooltip": "Niveau de compression du PDF de sortie",
        "ocr_jobs_tooltip": "Nombre de processus OCR parallèles",
        "ocr_verbose_tooltip": "Niveau de détail de la sortie du journal",
        "ocr_settings_explain_btn": "Explication",

        "ocr_force_ocr_explain": "Force la reconnaissance de texte sur <b>chaque</b> page, même si elle contient déjà du texte.\n\nRecommandation : <b>Activer</b> pour les PDF scannés, <b>Désactiver</b> pour les PDF natifs avec texte déjà existant.",

        "ocr_deskew_explain": "Corrige les scans légèrement inclinés (jusqu'à environ 5°).\n\nRecommandation : <b>Activer</b> pour les documents scannés, <b>Désactiver</b> si les pages sont déjà parfaitement droites.",

        "ocr_clean_explain": "Supprime le bruit, les points et les petits artéfacts de l'image.\n<b>IMPORTANT :</b> Pour les textes arabes, thaïlandais ou vietnamiens avec signes diacritiques (points au-dessus/en dessous des lettres), cette option doit être <b>désactivée</b>, sinon des caractères importants peuvent être perdus.",

        "ocr_oversample_explain": "Agrandit l'image <b>avant</b> la reconnaissance de texte au DPI spécifié.<br><br>• <b>72-150 DPI :</b> Très rapide, mais faible taux de reconnaissance<br>• <b>200-300 DPI :</b> Plage optimale (Par défaut : 300)<br>• <b>400+ DPI :</b> Reconnaissance à peine meilleure, mais fichiers nettement plus gros<br><br>Recommandation : 300 DPI pour les écritures complexes (arabe, chinois, japonais), 200 DPI pour les langues occidentales.",

        "ocr_pagesegmode_explain": "Détermine comment Tesseract divise la page en zones de texte.\n\n• <b>3 - Automatique (Par défaut) :</b> Bon pour les mises en page mixtes\n• <b>4 - Colonne unique :</b> Pour les textes à une colonne\n• <b>5 - Bloc vertical :</b> Pour les écritures verticales (japonais, chinois)\n• <b>6 - Bloc de texte uniforme :</b> Optimal pour le texte fluide sans colonnes\n• <b>11 - Image brute :</b> Pour les mauvais scans / écriture manuscrite\n\nRecommandation : <b>6</b> pour les documents texte simples, <b>3</b> pour les mises en page complexes.",

        "ocr_oem_explain": "Sélectionne le moteur OCR de Tesseract.\n\n• <b>0 - Legacy :</b> Ancien moteur (rapide, mais moins précis)\n• <b>1 - LSTM :</b> Moteur neuronal (plus lent, mais plus précis)\n• <b>2 - Legacy + LSTM :</b> Combine les deux résultats\n• <b>3 - Par défaut (LSTM préféré) :</b> Meilleur choix pour la plupart des cas\n\nRecommandation : <b>3</b> pour une précision de reconnaissance maximale.",

        "ocr_optimize_explain": "Compresse le PDF de sortie.\n\n• <b>0 :</b> Aucune optimisation (traitement le plus rapide)\n• <b>1 :</b> Optimisation légère (bon compromis)\n• <b>2 :</b> Optimisation modérée\n• <b>3 :</b> Optimisation forte (fichier le plus petit, mais plus lent)\n\nRecommandation : <b>1</b> pour une utilisation quotidienne.",

        "ocr_jobs_explain": "Nombre de processus parallèles pour l'OCR.\n\n• <b>1 :</b> Lent, mais consommation mémoire la plus faible\n• <b>4-8 :</b> Optimal pour les processeurs multi-cœurs modernes\n• <b>12+ :</b> Traitement à peine plus rapide avec une consommation mémoire élevée\n\nRecommandation : Nombre de cœurs CPU (ex. <b>4</b> sur les systèmes 4 cœurs).",

        "ocr_verbose_explain": "Niveau de détail de la sortie du journal dans la console.\n\n• <b>0 :</b> Aucune sortie\n• <b>1 :</b> Progression et messages d'état\n• <b>2 :</b> Sortie détaillée\n• <b>3 :</b> Sortie de débogage complète (très volumineuse)\n\nRecommandation : <b>1</b> pour un fonctionnement normal.",

        "ocr_reset_title": "Paramètres réinitialisés",
        "ocr_reset_message": "Tous les paramètres OCR ont été réinitialisés aux valeurs par défaut.",
        "info_tooltip": "Plus d'informations sur ce paramètre",
        "ocr_reset_defaults": "Réinitialiser aux valeurs par défaut",

        "ocr_psm_0": "Automatique (moteur Legacy)",
        "ocr_psm_1": "Détection automatique des colonnes",
        "ocr_psm_3": "Automatique (Par défaut)",
        "ocr_psm_4": "Colonne unique",
        "ocr_psm_5": "Bloc vertical",
        "ocr_psm_6": "Bloc de texte uniforme",
        "ocr_psm_7": "Ligne de texte unique",
        "ocr_psm_8": "Mot unique",
        "ocr_psm_11": "Image brute (sans analyse de mise en page)",

        "ocr_oem_0": "Moteur Legacy (rapide)",
        "ocr_oem_1": "Moteur LSTM (neuronal, précis)",
        "ocr_oem_2": "Legacy + LSTM combiné",
        "ocr_oem_3": "Par défaut (LSTM préféré)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Langue(s) OCR...",
        "ocr_language_title": "Sélectionner la/les langue(s) OCR",
        "ocr_language_instruction": "Sélectionnez la/les langue(s) pour la reconnaissance de texte (OCR).\nAttention : Plusieurs langues se font au détriment des performances et de la précision !\nVous obtenez les meilleurs résultats si vous ne sélectionnez qu'une seule langue.",
        "ocr_language_predefined": "Combinaisons prédéfinies",
        "ocr_language_custom": "Personnalisé...",
        "ocr_language_selected": "Langues OCR sélectionnées",
        "ocr_language_changed": "Langue OCR changée en {0}",
        "ocr_language_auto_detect": "Les langues disponibles sont détectées automatiquement.",
        "ocr_language_none_found": "Aucune donnée linguistique Tesseract trouvée ! Veuillez installer les paquets de langue (ex. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Sélection de langue personnalisée",
        "ocr_language_available": "Langues disponibles (installées) :",
        "ocr_language_select_hint": "Sélectionnez une ou plusieurs langues :",
        "ocr_language_confirm": "Appliquer",
        "ocr_language_reset": "Réinitialiser aux valeurs par défaut (deu+eng+vie)",
        "ocr_language_priorities": "Langues recommandées (préinstallées) :",

        "select_all_languages": "Tout sélectionner",
        "clear_all_languages": "Effacer la sélection",
        "install_language_packs": "Installer les paquets de langue manquants...",
        "install_hint": "💡 Astuce : Toutes les langues ne sont pas installées sur votre système. Ce bouton vous aidera à les installer.",
        "ocr_language_install_title": "Installation des paquets de langue Tesseract",

        "ocr_missing_languages": "Paquets de langue OCR manquants",
        "ocr_missing_languages_message": "Les langues sélectionnées suivantes ne sont pas installées sur votre système :\n\n{0}\n\nVeuillez installer les paquets de langue manquants (voir l'aide dans 'Aide à l'installation').\n\nVoulez-vous ouvrir l'aide à l'installation maintenant ?",
        "ocr_missing_languages_voice": "Paquets de langue manquants. Veuillez installer les langues manquantes.",
        "ocr_install_help_now": "Ouvrir l'aide",
        "ocr_continue_anyway": "Essayer quand même",
        "ocr_language_error_title": "Erreur de langue OCR",
        "ocr_language_error_message": "Erreur lors de la reconnaissance de texte : {0}\n\nVeuillez vérifier vos paramètres de langue OCR (Paramètres → Langue OCR).",
        "ocr_install_help_button": "Aide à l'installation",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Installer les paquets de langue Tesseract</p>

        <p>Pour que l'OCR fonctionne dans une langue spécifique, les données linguistiques correspondantes doivent être installées sur votre système. Suivez les instructions pour votre système d'exploitation :</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Ouvrez le <strong>Terminal</strong> (Finder → Programmes → Utilitaires → Terminal).</li>
        <li>Installez toutes les langues disponibles avec :<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Cela peut prendre quelques minutes.)</li>
        <li>Ou seulement des langues individuelles (ex. vietnamien) :<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Avec les versions actuelles de Homebrew, <code>*.traineddata</code> peut devoir être téléchargé manuellement (voir ci-dessous).</li>
        <li>Après l'installation : Fermez cette boîte de dialogue et rouvrez la sélection de langue OCR – les nouvelles langues apparaîtront automatiquement.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Ouvrez un terminal (Ctrl+Alt+T).</li>
        <li>Installez la langue souhaitée, par exemple pour le vietnamien :<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Codes de langue importants : <code>deu</code> (allemand), <code>eng</code> (anglais), <code>vie</code> (vietnamien), <code>spa</code> (espagnol), <code>fra</code> (français), <code>ita</code> (italien), <code>nld</code> (néerlandais), <code>fin</code> (finnois), <code>swe</code> (suédois), <code>nor</code> (norvégien).</li>
        <li>Afficher tous les paquets disponibles :<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuel)</p>
        <ol>
        <li>Téléchargez les fichiers <code>*.traineddata</code> souhaités depuis :<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ex. <code>vie.traineddata</code> pour le vietnamien).</li>
        <li>Copiez les fichiers dans le dossier des langues de Tesseract, généralement :<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Adaptez selon l'installation individuelle.)</li>
        <li>Redémarrez l'application (ou rouvrez la sélection de langue OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternative pour tous les systèmes</p>
        <ul>
        <li>Installez <strong>OCRmyPDF</strong> et <strong>Tesseract</strong> avec un gestionnaire de paquets de votre choix. La plupart des installations contiennent déjà quelques langues standard (anglais, allemand, français).</li>
        <li>Les langues manquantes peuvent être installées à tout moment – la sélection de langue OCR ne liste que les langues réellement existantes.</li>
        </ul>

        <hr>
        <p><b>✅ Après l'installation :</b> Pas besoin de redémarrer l'application – les langues nouvellement ajoutées apparaîtront immédiatement dans la liste.</p>
        <p><b>📖 Aide sur les codes de langue :</b> Une liste complète est disponible dans la <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">documentation Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Polices Noto Sans",
        "info_noto_font_voice": "Guide d'installation des polices Noto Sans",
        "btn_info_noto_font_install": "Info police",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Comment installer les polices gratuites Noto de Google</h2>

        <p>Les <strong>polices Noto</strong> sont une famille de polices open source de Google. Leur objectif est de ne voir <em>"aucun tofu"</em> (c'est-à-dire aucune boîte vide □) et d'afficher correctement chaque caractère de la norme Unicode. Elles sont le complément idéal pour les applications qui doivent afficher des textes dans de nombreuses langues différentes.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installation sur macOS</h3>

        <p><strong>Méthode 1 : Avec Homebrew (pour les avancés)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Méthode 2 : Via l'application "Font Book" (Recommandé)</strong></p>

        <ol>
        <li>Téléchargez le pack de polices officiel :<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extrayez le fichier ZIP</li>
        <li>Copiez les fichiers dans <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installation sur Windows (10 & 11)</h3>

        <p><strong>Méthode 1 : Microsoft Store (Recommandé)</strong><br>
        Recherchez "Google Noto Fonts" ou "Noto Sans" et cliquez sur <strong>Installer</strong>.</p>

        <p><strong>Méthode 2 : Installation manuelle</strong></p>

        <ol>
        <li>Téléchargement :<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extrayez le ZIP</li>
        <li>Sélectionnez les fichiers .ttf / .otf</li>
        <li>Clic droit → <strong>Installer</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ou<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nom\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installation sur Linux</h3>

        <ul style='list-style: none; padding-left: 0;'>

        <li><strong>Ubuntu / Debian :</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo apt update && sudo apt install fonts-noto-core fonts-noto-cjk fonts-noto-extra</pre>
        </li>

        <li><strong>Fedora :</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo dnf install google-noto-sans-cjk-ttc</pre>
        </li>

        <li><strong>Arch :</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo pacman -S noto-fonts noto-fonts-cjk</pre>
        </li>

        <li><strong>openSUSE :</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo zypper install google-noto-fonts</pre>
        </li>

        </ul>

        <p>Vérification :<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Gérer les signets",
        "bookmark_add": "Ajouter un signet",
        "bookmark_add_tooltip": "Enregistrer la page actuelle comme signet",
        "bookmark_remove": "Supprimer le signet",
        "bookmark_remove_tooltip": "Supprimer le signet marqué",
        "bookmark_remove_all": "Tout supprimer",
        "bookmark_remove_all_tooltip": "Supprimer tous les signets de ce PDF",
        "bookmark_jump": "Aller au signet",
        "bookmark_jump_tooltip": "Aller à la page sélectionnée",
        "bookmark_name": "Nom",
        "bookmark_page": "Page",
        "bookmark_no_bookmarks": "Aucun signet présent.\nCliquez sur 'Ajouter' pour enregistrer la page actuelle comme signet.",
        "bookmark_added": "Signet pour la page {0} ajouté : {1}",
        "bookmark_removed": "Signet supprimé : {0}",
        "bookmark_all_removed": "Tous les signets ont été supprimés.",
        "bookmark_name_default": "Page {0}",
        "bookmark_name_prompt": "Nom du signet :\n(le texte long sera raccourci à 50 caractères)",
        "bookmark_name_prompt_title": "Nom du signet",
        "bookmark_confirm_remove_all": "Êtes-vous sûr de vouloir supprimer les {0} signets ?",
        "menu_bookmarks": "Signets",
        "bookmark_manage": "Gérer les signets",
        "bookmark_next": "Signet suivant",
        "bookmark_prev": "Signet précédent",
        "bookmark_page_display": "Page {0}",
        "bookmark_exists": "Un signet pour cette page avec ce nom existe déjà.",
        "bookmark_select_first": "Veuillez d'abord sélectionner un signet.",
        "bookmark_confirm_remove": "Êtes-vous sûr de vouloir supprimer le signet 'Page {0} : {1}' ?",
        "bookmark_jumped_to": "Aller au signet '{0}' à la page {1}.",
        "bookmark_jumped_to_voice": "Signet {0}, page {1}",
        "btn_close": "Fermer",

        "bookmark_list": "Vos signets",
        "bookmark_rename": "Renommer le signet",
        "bookmark_rename_tooltip": "Changer le nom du signet sélectionné",
        "bookmark_rename_title": "Renommer le signet",
        "bookmark_rename_prompt": "Nouveau nom pour le signet à la page {0} :\n(max. 50 caractères)",
        "bookmark_renamed": "Le signet '{0}' a été renommé en '{1}'.",
        "bookmark_item_tooltip": "Page {0} : {1}\nDouble-clic pour y aller",
        "bookmark_name_exists_question": "Un signet nommé '{0}' existe déjà sur cette page.\nRenommer quand même ?",

        "context_bookmarks": "Signets",
        "context_bookmark_add_here": "Ajouter un signet pour cette page",
        "context_bookmarks_existing": "Signets existants :",
        "context_bookmarks_jump": "Aller au signet :",
        "context_bookmarks_none": "Aucun signet présent",
        "context_bookmarks_clear_all": "Supprimer les {0} signets",

        "bookmark_search_placeholder": "Rechercher des signets... (nom ou page)",
        "bookmark_search_results": "%d signets trouvés pour \"%s\"",
        "bookmark_no_search_results": "Aucun signet trouvé pour \"%s\"",
        "bookmark_no_search_results_label": "Aucun résultat pour \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Modifier les métadonnées PDF",
        "metadata_title": "Titre",
        "metadata_title_placeholder": "Titre du document",
        "metadata_title_tooltip": "Le titre du document (affiché dans la barre de titre)",
        "metadata_author": "Auteur",
        "metadata_author_placeholder": "Nom de l'auteur",
        "metadata_author_tooltip": "Le créateur du document",
        "metadata_subject": "Sujet",
        "metadata_subject_placeholder": "Sujet du document",
        "metadata_subject_tooltip": "Une brève description du contenu",
        "metadata_keywords": "Mots-clés",
        "metadata_keywords_placeholder": "Mots-clés séparés par des virgules",
        "metadata_keywords_tooltip": "Mots-clés pour catégoriser le document",
        "metadata_creator": "Créateur",
        "metadata_creator_placeholder": "Application qui a créé le PDF",
        "metadata_creator_tooltip": "Le logiciel avec lequel le document a été créé",
        "metadata_producer": "Producteur",
        "metadata_producer_placeholder": "Application qui a converti le PDF",
        "metadata_producer_tooltip": "Le logiciel qui a converti le PDF",
        "metadata_creation_date": "Date de création",
        "metadata_creation_date_tooltip": "La date de création du document",
        "metadata_mod_date": "Date de modification",
        "metadata_mod_date_tooltip": "La date de la dernière modification",
        "metadata_pdf_info": "📄 Informations PDF",
        "metadata_pages": "Nombre de pages",
        "metadata_file_size": "Taille du fichier",
        "metadata_pdf_version": "Version PDF",
        "metadata_encrypted": "Chiffré",
        "metadata_encrypted_yes": "Oui (protégé par mot de passe)",
        "metadata_encrypted_no": "Non",
        "metadata_reload": "📂 Recharger depuis le PDF",
        "metadata_reset": "Annuler les modifications",
        "metadata_reloaded": "Les métadonnées ont été rechargées depuis le PDF.",
        "metadata_reset_done": "Tous les champs de métadonnées ont été réinitialisés.",
        "metadata_no_file": "Aucun fichier PDF chargé.",
        "metadata_save_error": "Erreur lors de l'enregistrement des métadonnées",
        "metadata_saved": "Les métadonnées ont été enregistrées avec succès.",
        "metadata_pdf_version_unknown": "PDF (inconnu)",
        "metadata_saved_message": "Les métadonnées ont été enregistrées avec succès.",
        "metadata_saved_voice": "Métadonnées enregistrées.",

        "metadata_custom": "🔧 Métadonnées personnalisées",
        "metadata_custom_placeholder": "{\n  \"mon_champ\": \"ma_valeur\",\n  \"autre_champ\": 123\n}",
        "metadata_custom_tooltip": "Format JSON pour les métadonnées personnalisées (optionnel)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Modèle \"{0}\" sélectionné - Double-clic pour insérer",
        "text_use_template": "Utiliser un bloc de texte",
        "text_type": "Type",
        "text_search_templates": "Rechercher des blocs de texte...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informations d'exportation / d'importation",
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

        <h3>📦 Qu'est-ce qui est exporté ? (Aperçu)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Paramètres généraux de l'application</span></li>
            <li class="detail">• Mode sombre/clair</li>
            <li class="detail">• Inversion du mode sombre pour les images</li>
            <li class="detail">• Valeur seuil de gris</li>
            <li class="detail">• Langue</li>
            <li class="detail">• Géométrie de la fenêtre</li>
            <li class="detail">• Mode zoom</li>
            <li class="detail">• Navigation (Barre de navigation visible)</li>
            <li class="detail">• Sortie vocale (activée/désactivée)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Paramètres de sauvegarde</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nommage des fichiers (Horodatage, Séparateur, Suffixes)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Paramètres pour les insertions de</span></li>
            <li class="detail">• Signatures</li>
            <li class="detail">• Texte et blocs de texte</li>
            <li class="detail">• Croix, images et formes</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Paramètres OCR</span></li>
            <li class="detail">• Langue</li>
            <li class="detail">• Forcer l'OCR · Mode page</li>
            <li class="detail">• Prétraitement de l'image : Correction d'inclinaison, Nettoyage, Suréchantillonnage</li>
            <li class="detail">• Nombre de tâches parallèles</li>
            <li class="detail">• Mode d'inversion</li>
            <li class="detail">• Valeur seuil de gris</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Signets</span></li>
            <li class="detail">• Tous les signets par fichier PDF (Page, Nom, Heure de création)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Base de données de mots de passe</span></li>
            <li class="detail">• Mots de passe PDF enregistrés (optionnellement chiffrés ou en texte clair)</li>
            <li class="detail">• Hachage du mot de passe maître (si défini)</li>
            <li class="detail">• Données de vérification</li>
        </ul>

        <h4>⚠️ Remarques importantes</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Lors de l'importation :</strong>
            <ul>
                <li><span class="warning">➜ TOUS les paramètres actuels seront complètement écrasés</span></li>
                <li>• Un redémarrage de l'application est obligatoire</li>
                <li>• Les signatures, blocs de texte et signets existants seront remplacés</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Mot de passe maître et mode d'exportation :</strong>
            <ul>
                <li>• Lorsque le mot de passe maître est actif, vous pouvez choisir :</li>
                <li>  - <span style="color: #98FB98;"><strong>Déchiffré</strong></span> (les mots de passe sont en texte clair dans le ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Chiffré</strong></span> (lisibles uniquement avec le mot de passe maître sur le système cible)</li>
                <li>• Le hachage du mot de passe maître est <strong>toujours</strong> stocké chiffré</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Avis de sécurité :</strong>
            <ul>
                <li>• Le fichier ZIP exporté contient des données sensibles (<strong>mots de passe, signets, signatures</strong>)</li>
                <li>• Veuillez le conserver en sécurité (ex. clé USB chiffrée, gestionnaire de mots de passe)</li>
                <li>• En cas de perte du fichier, les mots de passe PDF enregistrés sont irrémédiablement perdus</li>
            </ul>
        </div>

        <h4>📁 Format d'exportation</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Les paramètres sont enregistrés dans un seul fichier ZIP :<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ce ZIP contient le fichier <code>settings.json</code> complet (de votre configuration) ainsi que d'éventuels fichiers d'image de signature intégrés et mots de passe chiffrés.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Signatures - Guide",
        'signature_guide_html': """
        📝 <strong>Signatures - Guide rapide</strong><br>
        <ul>
        <li>Définir un mot de passe maître</li>
        <li>Configurer les signatures dans le menu <em>Paramètres</em> (taille, horodatage, …)</li>
        <li>Insérer avec <strong>CLIC DROIT</strong> à la position souhaitée (mot de passe maître requis une fois par session)</li>
        <li>Déplacer la signature avec la souris ou les touches fléchées</li>
        <li>Insérer plusieurs signatures à la suite</li>
        <li>Personnaliser chaque signature individuellement</li>
        <li>Rejeter une signature individuelle</li>
        <li>Enregistrer / rejeter toutes les signatures en une fois</li>
        <li>Sinon, la barre de menu peut également être utilisée.</li>
        </ul>
        """,
        'signature_guide_voice': "Guide rapide pour les signatures. Définir le mot de passe maître. Configurer les signatures dans les paramètres. Insérer avec clic droit.",

        'image_guide_title': "Insérer des images - Guide",
        'image_guide_html': """
        📷 <strong>Insérer des images dans un PDF - Guide rapide</strong><br>
        <ol>
        <li>Clic droit à la position souhaitée</li>
        <li><em>„Insérer une image“</em> → Choisir l'image</li>
        <li>Positionner l'image: Glisser avec la souris</li>
        <li>Ajuster la taille: Glisser par les coins/bords</li>
        <li>Conserver le rapport hauteur/largeur: Touche <strong>[A]</strong></li>
        <li>Autres ajustements: Clic droit sur l'image</li>
        </ol>
        <p><strong>Astuce:</strong> Dans le menu contextuel, vous pouvez ajuster les paramètres.</p>
        """,
        'image_guide_voice': "Guide rapide pour les images. Clic droit, insérer une image, choisir. Positionner avec la souris, ajuster la taille aux coins. Rapport hauteur/largeur avec la touche A.",

        'form_guide_title': "Insérer des formes - Guide",
        'form_guide_html': """
        📐 <strong>Insérer des formes dans un PDF - Guide rapide</strong><br>
        <ol>
        <li>Choisir le type de forme (rectangle, ellipse, ligne, flèche)</li>
        <li>Cliquer sur la position:
            <ul>
            <li>Pour rectangle/ellipse: Un clic place la forme</li>
            <li>Pour ligne/flèche: Deux clics pour le point de départ et d'arrivée</li>
            </ul>
        </li>
        <li>Positionner la forme: Glisser avec la souris</li>
        <li>Ajuster la taille: Glisser par les coins/bords</li>
        <li>Enregistrer la forme: <strong>Entrée</strong></li>
        <li>Rejeter la forme: <strong>Échap</strong></li>
        <li>Autres ajustements: Clic droit sur la forme</li>
        </ol>
        <p><strong>Astuce:</strong> Dans le menu contextuel, vous pouvez ajuster les paramètres.</p>
        """,
        'form_guide_voice': "Guide rapide pour les formes. Choisir le type de forme. Pour rectangle ou ellipse, cliquer une fois, pour ligne ou flèche, deux fois. Positionner avec la souris, ajuster la taille aux coins. Enregistrer avec Entrée, rejeter avec Échap.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "précédent",
        "btn_next_result": "suivant",
        "ocr_text_window": "Fenêtre de texte OCR",
        "bookmark_existing": "Signets existants",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Comparaison OCR Mac - Windows",
        'ocr_method_mac_win_title': "Différences OCR entre Mac et Windows",
        'ocr_method_mac_win_voice': "Mac est meilleur",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Différences entre macOS et Windows</strong></p>

        <p><strong>macOS (recommandé)</strong></p>
        <p>Outil:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Résultat:</p>
        <ul>
        <li>Un PDF consultable avec texte intégré qui conserve en grande partie la mise en page originale.</li>
        </ul>
        <p>Avantages:</p>
        <ul>
        <li>Excellente qualité de reconnaissance de texte (même sur les pages inclinées).</li>
        <li>Conservation des graphiques vectoriels et des polices.</li>
        <li>Barre de progression GUI via l'évaluation du sous-processus.</li>
        <li>Contrôle total sur tous les paramètres OCR (Deskew, Clean, Oversample, optimisation).</li>
        <li>La recherche de texte est directement disponible dans la fenêtre principale (vue PDF).</li>
        </ul>
        <p>Inconvénients:</p>
        <ul>
        <li>Nécessite des outils système supplémentaires (ocrmypdf, Ghostscript, unpaper, pngquant – inclus dans le bundle de l'application).</li>
        <li>Gestion d'erreur plus complexe (blocages, dépassements de délai).</li>
        </ul>

        <p><strong>Windows (alternative stable)</strong></p>
        <p>Outil:</p>
        <ul>
        <li>pytesseract (liaison directe à Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Résultat:</p>
        <ul>
        <li>Un PDF consultable qui correspond visuellement à un PDF image, mais qui est consultable grâce au texte transparent.</li>
        </ul>
        <p>Avantages:</p>
        <ul>
        <li>Aucun ne me vient à l'esprit pour l'instant.</li>
        </ul>
        <p>Inconvénients:</p>
        <ul>
        <li>Le PDF est essentiellement une image avec du texte invisible ; la mise en page peut légèrement différer pour les documents complexes (colonnes, tableaux).</li>
        <li>Pas de correction automatique de l'inclinaison (--deskew) ni de nettoyage d'image (--clean).</li>
        <li>La barre de progression GUI est mise à jour uniquement de manière approximative en fonction du nombre de pages traitées.</li>
        <li>La vitesse OCR est légèrement plus lente (car chaque page est traitée individuellement).</li>
        <li>La recherche de texte est redirigée vers la fenêtre de texte OCR.</li>
        </ul>

        <p><strong>Points communs</strong></p>
        <ul>
        <li>Les deux méthodes créent un PDF consultable dans le même répertoire que le fichier source.</li>
        <li>Les paramètres OCR (langue, DPI, mode de segmentation de page, mode moteur OCR) peuvent être configurés via OCRSettingsDialog et s'appliquent aux deux implémentations.</li>
        </ul>

        <p><strong>Recommandation:</strong></p>
        <ul>
        <li>macOS: Le binaire ocrmypdf donne les meilleurs résultats – Achetez un Mac et utilisez la version (PDFDarkView pour Mac avec puce Apple Silicon ou Intel). Les résultats OCR sont meilleurs que sous Windows !</li>
        <li>Windows: Utilisez la solution pytesseract. Elle est stable et fournit une qualité tout à fait suffisante pour la plupart des documents.</li>
        </ul>

        <p><strong>Remarque importante:</strong></p>
        <ul>
        <li>Les deux versions sont entièrement intégrées à l'interface utilisateur – l'utilisateur ne remarque aucune différence.</li>
        <li>Le programme décide automatiquement quel moteur OCR utiliser en fonction du système d'exploitation.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Créer une signature (à partir d'un scan)",
        "signature_create_title": "Choisir une signature scannée (PDF/image)",
        "image_pdf_filter": "Images et PDF",
        "signature_pdf_empty": "Le PDF ne contient aucune page.",
        "signature_created_success": "Signature créée avec succès : {0}",
        "signature_create_error": "Erreur lors de la création de la signature :\n{0}",
        "rembg_missing": "rembg n'est pas installé.\nVeuillez installer : pip install rembg\nErreur : {0}",
        "signature_name_title": "Nom du fichier pour la signature",
        "signature_name_message": "Veuillez saisir un nom de fichier pour la nouvelle signature (sera enregistrée en PNG avec fond transparent) :",
        "signature_name_label": "Nom du fichier :",
        "signature_name_voice": "Saisir le nom du fichier pour la signature",
        "signature_processing": "Traitement en cours...",
        "signature_creation_title": "Création de la signature",
        "signature_overwrite_warning": "Le fichier '{0}' existe déjà. Écraser ?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Préparer le PDF pour la signature",
        "signature_prepare_instruction":"Veuillez sélectionner un PDF qui contient une signature scannée sur une seule page.\n\nPour une reconnaissance optimale, assurez-vous que :\n• La signature est écrite à l'encre noire (stylo à bille ou feutre fin) sur du papier blanc.\n• La signature se trouve dans le tiers supérieur d'une page A4 par ailleurs vierge.\n• Le PDF a été scanné avec au moins 300 dpi.\n• La signature est claire et pas trop fine.\n• Il n'y a pas de motifs de fond gênants ni de lignes.",
        "signature_prepare_voice":"Veuillez sélectionner un PDF avec une signature scannée. Veillez à une bonne qualité et au contraste.",
        "sig_thickness_label":"Épaisseur du trait :",
        "sig_thickness_normal":"Normale (fine)",
        "sig_thickness_bold":"Gras (recommandé)",
        "sig_thickness_very_bold":"Très gras",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Ajouter des langues GUI et OCR - Guide",
        'language_guide_title': "Ajouter des langues GUI et OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Téléchargez le fichier de traduction souhaité <code>translations_xy.py</code> depuis<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        et placez-le dans le répertoire suivant :</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Ouvrez votre navigateur Web.</li>
        <li>Allez à : <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Cherchez sur le bord droit de l'écran "Releases" et sélectionnez celui marqué <strong>"latest"</strong>.</li>
        <li>Sur la page de publication suivante, téléchargez le fichier <code>Source Code.zip</code> tout en bas.</li>
        <li>Décompressez le fichier ZIP.</li>
        <li>Recherchez dans le dossier décompressé tous les fichiers de langue dont vous avez besoin et copiez-les dans le répertoire :<br/>
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
        "menu_watermark":"Insérer un filigrane",
        "fullpage_text_watermark_title":"Texte comme filigrane",
        "fullpage_image_watermark_title":"Image comme filigrane",
        "filename_with_watermark":"_avec_filigrane",
        "watermark_text":"Texte :",
        "watermark_text_placeholder":"Votre texte de filigrane...",
        "watermark_font_family":"Police :",
        "watermark_font_size":"Taille de police :",
        "watermark_format":"Mise en forme :",
        "watermark_bold":"Gras",
        "watermark_italic":"Italique",
        "watermark_color":"Couleur :",
        "watermark_choose_color":"Choisir une couleur...",
        "watermark_opacity":"Opacité / Transparence :",
        "watermark_direction":"Sens de lecture :",
        "watermark_direction_l_r":"Gauche → Droite",
        "watermark_direction_bl_tr":"Bas gauche → Haut droit",
        "watermark_direction_tl_br":"Haut gauche → Bas",
        "watermark_direction_b_t":"Bas → Haut",
        "watermark_direction_t_b":"Haut → Bas",
        "watermark_preview":"Aperçu :",
        "watermark_preview_sample":"Exemple de texte",
        "watermark_empty_text":"Veuillez saisir un texte.",
        "watermark_applied":"Le filigrane a été appliqué à toutes les pages.",
        "watermark_saved":"Filigrane enregistré.",
        "image_scale":"Taille :",
        "image_preview":"Aperçu de l'image :",
        "no_image_selected":"Aucune image sélectionnée",
        "browse":"Parcourir...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Expurgations",
        "redact_add_black": "Expurgation (noir)",
        "redact_add_white": "Expurgation (blanc / effacer)",
        "redact_added_black": "Expurgation noire ajoutée",
        "redact_added_white": "Expurgation blanche ajoutée",
        "redact_apply_all": "Appliquer toutes les expurgations et enregistrer",
        "redact_discard_all": "Rejeter toutes les expurgations",
        "redact_discard": "Rejeter cette expurgation",
        "no_redactions": "Aucune expurgation",
        "redact_confirm_title": "Appliquer les expurgations de manière permanente",
        "redact_confirm_message": "Attention : Les zones marquées seront définitivement supprimées (noir ou blanc).\nUne sauvegarde sera créée (si activée).\n\nContinuer ?",
        "redact_apply": "Oui, expurger maintenant",
        "redact_saved": "{0} expurgation(s) appliquée(s) et enregistrée(s) avec succès.",
        "redact_saved_voice": "{0} expurgation(s) appliquée(s)",
        "redact_error": "Erreur lors de l'expurgation",
        "filename_redacted":"_expurgé",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Insérer des numéros de page',
        'page_numbers_format': 'Format de numéro :',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabe)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romain minuscule)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romain majuscule)',
        'page_numbers_format_letter': 'A, B, C ... (lettres)',
        'page_numbers_format_custom': 'Personnalisé',
        'page_numbers_custom_pattern': 'Modèle :',
        'page_numbers_custom_placeholder': 'ex. "Page {nummer}" ou "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Utilisez {nummer} pour le numéro de page actuel et {total} pour le nombre total',
        'page_numbers_position': 'Position :',
        'page_numbers_pos_tl': 'En haut à gauche',
        'page_numbers_pos_tc': 'En haut au centre',
        'page_numbers_pos_tr': 'En haut à droite',
        'page_numbers_pos_ml': 'Au milieu à gauche',
        'page_numbers_pos_mc': 'Centré',
        'page_numbers_pos_mr': 'Au milieu à droite',
        'page_numbers_pos_bl': 'En bas à gauche',
        'page_numbers_pos_bc': 'En bas au centre',
        'page_numbers_pos_br': 'En bas à droite',
        'page_numbers_margins': 'Marges :',
        'page_numbers_margin_x': 'Distance horizontale :',
        'page_numbers_margin_y': 'Distance verticale :',
        'page_numbers_range': 'Plage de pages :',
        'page_numbers_all_pages': 'Toutes les pages',
        'page_numbers_custom_range': 'Plage personnalisée',
        'page_numbers_from': 'De :',
        'page_numbers_to': 'À :',
        'page_numbers_progress': 'Insertion des numéros de page...',
        'page_numbers_start': 'Démarrage de l\'insertion des numéros de page...',
        'page_numbers_cancel': 'Insertion des numéros de page annulée',
        'page_numbers_success': 'Les numéros de page ont été ajoutés avec succès.\n\nSouhaitez-vous ouvrir le nouveau PDF ?\n\n{0}',
        'page_numbers_complete': 'Numéros de page ajoutés',
        'page_numbers_error_format': 'Erreur lors de l\'insertion des numéros de page : {0}',
        'page_numbers_content_type': 'Type de contenu :',
        'page_numbers_tab_simple': 'Numéro simple',
        'page_numbers_tab_range': 'Page X sur Y',
        'page_numbers_tab_date': 'Date',
        'page_numbers_tab_custom': 'Texte libre',
        'page_numbers_range_format': 'Format :',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Page {aktuell} sur {gesamt}',
        'page_numbers_range_custom': 'Personnalisé',
        'page_numbers_range_placeholder': 'ex. "Page {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format de date :',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1er janvier 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Personnalisé',
        'page_numbers_date_placeholder': 'ex. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Position :',
        'page_numbers_date_before': 'Date avant le numéro de page',
        'page_numbers_date_after': 'Date après le numéro de page',
        'page_numbers_date_only': 'Date uniquement (sans numéro de page)',
        'page_numbers_custom_text': 'Texte personnalisé :',
        'page_numbers_custom_placeholder_text': 'Utilisez {seite} pour le numéro de page et {gesamt} pour le total\nex. "Confidentiel - Page {seite}" ou "{seite} sur {gesamt}"',
        "filename_with_page_number":"_avec_numero_de_page",
        "filename_with_page_declaration":"_avec_indication_de_page",
        "filename_with_pagenumber":"_avec_numero_de_page",
        "filename_with_date":"_avec_date",
        "filename_with_my_page_declaration":"_avec_indication_personnalisee",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Modifications non enregistrées",
        "unsaved_changes_message_darkmode": "Des insertions non enregistrées existent.\nSouhaitez-vous les enregistrer avant de basculer ?",
        "save_and_switch": "Enregistrer et basculer",
        "discard_and_switch": "Basculer maintenant",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exporter les pages en tant qu\'images',
        'export_images_menu': 'Exporter en tant qu\'images (PNG/JPEG)',
        'export_images_format': 'Format d\'image :',
        'export_images_dpi': 'Résolution (DPI) :',
        'export_images_quality': 'Qualité JPEG :',
        'export_images_range': 'Plage de pages :',
        'export_images_all_pages': 'Toutes les pages',
        'export_images_custom_range': 'Plage personnalisée',
        'export_images_from': 'De :',
        'export_images_to': 'À :',
        'export_images_options': 'Options :',
        'export_images_single_files': 'Chaque page en tant que fichier séparé',
        'export_images_subfolder': 'Exporter dans un sous-dossier',
        'export_images_subfolder_info': 'Dans le sous-dossier "nomPDF_images"',
        'export_images_same_folder': 'Dans le même dossier que le PDF',
        'export_images_apply_darkmode': 'Appliquer les paramètres de PDFDarkView (Mode sombre)',
        'export_images_target_folder': 'Dossier cible :',
        'export_images_browse': 'Parcourir...',
        'export_images_preview': 'Aperçu :',
        'export_images_preview_info': 'Sélectionnez les paramètres d\'exportation',
        'export_images_preview_info_detail': '{0} pages en tant que {1}\nRésolution : {2} DPI\nNom du fichier : {3}\n{4}',
        'export_images_select_folder': 'Sélectionnez le dossier cible',
        'export_images_start': 'Démarrage de l\'exportation des images...',
        'export_images_progress': 'Exportation des images...',
        'export_images_saving': 'Enregistrement de la page {0} sur {1}...',
        'export_images_success': 'Exportation réussie !\n\n{0} images ont été enregistrées dans :\n{1}',
        'export_images_complete': 'Exportation des images terminée',
        'export_images_open_folder': '📁 Ouvrir le dossier',
        'export_images_cancel': 'Exportation des images annulée',
        'export_images_error_format': 'Erreur lors de l\'exportation des images : {0}',
        'export_images_pdf2image_missing': 'La bibliothèque "pdf2image" n\'est pas installée.\n\nVeuillez l\'installer avec :\npip install pdf2image\n\nPour Windows, vous avez également besoin de Poppler :\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Conversion PDF/A pour l\'archivage à long terme',
        'pdfa_menu': 'Conversion PDF/A (adapté à l\'archivage)',
        'pdfa_info': 'Convertit le PDF au format PDF/A.\n\nLe PDF/A est spécialement conçu pour l\'archivage à long terme et garantit que le document sera affiché correctement à l\'avenir.',
        'pdfa_standard': 'Norme PDF/A :',
        'pdfa_standard_select': 'Version :',
        'pdfa_1': 'PDF/A-1 (simple, largement compatible)',
        'pdfa_2': 'PDF/A-2 (moderne, meilleure compression)',
        'pdfa_3': 'PDF/A-3 (dernière version, permet les pièces jointes)',
        'pdfa_standards_explanation': '📖 Explication des normes :\n\n'
            '• PDF/A-1 : De base, compatible avec les anciens systèmes (env. 2005)\n'
            '• PDF/A-2 : Plus moderne, meilleure compression, prise en charge de la transparence (env. 2011)\n'
            '• PDF/A-3 : Dernière version, permet l\'intégration de pièces jointes (env. 2013)\n\n'
            'Recommandation : PDF/A-2 est un bon compromis entre compatibilité et fonctionnalités modernes.',
        'pdfa_options': 'Options :',
        'pdfa_compress_enable': 'Compresser le PDF (fichier plus petit)',
        'pdfa_metadata_preserve': 'Conserver les métadonnées (titre, auteur, etc.)',
        'pdfa_target_folder': 'Dossier cible :',
        'pdfa_browse': 'Parcourir...',
        'pdfa_select_folder': 'Sélectionnez le dossier cible',
        'pdfa_ocr_info_unknown': '🔍 Impossible de vérifier le contenu textuel.',
        'pdfa_ocr_info_not_needed': '✅ Texte disponible - l\'OCR n\'est pas nécessaire.\nLe PDF/A peut être créé directement.',
        'pdfa_ocr_info_recommended': '⚠️ Aucun texte suffisant trouvé.\n\nPour les PDF consultables, nous vous recommandons d\'exécuter d\'abord l\'OCR.\nRemarque : PDF/A fonctionne également sans OCR - mais le texte ne sera pas consultable.',
        'pdfa_ocr_info_error': '❌ Erreur lors de la vérification : {0}',
        'pdfa_start': 'Démarrage de la conversion PDF/A...',
        'pdfa_progress': 'Conversion PDF/A en cours...',
        'pdfa_success': 'Conversion PDF/A réussie !\n\nEnregistré sous :\n{0}\n\nSouhaitez-vous ouvrir le nouveau PDF ?',
        'pdfa_complete': 'Conversion PDF/A terminée',
        'pdfa_cancel': 'Conversion PDF/A annulée',
        'pdfa_error_format': 'Erreur lors de la conversion PDF/A :\n\n{0}',
        'pdfa_ocrmypdf_missing': 'La bibliothèque "ocrmypdf" n\'est pas installée.\n\nVeuillez l\'installer avec :\npip install ocrmypdf',
        'btn_convert': 'Convertir',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimiser le PDF (réduire la taille du fichier)',
        'optimize_menu': 'Optimiser le PDF (taille du fichier)',
        'optimize_info': 'Réduit la taille du fichier PDF grâce à différentes méthodes d\'optimisation.\n\nPlus le niveau de compression est élevé, plus le fichier est petit - avec une éventuelle perte de qualité des images.',
        'optimize_level': 'Niveau de compression :',
        'optimize_level_low': 'Faible (rapide, faible économie)',
        'optimize_level_medium': 'Moyen (bon compromis)',
        'optimize_level_high': 'Élevé (forte économie)',
        'optimize_level_maximum': 'Maximum (économie maximale, lent)',
        'optimize_level_explanation': 'Recommandation : "Moyen" est un bon compromis entre vitesse et taille de fichier.',
        'optimize_options': 'Options :',
        'optimize_compress_images': 'Compresser les images (réduire la qualité JPEG)',
        'optimize_clean_objects': 'Supprimer les objets inutilisés',
        'optimize_preserve_metadata': 'Conserver les métadonnées (titre, auteur, etc.)',
        'optimize_image_quality': 'Qualité d\'image :',
        'optimize_range': 'Plage de pages :',
        'optimize_all_pages': 'Toutes les pages',
        'optimize_custom_range': 'Plage personnalisée',
        'optimize_from': 'De :',
        'optimize_to': 'À :',
        'optimize_target_folder': 'Dossier cible :',
        'optimize_browse': 'Parcourir...',
        'optimize_select_folder': 'Sélectionnez le dossier cible',
        'optimize_info_box': 'Informations',
        'optimize_info_text': 'L\'optimisation peut prendre plusieurs minutes pour les grands PDF.\n\nLes images sont enregistrées avec une qualité réduite, ce qui peut réduire considérablement la taille du fichier.',
        'optimize_start': 'Démarrage de l\'optimisation PDF...',
        'optimize_progress': 'Optimisation du PDF...',
        'optimize_cancel': 'Optimisation PDF annulée',
        'optimize_complete': 'Optimisation PDF terminée',
        'optimize_error_format': 'Erreur lors de l\'optimisation PDF :\n\n{0}',
        'optimize_success_message': 'Optimisation PDF réussie !\n\nEnregistré sous :\n{0}\n\nAvant : {1}\nAprès : {2}\nÉconomie : {3:.1f}%\n\n{4}\n\nSouhaitez-vous ouvrir le PDF optimisé ?',
        'optimize_success_message_no_size': 'Optimisation PDF réussie !\n\nEnregistré sous :\n{0}\n\nInformations de taille non disponibles.\n\nSouhaitez-vous ouvrir le PDF optimisé ?',
        'optimize_result_positive': 'Le fichier a été réduit de {0:.1f}%.',
        'optimize_result_zero': 'Aucun changement de taille de fichier.',
        'optimize_result_negative': 'Le fichier a augmenté de {0:.1f}%.\nL\'optimisation a été ignorée, le fichier original a été conservé.',
        'btn_optimize': 'Démarrer l\'optimisation',
        'filename_optimize_low_suffix': '_optimise_faible',
        'filename_optimize_medium_suffix': '_optimise',
        'filename_optimize_high_suffix': '_optimise_eleve',
        'filename_optimize_maximum_suffix': '_optimise_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Rogner le PDF',
        'crop_menu': 'Rogner le PDF (Crop)',
        'crop_range': 'Appliquer à :',
        'crop_all_pages': 'Toutes les pages',
        'crop_current_page': 'Page actuelle uniquement',
        'crop_values': 'Valeurs de rognage (en points) :',
        'crop_left': 'Gauche :',
        'crop_right': 'Droite :',
        'crop_top': 'Haut :',
        'crop_bottom': 'Bas :',
        'crop_presets': 'Préréglages :',
        'crop_preset_white': 'Détecter les marges blanches',
        'crop_reset': 'Réinitialiser',
        'crop_mouse_hint': '🖱️ Faites glisser un rectangle pour sélectionner grossièrement la zone.\nVous pouvez ensuite ajuster les valeurs avec précision dans les SpinBoxes.\nUn ajustement manuel avec la souris n\'est pas possible.',
        'crop_apply': 'Rogner',
        'crop_scope_all': 'Toutes les pages',
        'crop_scope_current': 'Page actuelle',
        'crop_new_size': 'Nouvelle taille : {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Aucun PDF chargé',
        'crop_preview_error': 'Erreur lors du chargement de l\'aperçu',
        'crop_start': 'Démarrage du rognage...',
        'crop_progress': 'Rognage du PDF...',
        'crop_success': 'PDF rogné avec succès !\n\nEnregistré sous :\n{0}\n\nSouhaitez-vous ouvrir le PDF rogné ?',
        'crop_complete': 'Rognage terminé',
        'crop_cancel': 'Rognage annulé',
        'crop_error_format': 'Erreur lors du rognage :\n\n{0}',
        'filename_crop_suffix': '_rogne',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Aplatir le PDF (Flatten)',
        'flatten_menu': 'Aplatir le PDF (Flatten)',
        'flatten_info': 'Aplatir un PDF "grave" tous les éléments modifiables dans le contenu de la page.\n\nAprès cela, les champs de formulaire, les annotations, les textes, les croix, les signatures, les images et les formes ne sont plus modifiables individuellement.',
        'flatten_explanation_title': '📖 À quoi cela sert-il ?',
        'flatten_explanation_text': 'L\'aplatissement est nécessaire dans les situations suivantes :\n\n'
            '• 📄 Vous souhaitez préparer le document pour l\'impression\n'
            '• 🔒 Vous souhaitez empêcher la modification des champs de formulaire\n'
            '• 📎 Vous souhaitez "intégrer" définitivement les annotations et les commentaires dans le document\n'
            '• 🖼️ Vous souhaitez ancrer définitivement les textes, croix, signatures, images et formes dans le document\n'
            '• 📦 Vous souhaitez préparer le fichier pour l\'archivage\n\n'
            'L\'aplatissement rend le PDF plus petit et empêche le déplacement ou la suppression accidentelle des éléments.',
        'flatten_what_title': 'Qu\'est-ce qui est aplati ?',
        'flatten_what_list': '• ✅ Champs de formulaire (champs de texte, cases à cocher, boutons)\n'
            '• ✅ Annotations (commentaires, surlignages, notes)\n'
            '• ✅ Superpositions (textes, croix, signatures, images, formes)',
        'flatten_options': 'Options :',
        'flatten_forms': 'Aplatir les champs de formulaire',
        'flatten_annotations': 'Aplatir les annotations',
        'flatten_overlays': 'Aplatir les superpositions (textes, croix, signatures, images, formes)',
        'flatten_target_folder': 'Dossier cible :',
        'flatten_browse': 'Parcourir...',
        'flatten_select_folder': 'Sélectionnez le dossier cible',
        'flatten_warning': '⚠️ Important : L\'aplatissement est un processus irréversible !\n\nAprès l\'aplatissement, les éléments modifiables ne peuvent plus être modifiés ou supprimés individuellement.\nCréez une sauvegarde au préalable si nécessaire.',
        'flatten_apply': 'Aplatir',
        'flatten_start': 'Démarrage de l\'aplatissement...',
        'flatten_progress': 'Aplatissement du PDF...',
        'flatten_success': 'PDF aplati avec succès !\n\nEnregistré sous :\n{0}\n\nSouhaitez-vous ouvrir le PDF aplati ?',
        'flatten_complete': 'Aplatissement terminé',
        'flatten_cancel': 'Aplatissement annulé',
        'flatten_error_format': 'Erreur lors de l\'aplatissement :\n\n{0}',
        'filename_flatten_suffix': '_aplati',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Superposition de PDF (Overlay)',
        'overlay_menu': 'Superposition de PDF (Overlay)',
        'overlay_info': 'Place un PDF (superposition) sur un autre PDF.\n\nLe PDF de superposition est placé sur le PDF de base. Cela est utile pour les filigranes, les logos, les en-têtes ou les cachets.',
        'overlay_explanation_title': '📖 À quoi cela sert-il ?',
        'overlay_explanation_text': 'La superposition est nécessaire dans les situations suivantes :\n\n'
            '• 🏢 Placer un logo d\'entreprise comme filigrane sur chaque page\n'
            '• 📄 Placer un en-tête sur un PDF vierge\n'
            '• 🖊️ Placer une superposition de cachet sur un document\n'
            '• 🔖 Placer un filigrane sur toutes les pages\n'
            '• 📑 Placer une superposition de formulaire sur un modèle',
        'overlay_type': 'Type de superposition :',
        'overlay_type_fullpage': 'Page entière (couvrante)',
        'overlay_type_transparent': 'Page entière (transparent - recommandé)',
        'overlay_type_stamp': 'Cachet (positionnable)',
        'overlay_type_info_fullpage': '📄 Le PDF de superposition est placé exactement sur toute la page.\nL\'arrière-plan blanc peut être supprimé pour que seul le contenu reste visible.',
        'overlay_type_info_transparent': '🔍 Le PDF de superposition est placé sur toute la page avec un arrière-plan transparent.\nL\'arrière-plan blanc est automatiquement supprimé - idéal pour les filigranes et les logos !',
        'overlay_type_info_stamp': '🖊️ Le PDF de superposition est positionné et mis à l\'échelle comme un cachet.\nParfait pour les logos, les cachets ou les signatures à des positions spécifiques.',
        'overlay_remove_background': 'Supprimer l\'arrière-plan blanc :',
        'overlay_remove_background_enable': 'Supprimer l\'arrière-plan blanc du PDF de superposition (rend la superposition transparente)',
        'overlay_remove_background_tooltip': 'Supprime les zones blanches du PDF de superposition afin que le texte sous-jacent devienne visible.',
        'overlay_threshold': 'Valeur seuil :',
        'overlay_threshold_hint': '(1-254, plus élevé = plus de blanc est supprimé)',
        'overlay_select_file': 'Sélectionner le PDF de superposition :',
        'overlay_file_placeholder': 'Veuillez sélectionner un fichier PDF pour la superposition',
        'overlay_browse': 'Parcourir...',
        'overlay_select_overlay': 'Sélectionner le PDF de superposition',
        'overlay_range': 'Plage de pages :',
        'overlay_all_pages': 'Toutes les pages',
        'overlay_custom_range': 'Plage personnalisée',
        'overlay_from': 'De :',
        'overlay_to': 'À :',
        'overlay_position': 'Position :',
        'overlay_position_center': 'Centre',
        'overlay_position_top_left': 'En haut à gauche',
        'overlay_position_top_right': 'En haut à droite',
        'overlay_position_bottom_left': 'En bas à gauche',
        'overlay_position_bottom_right': 'En bas à droite',
        'overlay_size': 'Taille :',
        'overlay_size_original': 'Taille originale',
        'overlay_size_fit_page': 'Ajuster à la page',
        'overlay_size_custom': 'Personnalisé (%)',
        'overlay_opacity': 'Transparence :',
        'overlay_target_folder': 'Dossier cible :',
        'overlay_browse_folder': 'Parcourir...',
        'overlay_select_folder': 'Sélectionnez le dossier cible',
        'overlay_warning': '⚠️ Remarque : Le PDF de superposition est placé sur le PDF de base et y est "gravé".\n\nLes éléments du PDF de superposition ne peuvent plus être modifiés individuellement après l\'enregistrement.',
        'overlay_apply': 'Superposer',
        'overlay_start': 'Démarrage de la superposition...',
        'overlay_progress': 'Superposition du PDF...',
        'overlay_success': 'PDF superposé avec succès !\n\nEnregistré sous :\n{0}\n\nSouhaitez-vous ouvrir le PDF superposé ?',
        'overlay_complete': 'Superposition terminée',
        'overlay_cancel': 'Superposition annulée',
        'overlay_error_format': 'Erreur lors de la superposition :\n\n{0}',
        'overlay_no_file': 'Aucun PDF de superposition sélectionné.\n\nVeuillez sélectionner un fichier PDF à superposer.',
        'filename_overlay_suffix': '_superpose',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extraire les images du PDF',
        'extract_images_menu': 'Extraire toutes les images',
        'extract_images_info': 'Extrait toutes les images du PDF et les enregistre en tant que fichiers séparés.\n\nLes images sont enregistrées dans leur format d\'origine ou converties dans un format sélectionné.',
        'extract_images_format': 'Format d\'image :',
        'extract_images_quality': 'Qualité JPEG :',
        'extract_images_options': 'Options :',
        'extract_images_subfolder': 'Extraire dans un sous-dossier ("nomPDF_images")',
        'extract_images_unique': 'Images uniques uniquement (éviter les doublons)',
        'extract_images_range': 'Plage de pages :',
        'extract_images_all_pages': 'Toutes les pages',
        'extract_images_custom_range': 'Plage personnalisée',
        'extract_images_from': 'De :',
        'extract_images_to': 'À :',
        'extract_images_target_folder': 'Dossier cible :',
        'extract_images_browse': 'Parcourir...',
        'extract_images_select_folder': 'Sélectionnez le dossier cible',
        'extract_images_info_box': 'Informations',
        'extract_images_info_text': 'L\'extraction peut prendre plusieurs minutes pour les grands PDF.\n\nLes images sont enregistrées avec leur nom d\'origine (page_image).',
        'extract_images_extract': 'Extraire',
        'extract_images_start': 'Démarrage de l\'extraction...',
        'extract_images_progress': 'Extraction des images...',
        'extract_images_success': '✅ Images extraites avec succès !\n\n{0} images ont été enregistrées dans :\n{1}',
        'extract_images_complete': 'Extraction des images terminée',
        'extract_images_cancel': 'Extraction annulée',
        'extract_images_error_format': 'Erreur lors de l\'extraction des images :\n\n{0}',
        'extract_images_open_folder': '📁 Ouvrir le dossier',
        'extract_images_no_images': 'Aucune image trouvée dans le PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Plusieurs pages sur une page (N-Up)',
        'nup_menu': 'Plusieurs pages sur une page (N-Up)',
        'nup_info': 'Organise plusieurs pages PDF sur une seule page.\n\nIdéal pour les impressions compactes, les aperçus ou les polycopiés.',
        'nup_layout': 'Disposition :',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Aperçu :',
        'nup_preview_info': '{0} pages → {1} pages par feuille → {2} feuilles\nDisposition : {3}',
        'nup_order': 'Ordre :',
        'nup_order_horizontal': 'Horizontal (ligne par ligne)',
        'nup_order_vertical': 'Vertical (colonne par colonne)',
        'nup_order_horizontal_reverse': 'Horizontal inversé',
        'nup_order_vertical_reverse': 'Vertical inversé',
        'nup_range': 'Plage de pages :',
        'nup_all_pages': 'Toutes les pages',
        'nup_custom_range': 'Plage personnalisée',
        'nup_from': 'De :',
        'nup_to': 'À :',
        'nup_options': 'Options :',
        'nup_margins': 'Marges :',
        'nup_margin_between': 'Espacement entre les pages :',
        'nup_page_numbers': 'Insérer des numéros de page',
        'nup_target_folder': 'Dossier cible :',
        'nup_browse': 'Parcourir...',
        'nup_select_folder': 'Sélectionnez le dossier cible',
        'nup_create': 'Créer',
        'nup_start': 'Démarrage de N-Up...',
        'nup_progress': 'Création de N-Up...',
        'nup_success': 'N-Up créé avec succès !\n\nEnregistré sous :\n{0}\n\nSouhaitez-vous ouvrir le nouveau PDF ?',
        'nup_complete': 'N-Up terminé',
        'nup_cancel': 'N-Up annulé',
        'nup_error_format': 'Erreur lors de N-Up :\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Modifier la taille de la page',
        'pagesize_menu': 'Modifier la taille de la page',
        'pagesize_info': 'Modifie la taille de page du PDF.\n\nLe contenu est automatiquement adapté à la nouvelle taille.',
        'pagesize_format': 'Format :',
        'pagesize_select': 'Sélectionnez un format standard :',
        'pagesize_custom': 'Taille personnalisée :',
        'pagesize_width': 'Largeur :',
        'pagesize_height': 'Hauteur :',
        'pagesize_orientation': 'Orientation :',
        'pagesize_portrait': 'Portrait',
        'pagesize_landscape': 'Paysage',
        'pagesize_scale_options': 'Options de mise à l\'échelle :',
        'pagesize_fit': 'Ajuster (conserver le rapport d\'aspect)',
        'pagesize_stretch': 'Étirer (déformer)',
        'pagesize_center': 'Centrer (taille originale)',
        'pagesize_range': 'Plage de pages :',
        'pagesize_all_pages': 'Toutes les pages',
        'pagesize_custom_range': 'Plage personnalisée',
        'pagesize_from': 'De :',
        'pagesize_to': 'À :',
        'pagesize_target_folder': 'Dossier cible :',
        'pagesize_browse': 'Parcourir...',
        'pagesize_select_folder': 'Sélectionnez le dossier cible',
        'pagesize_apply': 'Appliquer',
        'pagesize_start': 'Démarrage du changement de taille de page...',
        'pagesize_progress': 'Changement de taille de page...',
        'pagesize_success': 'Taille de page modifiée avec succès !\n\nEnregistré sous :\n{0}\n\nSouhaitez-vous ouvrir le nouveau PDF ?',
        'pagesize_complete': 'Changement de taille de page terminé',
        'pagesize_cancel': 'Changement de taille de page annulé',
        'pagesize_error_format': 'Erreur lors du changement de taille de page :\n\n{0}',
        'pagesize_preview_info': 'Nouvelle taille : {0} x {1} pt',
        'filename_pagesize_suffix': '_nouvelle_taille',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informations sur le PDF',
        'pdf_info_menu': 'Afficher les informations du PDF',
        'pdf_info_voice': 'Affichage des informations du PDF',
        'pdf_info_error': 'Erreur lors de l\'affichage des informations du PDF :\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Afficher les raccourcis clavier",
        "shortcuts_dialog_title": "Raccourcis clavier",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FICHIER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Ouvrir un PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Fermer le PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Enregistrer sous...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Protéger le document</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Imprimer</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Imprimer immédiatement (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Quitter l'application</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORTER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exporter en tant que Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exporter en tant que DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exporter en tant que TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exporter en tant qu'images (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extraire les images</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ TRAITEMENT DES DOCUMENTS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Pages multiples)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Conversion PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Aplatir le PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Superposer le PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimiser le PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ MODIFIER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Rechercher</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Ajouter un signet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Gérer les signets</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Signet suivant</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Signet précédent</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Exécuter l'OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 GESTION DES PAGES</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Faire pivoter la page actuelle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Faire pivoter toutes les pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normaliser la page actuelle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normaliser toutes les pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Supprimer des pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extraire des pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Insérer des pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Déplacer des pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Fusionner des PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Modifier la taille de la page</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INSÉRER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Insérer du texte</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Insérer une croix</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Insérer la signature 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Insérer la signature 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Insérer une image</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Insérer un rectangle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Insérer une ellipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Insérer une ligne</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Insérer une flèche</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Insérer des numéros de page</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Filigrane texte</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Filigrane image</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ EXPURGATIONS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Expurgation (noir)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Expurgation (blanc)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Appliquer toutes les expurgations</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANCÉ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Rogner le PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Modifier les métadonnées</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ AFFICHAGE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Basculer en mode Sombre/Clair</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Afficher la fenêtre de texte</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Largeur de la page (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Deux pages (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Aperçu (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PARAMÈTRES</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Gestion des mots de passe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Paramètres OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Paramètres de signature</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatage des noms de fichiers</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exporter les paramètres</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importer les paramètres</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMATIONS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Afficher les informations du PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Activer/désactiver la sortie vocale</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Focus sur la barre de menus</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nouvelle version disponible",
        "update_available_message": "Une nouvelle version <b>{0}</b> est disponible.\n\nVisitez la page de version pour télécharger la mise à jour :\n{1}",
        "update_available_voice": "Nouvelle version {0} disponible. Veuillez télécharger la mise à jour depuis la page GitHub.",
        "update_open_release": "Ouvrir la page de version",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Télécharger toutes les traductions",
        "ask_download_all_translations": """En plus de l'allemand, l'anglais et le vietnamien, {total_languages} autres langues d'interface sont disponibles.\n\nFaut-il les fournir / mettre à jour ?\n\nRemarque :\nLes langues inutiles peuvent être supprimées manuellement plus tard dans le répertoire :\n{translations_path}
        \nSi vous annulez, vous pouvez télécharger les langues d'interface plus tard via le menu 'Outils → Mettre à jour les traductions'.""",
        "menu_update_translations": "Mettre à jour les traductions",
        "translations_updated": "Traductions mises à jour",
        "translations_update_success": "{} traductions ont été mises à jour avec succès ({} nouvelles, {} mises à jour).",
        "translations_update_error": "Erreur lors de la mise à jour des traductions",
        "translations_update_no_changes": "Toutes les traductions sont déjà à jour.",
        "translations_update_offline": "Pas de connexion Internet. Les traductions n'ont pas pu être mises à jour.",
        "translations_update_in_progress": "Les traductions sont mises à jour en arrière-plan...",
        "translations_downloading": "Téléchargement des traductions...",
        "translations_path_hint": "Répertoire utilisateur pour les traductions",
        "translations_update_not_available_title": "Mise à jour non disponible",
        "translations_update_not_available_message": """La mise à jour des traductions n'est disponible que dans la version installée.\n\nEn mode développement, les traductions sont déjà à jour.""",
        "translations_update_no_internet_title": "Pas de connexion Internet",
        "translations_update_no_internet_message": """Impossible d'établir une connexion Internet.\n\nLes traductions ne peuvent pas être téléchargées depuis GitHub.\n\nSolutions possibles :
        • Vérifiez votre connexion Internet
        • Désactivez temporairement tout pare-feu
        • Réessayez plus tard
        \nVous pouvez également télécharger les traductions manuellement depuis GitHub :
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "La mise à jour est déjà en cours",
        "btn_retry": "Réessayer",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Bienvenue dans PDF Dark View",
        "welcome_title_not_supported": "Bienvenue dans PDF Dark View",
        "welcome_message": "Bienvenue dans PDF Dark View !\n\nVotre langue système a été détectée comme '{language}'.\nSouhaitez-vous utiliser cette langue pour l'interface utilisateur ?\n\nVous pouvez changer la langue à tout moment via 'Paramètres → Langue'.",
        "welcome_message_language_not_available": "Bienvenue dans PDF Dark View !\n\nVotre langue système a été détectée comme '{language}'.\nCette langue n'est pas encore installée.\n\nSouhaitez-vous télécharger maintenant les traductions pour {language} depuis GitHub ?\n\n(La langue sera alors automatiquement utilisée pour l'interface utilisateur.)",
        "welcome_message_language_not_supported": "Bienvenue dans PDF Dark View !\n\nVotre langue système a été détectée comme '{language}'.\nMalheureusement, il n'y a pas encore de traductions pour cette langue.\n\nL'interface utilisateur sera affichée en {fallback_language}.\n\nVous pouvez changer la langue à tout moment via 'Paramètres → Langue'.\nSi vous le souhaitez, vous pouvez également contribuer à une traduction pour votre langue :\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Oui, utiliser la langue système",
        "welcome_keep_english": "Non, garder l'anglais",
        "welcome_download_language": "Oui, télécharger {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Le programme se ferme",

    }

