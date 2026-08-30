
# ============================================
# translations_tr.py - Türkçe sözlük
# Kategorilere göre tamamen sıralanmıştır
# Tutarlılık için yorumlar Almanca
# ============================================

def load_turkish_strings():
    """Tüm Türkçe dizeleri yükler"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF Aç",
        'btn_text_window': "OCR Metni",
        'btn_first': "İlk Sayfa",
        'btn_prev': "Önceki Sayfa",
        'btn_next': "Sonraki Sayfa",
        'btn_last': "Son Sayfa",
        'btn_print': "Yazdır",
        'btn_darkmode_light': "Açık Mod",
        'btn_darkmode_dark': "Koyu Mod",
        'btn_delete_pages': "Sayfaları Sil",
        'btn_extract_pages': "Sayfaları Çıkar",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "Tamam",
        'btn_cancel': "İptal",
        'btn_save': "Kaydet",
        'btn_close': "Kapat",
        'btn_delete': "Sil",
        'btn_delete_all': "Tümünü Sil",
        'btn_copy': "Kopyala",
        'btn_export': "Dışa Aktar",
        'btn_show': "Şifreyi Göster",
        'btn_hide': "Şifreyi Gizle",
        'btn_authenticate': "Kimlik Doğrula",
        'btn_settings': "Ayarlar",
        'btn_protect': "Koru",
        'btn_remove_password': "Şifreyi Kaldır",
        'btn_manage': "Şifre Yöneticisi",
        'btn_retry': "Yeniden Dene",
        'btn_select_all': "Tümünü Seç",
        'btn_clear_selection': "Seçimi Temizle",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Sayfa {0} / {1}",
        'page_count': "/ {0}",
        'goto_page': "Sayfaya Git",
        'page_simple': "Sayfa {0}",
        'full_view_page': "Tam görünüm sayfa {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Arama terimi girin + Enter",
        'search_results': "Sonuç: {0} / {1}",
        'search_nav_hint': "Enter: sonraki  (Shift+Enter: önceki) sonuç",
        'search_no_results': "Sonuç yok",
        'search_error': "Arama hatası",
        'search_active': "Arama alanı etkinleştirildi",
        'search_closed': "Arama kapatıldı",
        'search_position': "Sayfa {0} {1}",
        'search_pos_top': "en üst",
        'search_pos_upper': "üst",
        'search_pos_middle': "orta",
        'search_pos_lower': "alt",
        'search_pos_bottom': "en alt",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Metin tanıma başarıyla tamamlandı!",
        'ocr_success_title': "OCR başarılı",
        'ocr_success_message': "Belge artık aranabilir.",
        'ocr_failed': "OCR başarısız",
        'ocr_in_progress': "OCR devam ediyor",
        'ocr_preparing': "PDF hazırlanıyor...",
        'ocr_analyzing': "PDF analiz ediliyor...",
        'ocr_optimizing': "Görüntü iyileştirme sürüyor...",
        'ocr_recognizing': "Metin tanıma sürüyor...",
        'ocr_embedding': "Metin gömülüyor...",
        'ocr_finalizing': "PDF sonlandırılıyor...",
        'ocr_not_available': "OCR mevcut değil",
        'ocr_install_message': "OCR araçları bulunamadı.\n\nLütfen yükleyin:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR gerekli",
        'ocr_question': "PDF aranabilir metin içermiyor.\n{0} işlemini etkinleştirmek için OCR çalıştırılsın mı?",
        'ocr_perform': "OCR'ı Çalıştır",
        'ocr_later': "Daha Sonra",
        'ocr_starting': "Garantili OCR başlatılıyor...",
        'ocr_success_voice': "OCR başarılı. PDF artık aranabilir.",
        'ocr_partial_success': "OCR gerçekleştirildi, ancak değiştirme sırasında sorunlar oluştu.\n\nAranabilir sürüm şuraya kaydedildi:\n{0}\n\nHata: {1}",
        'ocr_partial_title': "OCR kısmen başarılı",
        'ocr_partial_voice': "OCR gerçekleştirildi, ancak değiştirme başarısız.",
        'original_file': "Orijinal dosya:",
        'old_size': "Eski dosya boyutu:    {0} bayt",
        'new_size': "Yeni dosya boyutu: {0} bayt",
        'size_change': "Değişim: {0}{1} bayt",
        'backup_created_file': "Yedek oluşturuldu:\n{0}",
        'backup_not_created': "Yedek: Oluşturulmadı (ayar devre dışı)",
        'page_header': "=== Sayfa {0} ===\n{1}\n",
        'scanned_page_header': "=== Sayfa {0} (taranmış) ===\n[Bu sayfa yalnızca taranmış metin içerir]\n[Lütfen OCR'ı elle çalıştırın]\n",
        'scanned_warning': "⚠️ TARANMIŞ METİN - OCR GEREKLİ",
        'guaranteed_title': "Aranabilir PDF oluşturuldu",
        'guaranteed_message': "<b>Garantili aranabilir sürüm oluşturuldu!</b>\n\nOtomatik OCR başarısız olduğu için alternatif bir aranabilir PDF oluşturuldu:\n\n{0}\n\n<b>Bu dosya şunları içerir:</b>\n• Çıkarılmış metin (varsa)\n• Taranmış sayfalar için ipuçları\n• Tamamen aranabilir",
        'guaranteed_voice': "Garantili aranabilir PDF oluşturuldu.",
        'instruction_title': "OCR TALİMATI",
        'instruction_file': "Orijinal dosya: {0}",
        'instruction_text': "Otomatik metin tanıma (OCR) başarısız oldu.\nLütfen OCR'ı elle gerçekleştirin:\n\n1. OCRmyPDF İLE (komut satırı):\n   ocrmypdf --force-ocr \"[DOSYA]\" \"çıktı.pdf\"\n\n2. ADOBE ACROBAT İLE (macOS/Windows):\n   • PDF'yi Acrobat'ta açın\n   • Araçlar > PDF Düzenle\n   • 'Metin Tanıma'yı seçin\n\n3. ÖN İZLEME İLE (macOS):\n   • PDF'yi Önizleme'de açın\n   • Dosya > Dışa Aktar...\n   • Quartz Filtresi: 'Dosya Boyutunu Küçült'\n   • 'OCR Gerçekleştir'i etkinleştirin\n\n4. ÇEVRİMİÇİ OCR HİZMETLERİ:\n   • smallpdf.com/tr/ocr-pdf\n   • ilovepdf.com/tr/ocr-pdf\n   • adobe.com/tr/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR talimatı oluşturuldu",
        'instruction_created_message': "Ayrıntılı bir talimat oluşturuldu:\n\n{0}\n\nElle OCR için adımları izleyin.",
        'instruction_created_voice': "OCR talimatı oluşturuldu.",
        'ocr_impossible': "OCR mümkün değil",
        'ocr_impossible_message': "OCR gerçekleştirilemedi.\n\n'{0}' dosyasını OCR yazılımıyla elle işleyin.",
        'ocr_impossible_voice': "OCR mümkün değil. Lütfen elle işleyin.",
        'emergency_title': "Acil OCR",
        'emergency_message': "Bir acil durum PDF'si oluşturuldu:\n\n{0}\n\nBu dosyayı elle OCR ile işleyin.",
        'emergency_voice': "Acil durum PDF'si oluşturuldu. Lütfen elle OCR çalıştırın.",
        'critical_error': "Kritik hata",
        'critical_error_message': "OCR başlatılamadı.\n\nProgramı yeniden başlatın ve\nOCR kurulumunu kontrol edin.",
        'critical_error_voice': "Kritik OCR hatası",
        'ocr_question_html': "<p>PDF aranabilir metin içermiyor.<p>{0} işlemini etkinleştirmek için OCR çalıştırılsın mı?</p>",
        'ocr_question_voice': "OCR gerekli. PDF aranabilir metin içermiyor. {0} işlemini etkinleştirmek için OCR çalıştırılsın mı?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "PDF yüklenmemiş",
        'no_pdf_message': "Hiç PDF yüklenmemiş",
        'pdf_not_found': "PDF dosyası bulunamadı",
        'file_size': "Dosya boyutu",
        'bytes': "bayt",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Yedek oluşturuldu",
        'backup_disabled': "Yedek devre dışı",
        'backup_activated': "Yedek oluşturma etkinleştirildi",
        'backup_deactivated': "Yedek oluşturma devre dışı bırakıldı",
        'backup_status': "Yedek: {0}",
        'backup_on': "✔ etkin",
        'backup_off': "✘ devre dışı",
        'close_pdf': "PDF kapatılıyor: {0}",
        'pdf_not_found_format': "PDF dosyası bulunamadı: {0}",
        'error_pdf_load_format': "PDF yüklenirken hata: {0}",
        'load_failed_format': "Yükleme başarısız:\n{0}",
        'decrypted_suffix': "(şifresi çözüldü)",
        'decryption_failed': "Şifre çözme başarısız.",
        'decryption_error': "Şifre çözme hatası",
        'decryption_success': "Şifre başarıyla çözüldü",
        'decryption_success_message': "PDF'nin şifresi çözüldü ve şuraya kaydedildi:\n\n{0}",
        'decryption_success_voice': "PDF'nin şifresi çözüldü ve kaydedildi.",
        'password_remove_error': "Şifre kaldırılırken hata",
        'save_unencrypted': "Şifrelenmemiş PDF'yi farklı kaydet",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Farklı kaydet...",
        'save_copy': "Kopyasını kaydet",
        'save_success': "PDF şuraya kaydedildi: {0}",
        'save_encrypted': "Korumalı PDF şuraya kaydedildi: {0}",
        'save_error': "PDF kaydedilemedi",
        'encryption_question': "PDF bir şifreyle korunsun mu?",
        'encryption_yes': "Evet",
        'encryption_no': "Hayır",
        'encryption_cancel': "İptal",
        'save_cancel': "Kaydetme iptal edildi",
        'save_encrypted_voice': "Dosya şifrelendi ve kaydedildi.",
        'save_success_voice': "PDF dosyası şifrelenmemiş olarak kaydedildi.",
        'save_error_format': "PDF kaydedilemedi:\n{0}",
        'export_pages_success': "Pages'e dışa aktarma başarılı",
        'export_pages_error': "Pages'e dışa aktarma başarısız",
        'export_pages_error_format': "Pages'e dışa aktarma başarısız: {0}",
        'export_word_success': "Word'e dışa aktarma başarılı",
        'export_word_error': "Word'e dışa aktarma başarısız",
        'export_word_error_format': "Word'e dışa aktarma başarısız: {0}",
        'export_text_success': "Metin olarak dışa aktarma başarılı",
        'export_text_error': "Metin olarak dışa aktarma başarısız",
        'export_text_error_format': "Metin olarak dışa aktarma başarısız: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Şifre gerekli",
        'password_enter': "Lütfen şifreyi girin",
        'password_confirm': "Şifreyi onayla",
        'password_new': "Yeni şifre",
        'password_current': "Mevcut şifre",
        'password_save': "Şifreyi kaydet (şifrelenmiş)",
        'password_saved': "✓ Bu dosya için şifre kaydedildi",
        'password_wrong': "Yanlış şifre",
        'password_mismatch': "Şifreler eşleşmiyor",
        'password_too_short': "Şifre çok kısa",
        'password_min_length': "Şifre en az 4 karakter olmalıdır",
        'password_strength': "Şifre gücü",
        'password_strength_very_weak': "Çok zayıf",
        'password_strength_weak': "Zayıf",
        'password_strength_medium': "Orta",
        'password_strength_strong': "Güçlü",
        'password_strength_very_strong': "Çok güçlü",
        'password_char_count': "({0} karakter)",
        'password_match': "✓ Eşleşiyor",
        'password_no_match': "✗ Şifreler eşleşmiyor",
        'password_show': "Göster",
        'password_hide': "Gizle",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Şifre Yöneticisi",
        'password_table_filename': "Dosya adı",
        'password_table_password': "Şifre",
        'password_count': "{0} kayıtlı şifre",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Kayıtlı şifre yok",
        'password_copied': "{0} şifre kopyalandı",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "'{0}' için şifre gerçekten silinsin mi?",
        'password_delete_multiple': "Seçili {0} şifre gerçekten silinsin mi?",
        'password_delete_all_confirm': "Kayıtlı {0} şifrenin tamamı gerçekten silinsin mi?",
        'password_deleted': "{0} şifre silindi",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Tüm şifreler silindi",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Şifre Oluşturucu",
        'generator_generated': "Oluşturulan şifre:",
        'generator_regenerate': "Yeniden oluştur",
        'generator_copy': "Kopyala",
        'generator_use': "Kullan",
        'generator_settings': "Ayarlar",
        'generator_length': "Uzunluk:",
        'generator_group_every': "Her",
        'generator_group_chars': "karakterde bir ayraç.   Ayraç:",
        'generator_uppercase': "Büyük harf (A-Z)",
        'generator_lowercase': "Küçük harf (a-z)",
        'generator_digits': "Rakam (0-9)",
        'generator_symbols': "Sembol (!@#$%^&*)",
        'generator_exclude': "Hariç tutulanlar:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Ana şifre gerekli",
        'master_password_setup': "Ana şifre oluştur",
        'master_password_change': "Ana şifreyi değiştir",
        'master_password_enter': "Lütfen ana şifrenizi girin",
        'master_password_choose': "Güçlü bir ana şifre seçin (en az 8 karakter)",
        'master_password_new': "Lütfen yeni ana şifrenizi girin",
        'master_password_confirm': "Şifreyi onayla",
        'master_password_authenticate': "Kimlik doğrula",
        'master_password_success': "Ana şifre başarıyla oluşturuldu.",
        'master_password_changed': "Ana şifre başarıyla değiştirildi.",
        'master_password_removed': "Ana şifre ve tüm şifreler silindi.",
        'master_password_remove': "Ana şifreyi kaldır",
        'master_password_remove_confirm': "TÜM şifreleri silmek istediğinizden EMİN MİSİNİZ?\n\nBu işlem GERİ ALINAMAZ!",
        'master_password_export_before': "Önce bir yedek kopya dışa aktarılsın mı?",
        'master_password_export_delete': "Dışa aktar ve sil",
        'master_password_delete_now': "Hemen sil",
        'master_password_for_signatures': "İmzaları kullanabilmek için bir ana şifre oluşturmalısınız.\n\nŞimdi bir ana şifre oluşturulsun mu?",
        'master_password_for_private': "Özel metin bloklarını kullanabilmek için bir ana şifre oluşturmalısınız.\n\nŞimdi bir ana şifre oluşturulsun mu?",
        'master_password_info': """
            <b>🔐 ANA ŞİFRE OLMADAN:</b><br>
            • Şifreleri görüntüleme, kopyalama ve dışa aktarma mümkün değil<br>
            • Şifre silme her zaman mümkündür (ana şifre olmadan da)<br><br>

            <b>🔐 ANA ŞİFRE İLE:</b><br>
            • Kimlik doğrulama sonrası tüm işlevler kullanılabilir<br>
            • Şifreler ana şifre ile şifrelenir<br>
            • Minimum uzunluk: 8 karakter<br>
            • Güvenli SHA-256 hash depolama<br><br>

            <b>ÖNEMLİ:</b><br>
            • Ana şifre kaybolursa: şifreler kurtarılamaz<br>
            • Ana şifre kaldırıldığında: TÜM şifreler silinir<br>
            • Silme öncesi dışa aktarma seçeneği mevcut<br>
            • Ana şifre her zaman değiştirilebilir
        """,
        'signature_auth_disabled': "İmzalar için şifre sorgusunu devre dışı bırak",
        'template_auth_disabled': "Özel metin blokları için şifre sorgusunu devre dışı bırak",
        'master_password_for_signatures_settings': "İmzaları kullanabilmek için bir ana şifre oluşturmalısınız.\n\nBunun için Ayarlar - Şifre Yöneticisi'ne gidin",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF'yi koru",
        'protect_info': "'{0}' dosyası bir şifre ile korunacak.",
        'protect_instruction': "Belgeyi korumak için istediğiniz şifreyi iki kez girin veya giriş alanının sağındaki şifre oluşturucuyu kullanın.",
        'protect_success': "PDF başarıyla korundu ve şuraya kaydedildi:\n{0}\n\nŞifre: {1}\n\nKorumalı PDF şimdi açılsın mı?",
        'protect_open': "Evet",
        'protect_skip': "Hayır",
        'protect_error': "PDF korunurken hata",
        'protect_open_title': "korumalı PDF aç",
        'protect_question': "Tamamlandı. Korumalı PDF şimdi açılsın mı? Evet mi Hayır mı?",
        'password_cancel': "Şifre diyaloğu iptal edildi",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Sayfaları sil",
        'pages_extract': "Sayfaları çıkar",
        'pages_insert': "Sayfa ekle",
        'pages_move': "Sayfaları taşı",
        'pages_delete_options': "Silme seçenekleri",
        'pages_delete_empty': "Tüm boş sayfaları sil",
        'pages_delete_current': "Geçerli sayfayı sil",
        'pages_delete_range': "Sayfa aralığını sil",
        'pages_extract_options': "Çıkarma seçenekleri",
        'pages_extract_current': "Geçerli sayfayı çıkar",
        'pages_extract_range': "Sayfa aralığını çıkar",
        'pages_insert_position': "Ekleme konumu",
        'pages_insert_before': "Şu sayfadan önce ekle:",
        'pages_insert_select': "PDF seç",
        'pages_insert_none': "PDF seçilmedi",
        'pages_move_source': "Taşınacak sayfalar",
        'pages_move_from': "Sayfadan:",
        'pages_move_to': "Sayfaya kadar:",
        'pages_move_target': "Hedef konum",
        'pages_move_before': "Şu sayfadan önce taşı:",
        'pages_move_hint': "Not: sayfa 1 = başlangıç, {0} = son",
        'pages_range_invalid': "Başlangıç sayfası bitiş sayfasından küçük veya eşit olmalıdır.",
        'pages_position_invalid': "Hedef konum taşınacak aralığın içinde olamaz.",
        'pages_no_pdf_selected': "Hiç PDF seçilmedi.",
        'pages_deleted': "{0} sayfa silindi.",
        'pages_extracted': "Çıkarıldı: {0}\nŞuraya kaydedildi: {1}\nDosya boyutu: {2:.1f} KB",
        'pages_inserted': "{0} sayfa eklendi",
        'pages_moved': "{0} sayfa taşındı.",
        'pages_deleted_none': "Hiç sayfa silinmedi.",
        'pages_delete_progress': "Sayfalar siliniyor...",
        'pages_deleted_with_backup': "{0} sayfa silindi.\n\nYedek: {1}",
        'pages_deleted_voice': "Bir yedek oluşturuldu ve {0} sayfa silindi.",
        'info': "Bilgi",
        'error_dialog_creation': "İletişim kutusu oluşturulamadı",
        'extract_page_single': "{0}. sayfayı çıkar",
        'extract_page_range': "{0}-{1}. sayfaları çıkar",
        'extract_success_voice': "Sayfalar başarıyla çıkarıldı",
        'extract_error_format': "Çıkarma hatası: {0}",
        'pages_inserted_voice': "{0} sayfa eklendi.",
        'insert_error_format': "Ekleme hatası: {0}",
        'pages_move_progress': "Sayfalar taşınıyor...",
        'pages_moved_with_backup': "{0} sayfa taşındı.\n\nYedek: {1}",
        'move_success_title': "Başarıyla taşındı",
        'pages_moved_voice': "{0} sayfa başarıyla taşındı",
        'mark_removed': "{0}. sayfadan işaret kaldırıldı",
        'mark_empty': "{0}. sayfa boş olarak işaretlendi",
        'mark_export_removed': "{0}. sayfadan dışa aktarma işareti kaldırıldı",
        'mark_export': "{0}. sayfa dışa aktarma için işaretlendi",
        'no_empty_pages': "Silinecek boş sayfa işaretlenmemiş",
        'delete_empty_confirm': "İşaretli {0} boş sayfanın tamamı silinsin mi?",
        'delete_empty_confirm_voice': "İşaretli {0} boş sayfa şimdi silinsin mi? Evet mi Hayır mı?",
        'empty_pages_deleted': "{0} boş sayfa silindi",
        'no_export_pages': "Dışa aktarma için işaretlenmiş sayfa yok",
        'overwrite_title': "Mevcut dosyanın üzerine yaz",
        'overwrite_question': "{0}\n\ndosyası zaten mevcut.\nÜzerine yazılsın mı?",
        'overwrite_voice': "Mevcut dosyanın üzerine yazılsın mı? Evet mi Hayır mı?",
        'page_skipped': "{0}. sayfa atlandı",
        'export_complete': "Dışa aktarma tamamlandı.",
        'export_complete_voice': "Dışa aktarma tamamlandı.",
        'no_pages_exported': "Hiç sayfa dışa aktarılmadı",
        'export_cancelled': "Dışa aktarma iptal edildi",
        'pages_exported': "{0} sayfa {1} konumuna dışa aktarıldı",
        'export_page_title': "Sayfayı dışa aktar",
        'page_exported': "{0}. sayfa {1} konumuna dışa aktarıldı",
        'export_error': "Dışa aktarma hatası",
        'export_marked_title': "İşaretli sayfaları dışa aktar",
        'rotate_all_title': "tüm sayfaları döndür",
        'rotate_all_question': "Tüm sayfalar 90 derece sağa döndürülsün mü?",
        'rotate_all_voice': "Tüm sayfalar 90 derece sağa döndürülsün mü? Evet mi Hayır mı?",
        'all_pages_rotated': "Tüm sayfalar döndürüldü",
        'page_rotated': "{0}. sayfa döndürüldü",
        'rotate_error': "Sayfa döndürülemedi",
        'delete_page_confirm': "{0}. sayfa silinsin mi?",
        'delete_page_confirm_voice': "{0}. sayfa gerçekten silinsin mi? Evet mi Hayır mı?",
        'page_deleted': "{0}. sayfa silindi",
        'delete_error': "Sayfa silinemedi",
        'pages_deleted_voice': "{0} sayfa silindi",
        'pages_exported_split': "{0} sayfa başarıyla dışa aktarıldı.",
        'pages_skipped': "{0} sayfa atlandı.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Sayfaları çıkar (gelişmiş)",
        'pdf_splitter_title': "PDF Ayırıcı ve Çıkarıcı",
        'pdf_splitter_load': " PDF dosyası seç",
        'pdf_splitter_info': "PDF belgeniz için bir seçenek belirleyin",
        'pdf_splitter_basic': "Temel işlemler",
        'pdf_splitter_single': "Tek tek sayfalara ayır",
        'pdf_splitter_range': "Sayfaları çıkar:",
        'pdf_splitter_range_placeholder': "ör. 1-3,5,7-9",
        'pdf_splitter_clean': "Temizleme işlemleri",
        'pdf_splitter_remove_empty': "Tüm boş sayfaları kaldır",
        'pdf_splitter_remove': "Sayfa aralığını sil:",
        'pdf_splitter_remove_placeholder': "ör. 2,4-6",
        'pdf_splitter_process': "PDF'yi işle",
        'pdf_splitter_loaded': "PDF yüklendi. Lütfen bir seçenek belirleyin",
        'pdf_read_error': "PDF okunamadı",
        'pages': "Sayfalar",
        'pages_created': "Sayfalar oluşturuldu",
        'range_empty': "Lütfen bir sayfa aralığı girin",
        'range_invalid': "Geçersiz sayfa aralığı",
        'range_created': "Seçili sayfalarla yeni PDF oluşturuldu:\n{0}",
        'empty_removed': "{0} boş sayfa kaldırıldı.\nÇıktı: {1}",
        'remove_empty': "Lütfen kaldırılacak sayfaları girin",
        'remove_invalid': "Kaldırılacak sayfalar geçersiz",
        'remove_done': "Temizlenmiş PDF oluşturuldu:\n{0}",
        'open_folder': "Klasörü aç",
        'show_in_finder': "Finder'da göster",
        'pdf_splitter_no_pdf': "Lütfen önce bir PDF dosyası yükleyin.",
        'process_error': "PDF işlenirken hata",
        'pages_created_voice': "{0} sayfa oluşturuldu",
        'range_created_voice': "Seçili sayfalarla PDF oluşturuldu",
        'empty_removed_voice': "{0} boş sayfa kaldırıldı",
        'remove_done_voice': "Temizlenmiş PDF oluşturuldu",
        'pdf_splitter_split_groups': "Her bitişik grubu ayrı dosyaya",
        'range_created_single': "Yeni PDF oluşturuldu:\n{0}",
        'range_created_multiple': "{0} PDF dosyası oluşturuldu.",
        'range_created_voice_single': "Seçili sayfalarla bir PDF oluşturuldu",
        'range_created_voice_multiple': "{0} PDF dosyası oluşturuldu",
        'empty_removed_none_left': "Hiç sayfa kalmadı",
        'empty_removed_all_empty': "Tüm sayfalar boş olarak algılandı ve kaldırılacaktı. Hiç dosya oluşturulmadı.",
        'preview_single': "Önizleme: {0}",
        'preview_enter_range': "Lütfen bir sayfa aralığı girin.",
        'preview_invalid_range': "Geçersiz sayfa aralığı.",
        'preview_file': "Önizleme: {0}",
        'preview_files': "Önizleme: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Yazdırma başlatılıyor",
        'print_sent': "Yazdırma işi gönderildi",
        'print_now': "Hemen yazdır",
        'print_error': "Hemen yazdırma hatası",
        'print_limited': "Bu sistemde yazdırma işlevi sınırlı",
        'print_error_format': "Hemen yazdırma hatası: {0}",
        'warning': "Uyarı",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Açık Mod'a geç",
        'mode_switch_to_dark': "Koyu Mod'a geç",
        'mode_dark_activated': "Koyu Mod etkinleştirildi",
        'mode_light_activated': "Açık Mod etkinleştirildi",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Tam görünüm",
        'zoom_two_pages': "Yan yana iki sayfa",
        'zoom_overview': "Genel bakış modu",
        'zoom_cannot_during_search': "Arama sırasında yakınlaştırma yapılamaz",
        'zoom_exit_first': "Lütfen önce yakınlaştırmadan çıkın",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Sürükle ve Bırak etkin",
        'drag_disabled': "Sürükle ve Bırak devre dışı",
        'drag_page_grab': "{0}. sayfa tutuluyor",
        'drag_page_dropped': "{0}. sayfa {1}. konuma eklendi",
        'drag_position_invalid': "Geçersiz konum",
        'drag_same_position': "{0}. sayfa {0}. konumda kalıyor",
        'drag_error': "Taşıma hatası",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Gelişmiş biçimlendirme ve metin bloğu yönetimi ile metin girişi",
        'text_templates': "Mevcut metin blokları:",
        'text_name': "Ad",
        'text_preview': "Metin önizlemesi",
        'text_enter': "Metin:",
        'text_font_size': "Yazı tipi boyutu:",
        'text_formatting': "Biçimlendirme:",
        'text_bold': "Kalın",
        'text_italic': "İtalik",
        'text_underline': "Altı çizili",
        'text_alignment': "Hizalama:",
        'text_left': "Sol",
        'text_center': "Orta",
        'text_right': "Sağ",
        'text_color': "Metin rengi:",
        'text_opacity': "Opaklık:",
        'text_word_wrap': "Satır kaydırma:",
        'text_auto': "Otomatik",
        'text_page_width_95': "Sayfa genişliği (%95)",
        'text_page_width_85': "Çok geniş (%85)",
        'text_page_width_75': "Daha geniş (%75)",
        'text_page_width_60': "Geniş (%60)",
        'text_page_width_50': "Orta (%50)",
        'text_page_width_30': "Dar (%30)",
        'text_page_width_20': "Daha dar (%20)",
        'text_page_width_10': "Çok dar (%10)",
        'text_no_wrap': "Kaydırma yok",
        'text_private': "Özel metin bloğu (kimlik doğrulama gerektirir)",
        'text_preview_label': "Önizleme:",
        'text_preview_placeholder': "Metnin önizlemesi burada gösterilecek...",
        'text_no_text': "(Metin yok)",
        'text_save_template': "💾 Blok olarak kaydet",
        'text_delete_template': "🗑 Seçili metin bloğunu sil",
        'text_show_private': "Özel olanları göster",
        'text_hide_private': "Özel olanları gizle",
        'text_use': "✅ Metni kullan",
        'text_saved': "Metin bloğu şu şekilde kaydedildi:\n{0}",
        'text_saved_voice': "Metin bloğu kaydedildi",
        'text_deleted': "Metin bloğu silindi",
        'text_no_text_to_save': "Kaydedilecek metin yok.",
        'text_no_templates': "Metin bloğu bulunamadı",
        'text_private_master_required': "Özel bloklar yalnızca bir ana şifre oluşturulmuşsa kullanılabilir.\n\nŞimdi bir ana şifre oluşturulsun mu?",
        'text_filename': "Metin bloğu için dosya adı ('Text_' ve '.txt' olmadan):",
        'text_filename_hint': "Örnek: 'Ev Telefonu' -> 'Text_Ev Telefonu.txt' olarak kaydedilir",
        'text_save_hint': "Metin bloğu biçimlendirmeyle birlikte otomatik olarak kaydedilir.",
        'text_guide_title': "Metin girişi - Kılavuz",
        'text_delete_confirm': "Metin bloğu gerçekten silinsin mi?\n\nDosya: {0}\nMetin: {1}...",
        'text_make_public': "Herkese açık olarak işaretle",
        'text_make_private': "Özel olarak işaretle",
        'text_privacy_changed': "Gizlilik durumu değiştirildi",
        'text_private_always': "Özel olanlar her zaman görünür (ayar)",
        'text_mode_required': "Lütfen önce metin modunu etkinleştirin",
        'text_continue_editing': "Düzenlemeye devam et - imleç metnin sonunda",
        'text_no_input': "Hiç metin girilmedi - metin iptal edildi",
        'save_dialog_question': "Nasıl devam etmek istersiniz?",
        'text_save_question': "Tüm metinler ve çarpılar kaydedilsin mi, ayarlansın mı, düzenlemeye devam edilsin mi yoksa iptal edilsin mi?",
        'copy_cross': "Çarpı kopyalandı",
        'paste_cross': "Çarpı yapıştırıldı",
        'paste_text': "Metin yapıştırıldı",
        'cross_discarded': "Çarpı iptal edildi",
        'all_discarded': "Her şey iptal edildi",
        'text_discarded': "Metin iptal edildi",
        'no_texts_to_save': "Kaydedilecek metin yok",
        'no_valid_texts': "Kaydedilecek geçerli metin yok",
        'text_word_singular': "metin",
        'text_word_plural': "metin",
        'cross_word_singular': "çarpı",
        'cross_word_plural': "çarpı",
        'texts_saved_title': "Metinler kaydedildi",
        'texts_crosses_saved': "{0} {1} ve {2} {3} PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'texts_crosses_saved_voice': "{0} {1} ve {2} {3} kaydedildi.",
        'texts_saved': "{0} {1} PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'texts_saved_voice': "{0} {1} kaydedildi.",
        'crosses_saved': "{0} {1} PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'crosses_saved_voice': "{0} {1} kaydedildi.",
        'elements_saved': "{0} öğe PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'elements_saved_voice': "{0} öğe kaydedildi.",
        'text_window_load_error': "Metin penceresi yüklenemedi",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Metin girişi ve metin blokları – Ayrıntılı kılavuz**

        **1. Metin ekleme ve düzenleme**
        - Belgede istediğiniz yere sağ tıklayın ve "Metin ekle"yi seçin.
        - Metninizi girip biçimlendirebileceğiniz bir iletişim kutusu açılır:
        • Yazı tipi boyutu, Kalın, İtalik, Altı çizili
        • Metin rengi (serbest seçim)
        • Saydamlık (opaklık) kaydırma çubuğu ile
        • Satır kaydırma (çeşitli genişlikler, örn. sayfa genişliği, dar, kaydırma yok)
        - Onaydan sonra metin tıklanan konumda görünür. Fare veya ok tuşlarıyla taşıyabilirsiniz.
        - Metne çift tıklamak düzenleme modunu açar; ESC ile çıkılır.

        **2. Metin bloklarını (şablonları) yönetme**
        - Metin iletişim kutusunda, solda kaydedilmiş tüm metin bloklarının bir listesini görürsünüz.
        - **Blok kaydetme:** Metninizi girin, biçimlendirin ve "💾 Blok olarak kaydet"e tıklayın. Bir dosya adı girin (uzantısız).
        - **Blok yükleme:** Listede istediğiniz ada tıklayın. Metin ve biçimlendirme uygulanır ve gerekiyorsa ayarlanabilir.
        - **Silme:** Bir bloğa sağ tıklayarak silebilir veya gizlilik durumunu değiştirebilirsiniz.

        **3. Özel metin blokları (Ana şifre)**
        - Bir ana şifre oluşturduysanız (Ayarlar → Şifre Yöneticisi altında), blokları "özel" olarak işaretleyebilirsiniz.
        - Kaydetmeden önce iletişim kutusundaki "Özel metin bloğu" onay kutusunu etkinleştirin.
        - Özel bloklar, listede yalnızca oturumda bir kez ana şifrenizi girdiğinizde gösterilir (kilit simgesiyle veya ilk erişimde kimlik doğrulama).
        - Bu sayede gizli metin bloklarını yetkisiz erişime karşı koruyabilirsiniz.

        **4. Çarpı ekleme**
        - Bağlam menüsü üzerinden grafiksel bir çarpı da ekleyebilirsiniz (örneğin onay kutuları için).
        - Çarpıların boyutu, çizgi kalınlığı ve rengi ayarlarda genel olarak değiştirilebilir ("Ayarlar" menüsü → "Çarpı ayarları").
        - Mevcut bir çarpıya sağ tıklayarak onu bireysel olarak değiştirebilirsiniz.

        **5. Toplu işlemler**
        - Bir sayfada birden çok metin veya çarpı yerleştirdiyseniz, bağlam menüsü (metin modunda sağ tıklama) üzerinden tüm öğeleri birlikte kaydedebilir veya iptal edebilirsiniz.
        - Kaydederken tüm öğeler PDF'ye gömülür ve vektör grafik olarak kalır.

        **6. Metin modunda klavye kısayolları**
        - Ok tuşları: öğeyi taşı
        - Ctrl+Ok tuşları: daha büyük adımlar
        - Enter: kaydetme iletişim kutusunu aç (tümünü kaydet / ayarla / iptal et)
        - ESC: geçerli öğeyi iptal et
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Metin girişi ve metin blokları – Ayrıntılı kılavuz</strong></p>

        <p><strong>1. Metin ekleme ve düzenleme</strong></p>
        <ul>
        <li>Belgede istediğiniz yere sağ tıklayın ve "Metin ekle"yi seçin.</li>
        <li>Metninizi girip biçimlendirebileceğiniz bir iletişim kutusu açılır:<br/>
        • Yazı tipi boyutu, Kalın, İtalik, Altı çizili<br/>
        • Metin rengi (serbest seçim)<br/>
        • Saydamlık (opaklık) kaydırma çubuğu ile<br/>
        • Satır kaydırma (çeşitli genişlikler, örn. sayfa genişliği, dar, kaydırma yok)</li>
        <li>Onaydan sonra metin tıklanan konumda görünür. Fare veya ok tuşlarıyla taşıyabilirsiniz.</li>
        <li>Metne çift tıklamak düzenleme modunu açar; ESC ile çıkılır.</li>
        </ul>

        <p><strong>2. Metin bloklarını (şablonları) yönetme</strong></p>
        <ul>
        <li>Metin iletişim kutusunda, solda kaydedilmiş tüm metin bloklarının bir listesini görürsünüz.</li>
        <li><strong>Blok kaydetme:</strong> Metninizi girin, biçimlendirin ve "💾 Blok olarak kaydet"e tıklayın. Bir dosya adı girin (uzantısız).</li>
        <li><strong>Blok yükleme:</strong> Listede istediğiniz ada tıklayın. Metin ve biçimlendirme uygulanır ve gerekiyorsa ayarlanabilir.</li>
        <li><strong>Silme:</strong> Bir bloğa sağ tıklayarak silebilir veya gizlilik durumunu değiştirebilirsiniz.</li>
        </ul>

        <p><strong>3. Özel metin blokları (Ana şifre)</strong></p>
        <ul>
        <li>Bir ana şifre oluşturduysanız (Ayarlar → Şifre Yöneticisi altında), blokları "özel" olarak işaretleyebilirsiniz.</li>
        <li>Kaydetmeden önce iletişim kutusundaki "Özel metin bloğu" onay kutusunu etkinleştirin.</li>
        <li>Özel bloklar, listede yalnızca oturumda bir kez ana şifrenizi girdiğinizde gösterilir (kilit simgesiyle veya ilk erişimde kimlik doğrulama).</li>
        <li>Bu sayede gizli metin bloklarını yetkisiz erişime karşı koruyabilirsiniz.</li>
        </ul>

        <p><strong>4. Çarpı ekleme</strong></p>
        <ul>
        <li>Bağlam menüsü üzerinden grafiksel bir çarpı da ekleyebilirsiniz (örneğin onay kutuları için).</li>
        <li>Çarpıların boyutu, çizgi kalınlığı ve rengi ayarlarda genel olarak değiştirilebilir ("Ayarlar" menüsü → "Çarpı ayarları").</li>
        <li>Mevcut bir çarpıya sağ tıklayarak onu bireysel olarak değiştirebilirsiniz.</li>
        </ul>

        <p><strong>5. Toplu işlemler</strong></p>
        <ul>
        <li>Bir sayfada birden çok metin veya çarpı yerleştirdiyseniz, bağlam menüsü (metin modunda sağ tıklama) üzerinden tüm öğeleri birlikte kaydedebilir veya iptal edebilirsiniz.</li>
        <li>Kaydederken tüm öğeler PDF'ye gömülür ve vektör grafik olarak kalır.</li>
        </ul>

        <p><strong>6. Metin modunda klavye kısayolları</strong></p>
        <ul>
        <li>Ok tuşları: öğeyi taşı</li>
        <li>Ctrl+Ok tuşları: daha büyük adımlar</li>
        <li>Enter: kaydetme iletişim kutusunu aç (tümünü kaydet / ayarla / iptal et)</li>
        <li>ESC: geçerli öğeyi iptal et</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Çarpı ayarları",
        'cross_properties': "Çarpı özellikleri",
        'cross_size': "Boyut (px):",
        'cross_line_width': "Çizgi kalınlığı:",
        'cross_color': "Renk:",
        'cross_choose_color': "Seç",
        'cross_fine_tuning': "Kaydederken ince ayar (piksel)",
        'cross_offset_x': "X kayması:",
        'cross_offset_y': "Y kayması:",
        'cross_offset_x_tooltip': "Negatif değerler çarpıyı sola, pozitifler sağa kaydırır",
        'cross_offset_y_tooltip': "Negatif değerler çarpıyı yukarı, pozitifler aşağı kaydırır",
        'cross_preview': "Önizleme",
        'cross_save': "Ayarları uygula",
        'cross_customized': "Çarpı ayarlandı",
        'cross_settings_applied': "Çarpı ayarları kaydedildi.\nBoyut: {0}px, Çizgi kalınlığı: {1}px\n{2}",
        'cross_updated_count': "Mevcut {0} çarpı güncellendi.",
        'cross_no_crosses': "Mevcut çarpı bulunamadı.",
        'cross_settings_applied_all': "Çarpı ayarları tüm {0} çarpıya uygulandı",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "İmza ayarları",
        'signature_1': "İmza 1",
        'signature_2': "İmza 2",
        'signature_select': "İmza seç",
        'signature_add': "➕ Yeni imza ekle...",
        'signature_size': "{0}. imza için boyut (%):",
        'signature_common': "Genel ayarlar",
        'signature_timestamp': "Otomatik olarak zaman damgası ekle",
        'signature_location': "Varsayılan yer:",
        'signature_timestamp_size': "Zaman damgası yazı tipi boyutu:",
        'signature_no_files': "-- İmza bulunamadı --",
        'signature_insert': "İmza ekle",
        'signature_insert_1': "İmza 1 ekle",
        'signature_insert_2': "İmza 2 ekle",
        'signature_customize': " İmzayı özelleştir",
        'signature_discard': " Bu imzayı iptal et",
        'signature_save_all': " Tüm imzaları kaydet",
        'signature_discard_all': " Tüm imzaları iptal et",
        'signature_guide_title': "İmzalar - Kılavuz",
        'signature_guide': """
📝 İmzalar - Hızlı kılavuz

- Ana şifre oluşturun
- İmzaları Ayarlar menüsünde yapılandırın
  (boyut, zaman damgası ...)
- İstediğiniz konuma SAĞ TIKLAYARAK ekleyin
  (oturumda bir kez ana şifre gerekir)
- İmzayı fare veya ok tuşlarıyla taşıyın
- Birden çok imza art arda eklenebilir
- Her imza ayrı ayrı özelleştirilebilir
- Tek bir imzayı iptal edin
- Tüm imzaları bir kerede kaydedin / iptal edin
- Alternatif olarak menü çubuğu kullanılabilir.
        """,
        'signature_placeholder': "Önizleme mevcut değil",
        'signature_info': "İmza {0}: {1}×{2} px ({3}% / {4}×{5})",
        'signature_info_placeholder': "{0}. imza için ayarlar",
        'signature_inserted': "İmza {0} {1}. sayfaya eklendi",
        'signature_deleted': "İmza silindi",
        'signature_copied': "İmza kopyalandı",
        'signature_pasted': "İmza {0} yapıştırıldı",
        'signature_saved': "{0} imza PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'signature_saved_voice': "{0} imza kaydedildi",
        'mode_replace_signature_format': "Moddan çık ve {0}. imzayı ekle",
        'mode_conflict_voice_signature': "{0} modu etkin. Çıkılıp imza eklensin mi?",
        'signature_not_configured': "İmza {0} yapılandırılmamış",
        'signature_file_not_found': "İmza dosyası bulunamadı",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Kopyalanmış imza yok",
        'no_signatures_to_save': "Kaydedilecek imza yok",
        'signature_save_question': "Tüm imzalar kaydedilsin mi, ayarlansın mı yoksa bu iptal edilsin mi?",
        'signatures_saved_title': "İmzalar kaydedildi",
        'signatures_saved': "{0} imza PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'signatures_saved_voice': "{0} imza kaydedildi.",
        'all_signatures_discarded': "Tüm imzalar iptal edildi",
        'signature_settings_saved': "İmza ayarları kaydedildi",
        'signature_cancelled': "İmza iptal edildi",
        'signature_active_title': "İmza etkin",
        'signature_replace_question': "Zaten etkin bir imza var.\n\nMevcut imza değiştirilsin mi?",
        'signature_replace': "İmzayı değiştir",
        'signature_replace_voice': "Mevcut imza değiştirilsin mi yoksa iptal edilsin mi?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Resim ayarları",
        'image_common': "Genel resim ayarları",
        'image_keep_aspect': "Sürüklerken en boy oranını koru",
        'image_default_size': "Varsayılan boyut (%):",
        'image_dark_invert': "Koyu Modda resimleri ters çevir",
        'image_dark_invert_tooltip': "Etkin: daha iyi görünürlük için resimler ters çevrilir",
        'image_fine_tuning': "İnce ayar (piksel)",
        'image_offset_x': "X kayması:",
        'image_offset_y': "Y kayması:",
        'image_offset_x_tooltip': "Negatif değerler resmi sola, pozitifler sağa kaydırır",
        'image_offset_y_tooltip': "Negatif değerler resmi yukarı, pozitifler aşağı kaydırır",
        'image_select': "Resim seç",
        'image_insert': "Resim ekle",
        'image_customize': " Resmi özelleştir",
        'image_aspect': " En boy oranını koru",
        'image_discard': " Bu resmi iptal et",
        'image_save_all': " Tüm resimleri kaydet",
        'image_discard_all': " Tüm resimleri iptal et",
        'image_filter': "Resimler",
        'image_guide_title': "Resim ekleme - Kılavuz",
        'image_guide': """
📷 PDF'ye resim ekleme - Hızlı kılavuz:

1. İstediğiniz konuma sağ tıklayın
2. "Resim ekle" → resim seçin
3. Resmi konumlandırın: fareyle sürükleyin
4. Boyutu ayarlayın: köşelerden/kenarlardan sürükleyin
5. En boy oranını koruyun: [A] tuşu
6. Diğer ayarlar: resme sağ tıklayın

İpucu: Ayarları bağlam menüsünde değiştirebilirsiniz.
        """,
        'image_inserted': "{0}. resim {1}. sayfaya eklendi",
        'image_deleted': "Resim iptal edildi",
        'image_copied': "Resim kopyalandı",
        'image_pasted': "Resim yapıştırıldı",
        'image_saved': "{0} resim PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'image_saved_voice': "{0} resim kaydedildi",
        'image_aspect_on': "etkin",
        'image_aspect_off': "devre dışı",
        'image_aspect_toggle': "En boy oranını koru {0}",
        'image_reset': "Resim orijinal boyutuna sıfırlandı",
        'image_replaced': "Resim değiştirildi",
        'image_invalid': "Geçerli bir resim değil",
        'mode_replace_image': "Resim ekle",
        'mode_conflict_voice_image': "{0} modu etkin. Çıkılıp resim eklensin mi?",
        'image_active_title': "Resim etkin",
        'image_replace_question': "Zaten etkin bir resim var.\n\nMevcut resim değiştirilsin mi?",
        'image_replace': "Resmi değiştir",
        'image_replace_voice': "Mevcut resim değiştirilsin mi yoksa iptal edilsin mi?",
        'image_filter_all': "Resimler (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Tüm dosyalar (*.*)",
        'no_copied_image': "Kopyalanmış resim yok",
        'image_discarded': "Resim iptal edildi",
        'image_save_question': "Tüm resimler kaydedilsin mi, ayarlansın mı yoksa bu iptal edilsin mi?",
        'no_images_to_save': "Kaydedilecek resim yok",
        'no_valid_images': "Kaydedilecek geçerli resim yok",
        'images_saved_title': "Resimler kaydedildi",
        'images_saved': "{0} resim PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'images_saved_voice': "{0} resim kaydedildi.",
        'all_images_discarded': "Tüm resimler iptal edildi",
        'image_settings_updated': "Resim ayarları güncellendi",
        'image_replace_title': "Yeni resim seç",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Şekil ayarları",
        'form_basic': "Temel ayarlar",
        'form_default_type': "Varsayılan şekil türü:",
        'form_rectangle': "Dikdörtgen",
        'form_ellipse': "Elips",
        'form_line': "Çizgi",
        'form_arrow': "Ok",
        'form_line_width': "Çizgi kalınlığı:",
        'form_colors': "Renkler",
        'form_line_color': "Çizgi rengi:",
        'form_fill_color': "Dolgu rengi:",
        'form_choose_color': "Seç",
        'form_transparent': "Saydam arka plan (sadece çizgi)",
        'form_filled': "dolgulu",
        'form_dark_mode': "Koyu Mod",
        'form_dark_invert': "Koyu Modda renkleri ters çevir",
        'form_fine_tuning': "İnce ayar (piksel)",
        'form_offset_x': "X kayması:",
        'form_offset_y': "Y kayması:",
        'form_offset_x_tooltip': "Negatif değerler şekli sola, pozitifler sağa kaydırır",
        'form_offset_y_tooltip': "Negatif değerler şekli yukarı, pozitifler aşağı kaydırır",
        'form_preview': "Önizleme",
        'form_insert': "Şekil ekle",
        'form_rectangle_insert': "Dikdörtgen",
        'form_ellipse_insert': "Elips/Çember",
        'form_line_insert': "Çizgi (2 tıklama)",
        'form_arrow_insert': "Ok (2 tıklama)",
        'form_customize': " Şekli özelleştir",
        'form_transparent_toggle': " Saydam arka plan",
        'form_discard': " Bu şekli iptal et",
        'form_save_all': " Tüm şekilleri kaydet",
        'form_discard_all': " Tüm şekilleri iptal et",
        'form_guide_title': "Şekil ekleme - Kılavuz",
        'form_guide': """
📐 PDF'ye şekil ekleme - Hızlı kılavuz:

1. Şekil türünü seçin (dikdörtgen, elips, çizgi, ok)
2. Konuma tıklayın
   - Dikdörtgen/Elips: Tek tıklama şekli yerleştirir
   - Çizgi/Ok: Başlangıç ve bitiş için iki tıklama
3. Şekli konumlandırın: fareyle sürükleyin
4. Boyutu ayarlayın: köşelerden/kenarlardan sürükleyin
5. Şekli kaydedin: Enter
6. Şekli iptal edin: ESC
7. Diğer ayarlar: şekle sağ tıklayın

İpucu: Ayarları bağlam menüsünde değiştirebilirsiniz.
        """,
        'form_inserted': "{0} {1}. sayfaya eklendi",
        'form_deleted': "Şekil silindi",
        'form_copied': "Şekil kopyalandı",
        'form_pasted': "Şekil yapıştırıldı",
        'form_saved': "{0} şekil PDF'ye eklendi.\n\nPDF yeniden yüklendi...",
        'form_saved_voice': "{0} şekil kaydedildi",
        'form_reset': "Şekil varsayılan boyuta sıfırlandı",
        'form_transparent_on': "etkin",
        'form_transparent_off': "devre dışı",
        'form_transparent_toggled': "Saydam arka plan {0}",
        'form_line_cancel': "Çizgi çizme iptal edildi",
        'form_second_click': "Şimdi {0} için bitiş noktasına tıklayın",
        'mode_replace_form': "Şekil ekle",
        'mode_conflict_voice_form': "{0} modu etkin. Çıkılıp bir şekil eklensin mi?",
        'form_settings_updated': "Şekil ayarları güncellendi",
        'form_unknown': "Şekil",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Başlangıç konumuna tıklayın",
        'form_line_guide_2': "2. Bitiş konumuna tıklayın",
        'form_line_guide_3': "Çizgi iki nokta arasına çizilecektir.",
        'form_line_status_1': "İlk tıklama bekleniyor...",
        'form_line_status_2': "İlk nokta ayarlandı: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Şimdi bitiş noktasına tıklayın...",
        'form_line_status_4': "Her iki nokta da ayarlandı.\nKaydetmek için 'Tamam' düğmesine tıklayın.",
        'form_line_reset': "Sıfırla",
        'form_line_finish': "Tamam",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopyala (Cmd+C)",
        'paste': "Yapıştır (Cmd+V)",
        'copied': "Kopyalandı: {0}",
        'no_element_to_copy': "Kopyalanacak öğe seçilmedi",
        'no_copied_data': "Kopyalanmış veri yok",
        'no_valid_position': "Yapıştırmak için geçerli konum yok",
        'copy_text': "Metin kopyalandı",
        'copy_image': "Resim kopyalandı",
        'copy_form': "Şekil kopyalandı",
        'copy_signature': "İmza kopyalandı",
        'element_text': "metin",
        'element_image': "resim",
        'element_form': "şekil",
        'element_signature': "imza",
        'element_unknown': "öğe",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Mod çakışması",
        'mode_conflict_message': "'{0}' modu zaten etkin.\n\nBu moddan çıkılıp {1}?",
        'mode_replace': "Moddan çık ve {0}",
        'mode_cancel': "İptal",
        'mode_replace_text': "metin ekle",
        'mode_replace_cross': "çarpı ekle",
        'mode_replace_signature': "imza ekle",
        'mode_replace_image': "resim ekle",
        'mode_replace_form': "şekil ekle",
        'mode_conflict_voice': "{0} modu etkin. Çıkılıp metin eklensin mi?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Metin girişi",
        'active_mode_signature': "İmza",
        'active_mode_image': "Resim",
        'active_mode_form': "Şekil",
        'active_mode_and': " ve ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Ekle",                    # Hauptmenü
        'insert_another_text': "Metin ekle",          # Vereinfacht
        'insert_another_cross': "Çarpı ekle",        # Vereinfacht
        'insert_another_signature_1': "İmza 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "İmza 2",      # Untermenü-Eintrag
        'insert_another_image': "Resim ekle",         # Vereinfacht
        'insert_another_form_rect': "Dikdörtgen",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Elips",        # Untermenü-Eintrag
        'insert_another_form_line': "Çizgi (2 tıklama)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Ok (2 tıklama)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} kaydet",
        'save_dialog_message': "{0}, {1}. sayfaya kaydedilecek.\n\nNasıl devam etmek istersiniz?",
        'save_all': "Tüm {0} kaydet",
        'save_single': "{0} kaydet",
        'save_customize': "{0} ayarla",
        'save_discard': "Bu {0} iptal et",
        'save_continue': "Düzenlemeye devam et",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " {0}. sayfaya git",
        'context_rotate': " {0}. sayfayı döndür",
        'context_delete': " {0}. sayfayı sil",
        'context_export': " {0}. sayfayı dışa aktar",
        'context_mark_as': " Sayfayı şu şekilde işaretle...",
        'context_mark_empty': " Boş sayfa",
        'context_unmark_empty': " Artık boş değil",
        'context_mark_export': " Dışa aktarılacak olarak işaretle",
        'context_unmark_export': " Artık dışa aktarma",
        'context_batch_actions': " Toplu işlemler",
        'context_batch_delete_empty': " {0} boş sayfayı sil",
        'context_batch_export_single': " Tüm {0} sayfa (tek dosya)",
        'context_batch_export_split': " Tüm {0} sayfa (ayrı ayrı)",
        'context_drag_start': " Sürükle ve Bırak'ı başlat",
        'context_drag_stop': " Sürükle ve Bırak'ı bitir",
        'context_insert': " Ekle",
        'context_insert_pages': " Sayfa ekle",
        'context_zoom': "Yakınlaştır",
        'discard_mixed': "{0} {1} ve {2} {3} iptal et",
        'save_mixed': "{0} {1} ve {2} {3} kaydet",
        'discard_texts': "{0} metni iptal et",
        'discard_text_single': "1 metin iptal et",
        'save_texts': "{0} metni kaydet",
        'save_text_single': "1 metin kaydet",
        'discard_crosses': "{0} çarpıyı iptal et",
        'discard_cross_single': "1 çarpıyı iptal et",
        'save_crosses': "{0} çarpıyı kaydet",
        'save_cross_single': "1 çarpıyı kaydet",
        'discard_signatures': "{0} imzayı iptal et",
        'save_signature_single': "1 imzayı kaydet",
        'save_signatures': "{0} imzayı kaydet",
        'discard_images': "{0} resmi iptal et",
        'save_image_single': "1 resmi kaydet",
        'save_images': "{0} resmi kaydet",
        'discard_forms': "{0} şekli iptal et",
        'save_form_single': "1 şekli kaydet",
        'save_forms': "{0} şekli kaydet",
        'cross_discard': "Bu çarpıyı iptal et",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Dışa Aktarma / İçe Aktarma Bilgisi",
        'export_what': "📋 Neler dışa aktarılır?",
        'export_general': "Genel ayarlar",
        'export_general_items': "• Sesli çıktı (açık/kapalı, hız)\n• Koyu/Açık Mod\n• Yedekleme ayarları\n• OCR ayarları",
        'export_image_form': "Resim ve şekil ayarları",
        'export_image_form_items': "• Resim ayarları (en boy oranı, varsayılan boyut)\n• Şekil ayarları (çizgi kalınlığı, renkler)\n• İmza ayarları (yollar, boyutlar, zaman damgası)",
        'export_passwords': "Şifre veritabanı",
        'export_passwords_items': "• Kayıtlı tüm PDF şifreleri\n• İsteğe bağlı şifrelenmiş veya şifresi çözülmüş",
        'export_master': "Ana şifre ayarları",
        'export_master_items': "• Ana şifre karması\n• İmza/metin bloğu ayarları",
        'export_signatures': "İmzalar ve metin blokları",
        'export_signatures_items': "• Tüm resim dosyaları (imzalar)\n• Biçimlendirmeli tüm metin blokları\n• Özel/herkese açık işaretlemeler",
        'export_import_warning': "⚠️ Önemli notlar",
        'export_import_note': "• İçe aktarırken TÜM mevcut ayarların üzerine yazılır\n• Uygulamanın yeniden başlatılması gerekir\n• Mevcut imzalar/metin blokları değiştirilir",
        'export_master_note': "• Ana şifre belirlenmişse şunları seçebilirsiniz:\n  - Şifresi çözülmüş (şifreler düz metin)\n  - Şifrelenmiş (sadece ana şifreyle okunabilir)",
        'export_security': "• Dışa aktarılan ZIP dosyası gizli veriler içerir\n• Güvenli bir yerde saklayın (örn. şifreli USB bellek)\n• Dosya kaybolursa şifreler geri döndürülemez şekilde kaybolur",
        'export_format': "📁 Dışa aktarma biçimi",
        'export_format_desc': "Ayarlar tek bir ZIP dosyasında saklanır:",
        'export_filename': "PDFDarkView_Ayarlar_YYYYMMGG_SSddss.zip",
        'export_success': "Ayarlar başarıyla dışa aktarıldı",
        'export_failed': "Dışa aktarma başarısız",
        'export_import_question': "Uygulama şimdi yeniden başlatılsın mı?",
        'export_password_question': "Bir ana şifre belirlenmiş.\n\nŞifreler şifresi çözülmüş olarak dışa aktarılsın mı?\n(aksi halde şifrelenmiş olarak dışa aktarılırlar)",
        'export_decrypt': "Şifresi çözülmüş olarak dışa aktar",
        'export_encrypt': "Şifrelenmiş olarak dışa aktar",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Bilgi",
        'info_title': "PDF Dark View Hakkında",
        'info_version': "Sürüm",
        'info_author': "Toralf Schulz (BinhDiez) tarafından geliştirilmiştir",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Hakkında",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong>, özellikle görme engelli kişiler için geliştirilmiş, erişilebilir bir PDF görüntüleyicisidir.</p>

            <p><strong>Temel Özellikler:</strong></p>
            <ul>
                <li>Kontrastlı, özelleştirilebilir arayüz</li>
                <li>Tam klavye kontrolü</li>
                <li>Entegre sesli okuma</li>
                <li>Taranmış belgeler için OCR</li>
                <li>Kapsamlı düzenleme araçları</li>
            </ul>

            <p>50'den fazla dil desteklenmektedir – böylece PDF'ler herkes için erişilebilirdir.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Özellikler",
        'info_features_intro': "PDF Dark View size aşağıdaki olanakları sunar:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Görüntüleme ve Gezinme</strong> – Koyu/Açık mod, sayfa çevirme, yakınlaştırma, sayfaya atlama</li>
            <li><strong>OCR (Metin Tanıma)</strong> – Taranmış belgeleri aranabilir ve kopyalanabilir hale getirin</li>
            <li><strong>Düzenleme</strong> – Metin, çarpı işareti, imza, resim ve şekil ekleme</li>
            <li><strong>Sayfa Yönetimi</strong> – Silme, çıkarma, ekleme, sürükle ve bırak ile taşıma</li>
            <li><strong>Dışa Aktarma</strong> – Word, Pages veya metin olarak</li>
            <li><strong>Güvenlik</strong> – Parola koruması ve yönetimi</li>
            <li><strong>Erişilebilirlik</strong> – Sesli okuma, klavye kontrolü, yüksek kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Kullanım",
        'info_accessibility': "♿ Erişilebilirlik – tam klavye kontrolü",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Genel</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF aç</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Ara</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Koyu/Açık modu değiştir</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Yazdır</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Çıkış</div>

        <div class="shortcut-cat">📖 Gezinme</div>
        <div class="shortcut-row"><kbd>Ok tuşları</kbd> Sayfa sayfa çevir</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Sayfaya git</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> İlk sayfa</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Son sayfa</div>

        <div class="shortcut-cat">✏️ Düzenleme</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Metin ekle</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Sayfaları sil</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Sayfaları çıkar</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Sayfa ekle</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Sayfaları taşı</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Sayfayı döndür</div>

        <div class="shortcut-cat">🖼️ Öğeleri taşıma</div>
        <div class="shortcut-row"><kbd>Ok tuşları</kbd> Metin/resim/imza taşı</div>
        <div class="shortcut-row"><kbd>Ctrl+Ok tuşları</kbd> Daha büyük adımlar</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Kaydet</div>
        <div class="shortcut-row"><kbd>ESC</kbd> İptal et</div>

        <div class="shortcut-cat">🗣️ Sesli okuma</div>
        <div class="shortcut-row"><kbd>F2</kbd> Sesli okumayı aç/kapat</div>
        """,
        'info_contextmenu': "📌 Önemli: Tüm işlevler bağlam menüsü (sağ fare tuşu) üzerinden de erişilebilir!",
        'info_accessibility_hint': "💡 İpucu: Sesli okuma (F2) yön bulmayı kolaylaştırır ve menüler ve diyaloglar hakkında geri bildirim sağlar.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisans & Künye",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 KÜNYE</strong><br>
        § 5 TMG'ye göre bilgiler:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Almanya<br>
        E-posta: binhdiez64@gmail.com<br>
        İçerik sorumlusu: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Sorumluluk reddi</strong><br>
        Yazılım en büyük özenle geliştirilmiştir. Doğruluk, eksiksizlik ve işlevsellik için hiçbir garanti verilmez. Kullanım kendi sorumluluğunuzdadır.<br><br>

        <strong>📄 MIT Lisansı (özel kullanım)</strong><br>
        Telif hakkı (c) 2026 Toralf Schulz (BinhDiez)<br>
        İzin verilen: ücretsiz kullanım, özel değişiklikler, kişisel kopyalar.<br>
        İzin verilmeyen: satış, ticari kullanım, telif hakkı bildirimlerinin kaldırılması.<br><br>

        <strong>🔧 Üçüncü taraf bileşenler</strong><br>
        Bu yazılım, GPL, AGPL, Apache 2.0, BSD ve MIT lisansları altında bileşenler içerir.<br>
        Yeniden dağıtım sırasında ilgili lisans koşullarına uyulmalıdır.<br><br>

        <strong>🌐 Açık Kaynak</strong><br>
        Kaynak kodu mevcuttur ve ilgili lisans koşullarına göre görüntülenebilir, değiştirilebilir ve yeniden dağıtılabilir.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Teşekkürler",
        'info_credits': "Açık kaynak topluluğuna teşekkürler",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF işleme</li>
            <li><strong>PyQt5</strong> – Grafik arayüz</li>
            <li><strong>Tesseract OCR</strong> – Metin tanıma</li>
            <li><strong>OCRmyPDF</strong> – OCR entegrasyonu</li>
            <li><strong>python-docx</strong> – Word dışa aktarımı</li>
            <li><strong>qtawesome</strong> – Simgeler</li>
            <li><strong>DeepSeek</strong> – Çevirilerde destek (50+ dil)</li>
            <li><strong>Tüm kullanıcılar</strong> – Değerli geri bildirimler için</li>
            <li><strong>Açık kaynak topluluğu</strong> – Harika kütüphaneler için</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Diller",
        'info_languages_header': "🌍 Dil Desteği",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View şu anda <strong>62 dili</strong> desteklemektedir – böylece yazılım dünya çapında erişilebilir şekilde kullanılabilir.</p>

            <p><strong>📖 Tam dil listesi (Mart 2026 itibarıyla):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaanca</li>
                    <li>🇦🇱 Arnavutça (Shqip)</li>
                    <li>🇩🇿 Arapça (العربية)</li>
                    <li>🇮🇩 Bali Dili (Basa Bali)</li>
                    <li>🇧🇩 Bengalce (বাংলা)</li>
                    <li>🇲🇲 Birmanca (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Boşnakça (Bosanski)</li>
                    <li>🇧🇬 Bulgarca (Български)</li>
                    <li>🇨🇳 Çince (中文)</li>
                    <li>🇩🇰 Danca (Dansk)</li>
                    <li>🇩🇪 Almanca (Deutsch)</li>
                    <li>🇬🇧 İngilizce (English)</li>
                    <li>🇪🇪 Estonca (Eesti)</li>
                    <li>🇫🇮 Fince (Suomi)</li>
                    <li>🇫🇷 Fransızca (Français)</li>
                    <li>🇬🇷 Yunanca (Ελληνικά)</li>
                    <li>🇮🇱 İbranice (עברית)</li>
                    <li>🇮🇳 Hintçe (हिन्दी)</li>
                    <li>🇭🇷 Hırvatça (Hrvatski)</li>
                    <li>🇭🇺 Macarca (Magyar)</li>
                    <li>🇮🇩 Endonezce (Bahasa Indonesia)</li>
                    <li>🇮🇪 İrlandaca (Gaeilge)</li>
                    <li>🇮🇸 İzlandaca (Íslenska)</li>
                    <li>🇮🇹 İtalyanca (Italiano)</li>
                    <li>🇯🇵 Japonca (日本語)</li>
                    <li>🇰🇭 Khmerce (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korece (한국어)</li>
                    <li>🇱🇦 Laosça (ພາສາລາວ)</li>
                    <li>🇱🇻 Letonca (Latviešu)</li>
                    <li>🇱🇹 Litvanca (Lietuvių)</li>
                    <li>🇱🇺 Lüksemburgca (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malayca (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Moğolca (Монгол)</li>
                    <li>🇳🇵 Nepalce (नेपाली)</li>
                    <li>🇳🇱 Hollandaca (Nederlands)</li>
                    <li>🇳🇴 Norveççe (Norsk)</li>
                    <li>🇦🇫 Peştuca (پښتو)</li>
                    <li>🇮🇷 Farsça (فارسی)</li>
                    <li>🇵🇱 Lehçe (Polski)</li>
                    <li>🇵🇹 Portekizce (Português)</li>
                    <li>🇮🇳 Pencapça (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumence (Română)</li>
                    <li>🇷🇺 Rusça (Русский)</li>
                    <li>🇸🇪 İsveççe (Svenska)</li>
                    <li>🇷🇸 Sırpça (Српски)</li>
                    <li>🇸🇰 Slovakça (Slovenčina)</li>
                    <li>🇸🇮 Slovence (Slovenščina)</li>
                    <li>🇪🇸 İspanyolca (Español)</li>
                    <li>🇹🇿 Svahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalogca (Filipino)</li>
                    <li>🇮🇳 Tamilce (தமிழ்)</li>
                    <li>🇮🇳 Teluguca (తెలుగు)</li>
                    <li>🇹🇭 Tayca (ไทย)</li>
                    <li>🇨🇿 Çekçe (Čeština)</li>
                    <li>🇹🇷 Türkçe (Türkçe)</li>
                    <li>🇺🇦 Ukraynaca (Українська)</li>
                    <li>🇵🇰 Urduca (اردو)</li>
                    <li>🇻🇳 Vietnamca (Tiếng Việt)</li>
                    <li>🇸🇳 Wolofça (Wolof)</li>
                    <li>🇺🇸 Yidiş (ייִדיש)</li>
                    <li>🇿🇦 Zuluca (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Kendi dillerinizi ekleyin:</strong><br>
                Henüz dahil edilmemiş bir dili mi istiyorsunuz? Kendi sözlük dosyanızı (<code>sprache_xx.py</code>) uygulamanın yanına yerleştirmeniz yeterlidir – yazılım bunu otomatik olarak tanır. Belirli bir çeviriyle ilgileniyorsanız, lütfen benimle iletişime geçin.
            </div>

            <p><strong>🙏 Özel teşekkür:</strong> Tüm sözlüklerin 62 dile çevrilmesinde destek sağlayan DeepSeek'e teşekkürler.</p>

            <p>📧 Çeviriler için iletişim: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Hata",
        'error_occurred': "Bir hata oluştu",
        'error_pdf_load': "PDF yüklenirken hata",
        'error_pdf_save': "PDF kaydedilirken hata",
        'error_ocr': "Metin tanıma hatası",
        'error_no_pdf': "PDF yüklenmemiş",
        'error_page_not_found': "Sayfa bulunamadı",
        'error_invalid_range': "Geçersiz sayfa aralığı",
        'error_file_not_found': "Dosya bulunamadı",
        'error_permission': "İzin yok",
        'error_unknown': "Bilinmeyen hata",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Başarılı",
        'success_operation': "İşlem başarıyla tamamlandı",
        'success_saved': "Başarıyla kaydedildi",
        'success_exported': "Başarıyla dışa aktarıldı",
        'success_imported': "Başarıyla içe aktarıldı",
        'success_deleted': "Başarıyla silindi",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Onay",
        'confirm_yes': "Evet",
        'confirm_no': "Hayır",
        'confirm_ok': "Tamam",
        'confirm_cancel': "İptal",
        'confirm_delete': "Sil",
        'confirm_overwrite': "Üzerine yaz",
        'confirm_continue': "Devam et",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF yükleniyor...",
        'progress_saving': "PDF kaydediliyor...",
        'progress_exporting': "PDF dışa aktarılıyor...",
        'progress_processing': "İşlem sürüyor...",
        'progress_wait': "Lütfen bekleyin...",
        'progress_preparing': "Hazırlanıyor...",
        'progress_finalizing': "Sonlandırılıyor...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Beyaz",
        'color_black': "Siyah",
        'color_red': "Kırmızı",
        'color_green': "Yeşil",
        'color_blue': "Mavi",
        'color_yellow': "Sarı",
        'color_magenta': "Eflatun",
        'color_cyan': "Camgöbeği",
        'color_orange': "Turuncu",
        'color_gray': "Gri",
        'color_custom': "Renk seçici",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Dosya",
        'menu_edit': "&Düzen",
        'menu_view': "&Görünüm",
        'menu_tools': "&Araçlar",
        'menu_settings': "&Ayarlar",
        'menu_help': "&Yardım",
        'menu_language': "🌐 Dil",
        'menu_guides': "&Kılavuzlar",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Aç",
        'file_save_as': "&Farklı kaydet...",
        'file_protect': "Belgeyi &koru...",
        'file_export': "&Dışa aktar",
        'file_export_pages': "Pages olarak dışa aktar",
        'file_export_word': "DOCX olarak dışa aktar",
        'file_export_text': "TXT olarak dışa aktar",
        'file_print_now': "&Hemen yazdır",
        'file_print': "&Yazdır",
        'file_close': "&Kapat",
        'file_quit': "&Çık",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Ara",
        'edit_ocr': " OCR çalıştır",
        'edit_rotate': "Sayfayı &döndür",
        'edit_rotate_all': "&Tüm sayfaları döndür",
        'edit_delete_pages': "Sayfaları &sil",
        'edit_extract_pages': "Sayfaları &çıkar",
        'edit_insert_pages': "Sayfa &ekle",
        'edit_move_pages': "Sayfaları &taşı",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Metin ve çarpı ekle",
        'text_insert': " Metin ekle",
        'cross_insert': " Çarpı ekle",
        'text_customize': " Metni ayarla",
        'cross_customize': " Bu çarpıyı ayarla",
        'cross_customize_all': " Tüm çarpıları ayarla",
        'text_discard': " Bu metni/çarpıyı iptal et",
        'text_discard_all': " Tüm metinleri ve çarpıları iptal et",
        'text_save_all': " Tüm metinleri ve çarpıları kaydet",
        'text_guide': " Metin girişi / metin blokları - Kılavuz",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " İmza ekle",
        'signature_settings_menu': " Ayarlar...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Resim ekle",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Şekil ekle",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Metin penceresini göster",
        'view_zoom': "&Yakınlaştır",
        'view_zoom_page': "&Sayfa genişliği (varsayılan)",
        'view_zoom_two': "&İki sayfa",
        'view_zoom_overview': "&Genel bakış (birden çok sayfa)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Erişilebilirlik",
        'settings_voice': "Sesli çıktı",
        'settings_voice_tooltip': "ekran okuyucuların sesli çıktısını ek bilgilerle tamamlar",
        'settings_signature': "&İmza ayarları",
        'settings_password': "&Şifre yöneticisi",
        'settings_backup': "Değişikliklerden önce yedek oluştur",
        'settings_export_import': "&Ayarları dışa aktar / içe aktar",
        'settings_export': "&Tüm ayarları dışa aktar...",
        'settings_import': "&Tüm ayarları içe aktar...",
        'settings_export_info': "&Neler dışa aktarılır?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "açık",
        'voice_off': "kapalı",
        'voice_toggle': "Sesli çıktı {0}",
        'voice_speed': "Hız {0} yüzde",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Araç bulunamadı:\n{0}\n\nBASE_DIR: {1}\nPDF araçlarının {1} dizininde kurulu olduğundan emin olun.",
        'tool_started': "{0} başlatıldı",
        'tool_start_failed': "Başlatılamadı",
        'process_error_failed_to_start': "İşlem başlatılamadı. Dosya mevcut mu?",
        'process_error_crashed': "İşlem başlangıçta çöktü.",
        'process_error_timeout': "İşlem zaman aşımına uğradı.",
        'process_error_write': "İşleme yazma hatası.",
        'process_error_read': "İşlemden okuma hatası.",
        'process_error_unknown': "Bilinmeyen işlem hatası",
        'process_command': "Komut",
        'process_normal_exit': "normal şekilde sonlandı",
        'process_crashed': "çöktü",
        'process_nonzero_exit': "{0} {1} hata koduyla sonlandı",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "İptal ediliyor...",
        'move_cancelling': "Taşıma iptal ediliyor",
        'opening_pdf': "PDF açılıyor...",
        'loading_document': "Belge yükleniyor...",
        'pdf_opened': "PDF açıldı",
        'pages_found_moving': "{0} sayfa bulundu, {1} taşınacak",
        'creating_backup': "Yedek oluşturuluyor...",
        'backup_description': "Orijinal dosya yedekleniyor...",
        'backup_saved_as': "Yedeklendi: {0}",
        'error_format': "Hata: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Arama sıfırlandı",
        'page_header_simple': "=== Sayfa {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Şifre Yöneticisi – Kılavuz",
        'password_guide_voice': "Şifre yönetimi kılavuzu. Lütfen notları okuyun.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Şifre Yöneticisi – Ayrıntılı Kılavuz</strong></p>

        <p><strong>1. PDF'ler için şifre koruması</strong></p>
        <ul>
        <li>Şifre korumalı bir PDF açıldığında, şifreyi girebileceğiniz bir iletişim kutusu görünür.</li>
        <li>Şifreyi şifrelenmiş olarak kaydedebilirsiniz, böylece her seferinde yeniden girmeniz gerekmez ("Şifreyi kaydet" onay kutusu).</li>
        <li>"Şifreyi kaldır" düğmesiyle PDF'nin şifresi çözülmüş bir kopyasını oluşturabilir ve şifreyi veritabanından silebilirsiniz.</li>
        </ul>

        <p><strong>2. Ana şifre</strong></p>
        <ul>
        <li>Ana şifre, kayıtlı tüm PDF şifrelerine erişimi korur.</li>
        <li><strong>Oluşturma:</strong> "Ayarlar → Şifre Yöneticisi → Ana Şifre Ayarları"na gidin ve "Ana şifre oluştur"a tıklayın. Güçlü bir ana şifre seçin (en az 8 karakter).</li>
        <li><strong>Değiştirme:</strong> Başarılı kimlik doğrulamadan sonra ana şifreyi değiştirebilirsiniz.</li>
        <li><strong>Kaldırma:</strong> Ana şifreyi silerseniz, TÜM kayıtlı şifreler geri alınamaz şekilde silinir. Önceden bir yedek dışa aktarabilirsiniz.</li>
        <li>Oturumda bir kez ana şifre ile kimlik doğrulamanız gerekir (örneğin şifreleri görüntülemek gibi korumalı işlevlere erişmek için).</li>
        </ul>

        <p><strong>3. Şifre yöneticisi (liste)</strong></p>
        <ul>
        <li>"Ayarlar → Şifre Yöneticisi" altında, kayıtlı tüm PDF'lerin şifrelenmiş şifreleriyle birlikte bir tablosu açılır.</li>
        <li><strong>Ana şifre olmadan:</strong> Yalnızca girişleri silebilirsiniz – şifreler gizli kalır.</li>
        <li><strong>Ana şifre ile (kimlik doğrulanmış):</strong> Şifreleri görüntüleyebilir, kopyalayabilir, dışa aktarabilir ve silebilirsiniz.</li>
        <li><strong>Dışa aktarma:</strong> Bir biçim seçin (JSON, CSV, TXT) ve listeyi kaydedin. Ana şifre belirlenmişse, şifrelerin düz metin olarak mı yoksa şifrelenmiş olarak mı dışa aktarılacağına karar verebilirsiniz.</li>
        <li><strong>İçe aktarma:</strong> Önceden dışa aktarılmış tüm ayarları (şifreler dahil) içeren bir ZIP dosyası, "Ayarlar → Ayarları dışa aktar/içe aktar" yoluyla yeniden içe aktarılabilir. Dikkat: Mevcut verilerin üzerine yazılır!</li>
        </ul>

        <p><strong>4. Şifre oluşturucu</strong></p>
        <ul>
        <li>Şifre iletişim kutusunda (örneğin bir PDF'yi korurken), giriş alanının sağında bir zar düğmesi 🎲 bulacaksınız.</li>
        <li>Şifre oluşturucuyu açmak için tıklayın. Uzunluk, karakter kümeleri (büyük harf, küçük harf, rakam, sembol) ve daha iyi okunabilirlik için ayraç ayarlayabilirsiniz.</li>
        <li>Oluşturulan şifre doğrudan kullanılabilir ve gerekiyorsa kopyalanabilir.</li>
        </ul>

        <p><strong>5. Önemli güvenlik notları</strong></p>
        <ul>
        <li>Kayıtlı şifreler AES-256 ile şifrelenmiş olarak saklanır. Anahtar, ana şifrenizden (varsa) veya sabit bir değerden (ana şifre yoksa) türetilir.</li>
        <li>Ana şifre olmadan şifreler şifrelenmiş olsa da, anahtar programa gömülüdür – dosyalarınıza erişimi olan bir saldırgan bunları çözebilir. Bu nedenle bir ana şifre kullanmanızı şiddetle tavsiye ederiz.</li>
        <li>Şifre veritabanı `Data/passwords.json` dizininde bulunur. Özellikle ana şifreyi kaldırmadan önce düzenli yedekleme yapın.</li>
        <li>Ana şifre kaybolursa, kayıtlı tüm şifreler geri alınamaz şekilde kaybolur.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Ters çevirme modu",
        'invert_mode_classic': "Klasik (tüm renkleri ters çevir)",
        'invert_mode_smart': "Akıllı (yalnızca parlaklığı ters çevir)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Gri ton eşiği",
        'gray_threshold_10': "%10 (katı)",
        'gray_threshold_20': "%20",
        'gray_threshold_30': "%30 (Varsayılan)",
        'gray_threshold_40': "%40",
        'gray_threshold_50': "%50 (yumuşak)",
        'threshold_changed': "Eşik %{0} olarak ayarlandı",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Gri ton eşiği – Açıklama",
        'threshold_guide_text': "Gri ton eşiği, akıllı karanlık modda hangi piksellerin 'gri' olarak kabul edildiğini ve ters çevrildiğini belirler.\n\n"
                                "• Düşük değer (%10) yalnızca neredeyse mükemmel gri tonlarını ters çevirir – renkli öğeler tamamen korunur.\n"
                                "• Yüksek değer (%50) hafif renkli pikselleri de ters çevirir – bu kontrastı artırır, ancak renkleri bozabilir.\n\n"
                                "Optimum değer belgeye bağlıdır. Salt metin belgeleri için %30–40 genellikle idealdir, renkli grafikler için %10–20 daha uygundur.\n\n"
                                "Değeri 'Ayarlar' menüsü üzerinden istediğiniz zaman ayarlayabilirsiniz – PDF hemen yeniden yüklenecektir.\n\n"
                                "Not:\n* Fotoğraflar ve resimler yalnızca açık modda doğru görüntülenebilir!\n* Ters çevirme ayarları yalnızca karanlık mod etkinleştirildiğinde gösterilir.",
        'threshold_guide_voice': "Gri ton eşiği, akıllı karanlık modun ne kadar müdahale ettiğini belirler. Düşük değer renkleri korur, yüksek değer kontrastı artırır.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF açılıyor...",
        'progress_loading_document': "Belge yükleniyor...",
        'progress_pdf_opened': "PDF açıldı",
        'progress_creating_backup': "Yedek oluşturuluyor...",
        'progress_backup_description': "Orijinal dosya güvence altına alınıyor...",
        'progress_backup_created': "Yedek oluşturuldu",
        'progress_backup_saved_as': "{0} olarak kaydedildi",
        'progress_analyzing_start': "Analiz başlatılıyor...",
        'progress_searching_empty': "Boş sayfalar aranıyor...",
        'progress_page_empty': "{0}. sayfa boş",
        'progress_page_keep': "{0}. sayfayı tut",
        'progress_analysis_complete': "Analiz tamamlandı",
        'progress_empty_found': "{0} boş sayfa bulundu",
        'progress_current_page': "Geçerli sayfa",
        'progress_mark_delete': "Silinmek üzere işaretleniyor",
        'progress_range_selected': "Sayfa aralığı {0}-{1}",
        'progress_deleting_pages': "{0} sayfa siliniyor",
        'progress_creating_new_pdf': "Yeni PDF oluşturuluyor...",
        'progress_transferring_pages': "Sayfalar aktarılıyor",
        'progress_keeping_page': "{0}. sayfa tutulacak ({1}/{2})",
        'progress_saving_pdf': "PDF kaydediliyor...",
        'progress_optimizing': "Dosya boyutu optimize ediliyor...",
        'progress_finalizing': "Sonlandırılıyor...",
        'progress_new_size': "Yeni boyut: {0:.2f} MB",
        'progress_cancelling': "İptal ediliyor...",
        'progress_cancel_message': "{0} iptal ediliyor",
        'progress_pages_found_moving': "{0} sayfa bulundu, {1} taşınacak",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF analiz ediliyor...",
        'ocr_status_optimizing': "Görüntü optimizasyonu sürüyor...",
        'ocr_status_recognizing': "Metin tanıma sürüyor...",
        'ocr_status_embedding': "Metin gömülüyor...",
        'ocr_status_finalizing': "PDF sonlandırılıyor...",

        # PDF-Laden
        'progress_preparing': "Hazırlanıyor...",
        'progress_loading': "PDF yükleniyor...",

        # Seitenoperationen
        'progress_deleting_title': "Sayfalar siliniyor...",
        'progress_moving_title': "Sayfalar taşınıyor...",
        'pages_found': "Sayfalar bulundu",
        'progress_creating_new_order': "Yeni sıra oluşturuluyor...",
        'progress_sorting_pages': "Sayfalar sıralanıyor...",
        'progress_moving_to_begin': "{0} sayfayı başa taşı",
        'progress_transferring_count': "{0} sayfayı aktar",
        'progress_transferring_before_target': "Sayfaları hedefin önüne aktar",
        'progress_moving_pages': "{0} sayfayı taşı",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_yedek_",
        'filename_protected_suffix': "_korumali_",
        'filename_copy_suffix': "_Kopya",
        'filename_page_single': "_Sayfa_",
        'filename_page_range': "_Sayfalar_",
        'filename_export_page': "_Sayfa_{0:03}",
        'filename_export_range': "_Sayfalar_{0}-{1}",
        'filename_export_multiple': "_Sayfalar_{0}",
        'filename_with_text': "_metinli",
        'filename_with_signature': "_imzali",
        'filename_with_image': "_resimli",
        'filename_with_forms': "_sekilli",
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
        'view_toggle_navbar': "Buton çubuğunu göster",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Tüm sayfalar silinemez",
		'pages_cannot_delete_last_page': 'Son sayfa silinemez!',
		'pages_cannot_delete_all_pages': 'Belgede en az bir sayfa kalmalıdır!',
		'delete_pages_confirm': '{0} sayfayı silmek istediğinizden emin misiniz?',
		'delete_pages_confirm_voice': '{0} sayfayı silmek istediğinizden emin misiniz?',
		'pages_deleted': '{0} sayfa başarıyla silindi.',
		'warning': 'Uyarı',
		'error': 'Hata',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Form seçilmedi",
        'form_customized': "Form özelleştirildi",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Seç",
        'btn_use': "Kullan",
        'master_password_for_spasswords': "Şifreleri saklamak ve kullanmak için önce bir ana şifre oluşturmalısınız.\n\nAna şifreyi şimdi oluşturmak istiyor musunuz?",
        'open_saved_dialog_title': "Kaydedilmiş dosyayı aç",
        'open_saved_question': "Kaydedilmiş dosyayı şimdi açmak istiyor musunuz?",
        'password': "Şifre",
        'password_manager_master_required': "Şifre yöneticisi yalnızca bir ana şifre oluşturulmuşsa kullanılabilir.\n\nAna şifreyi şimdi oluşturmak istiyor musunuz?",
        'password_master_required_for_select': "Kaydedilmiş şifreleri görüntülemek ve seçmek için önce ana şifrenizle kimlik doğrulamanız gerekir.\n\nŞimdi kimlik doğrulamak istiyor musunuz?",
        'password_not_available': "Seçilen şifre mevcut değil veya şifresi çözülemedi.",
        'password_options_title': "Şifre seçenekleri",
        'password_save_choice_change': "Yeni şifre belirle",
        'password_save_choice_keep': "Mevcut şifreyi kullan",
        'password_save_choice_none': "Şifrelemeden kaydet",
        'password_save_hint': "Şifreleri güvenli bir şekilde saklamak için önce bir ana şifre oluşturun.",
        'password_save_master_required': "Şifreyi kaydet (yalnızca ana şifreyle mümkün)",
        'password_save_question': "Geçerli PDF şifre korumalı. Mevcut şifreyi kullanmak mı, yeni bir şifre belirlemek mi yoksa şifrelemeden kaydetmek mi istiyorsunuz?",
        'password_select': "Şifre seç",
        'password_select_none': "Hiçbir şifre seçilmedi.\n\nLütfen listeden bir şifre seçin.",
        'password_select_one': "Lütfen tam olarak bir şifre seçin.\n\nBirden fazla şifre işaretlediniz.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_yedek",
        'filename_insert_suffix': "_eklemeli",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_sayfalar_silindi",
        'filename_pages_moved': "_sayfalar_tasindi",
        'filename_rotated_all_suffix': "_tum_sayfalar_donduruldu",
        'filename_rotated_suffix': "_sayfa_donduruldu",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "PDF değiştirilirken dosya adlarının yapılandırılması",
        'filename_keep_suffixes': "Önceki ekleri koru (ör. _metinli)",
        'filename_keep_suffixes_false': "Değiştir",
        'filename_keep_suffixes_true': "Koru",
        'filename_preview_label': "Dosya adı önizlemesi:",
        'filename_preview_overwrite_hint': "Önizleme mevcut değil – orijinalin üzerine yazılacak.",
        'filename_separator': "Kelimeler arası ayırıcı",
        'filename_separator_none': "Ayırıcı yok",
        'filename_separator_space': "Boşluk ( )",
        'filename_separator_underscore': "Alt çizgi (_)",
        'filename_settings_saved': "Dosya adı ayarları kaydedildi",
        'filename_settings_title': "Dosya adı biçimlendirme ve yedekleme",
        'filename_timestamp_position': "Zaman damgasının konumu",
        'filename_timestamp_position_after': "Temel addan sonra",
        'filename_timestamp_position_before': "En önde",
        'filename_timestamp_position_end': "Sonda",
        'filename_use_timestamp': "Zaman damgası kullan",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Değişikliklerde davranış:</b><ul><li>Sayfaları silme ve ekleme</li><li>Metin, imza, resim ve şekil ekleme</li><li>OCR</li></ul></html>",
        'backup_section': "Sayfa işlemleri için yedekleme (Sil, Taşı)",
        'behavior_info': "Not: 'Orijinalin üzerine yaz'da zaman damgaları ve ekler yoksayılır – dosya adını korur.",
        'behavior_new_file': "Her zaman yeni dosya oluştur (zaman damgası ve ek ile)",
        'behavior_overwrite': "Orijinalin üzerine yaz (yeni dosya yok)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Tüm sayfalar döndürüldü.\n\nOrijinal değişmeden kaldı.\nYeni dosya: {0}",
        'all_pages_rotated_voice': "Tüm sayfalar döndürüldü, yeni dosya oluşturuldu.",
        'empty_pages_deleted_new_file': "{0} boş sayfa silindi.\n\nOrijinal değişmeden kaldı.\nYeni dosya: {1}",
        'empty_pages_deleted_voice': "{0} boş sayfa silindi, yeni dosya oluşturuldu.",
        'ocr_keep_original': "Orijinali koru (daha sonra manuel olarak aç)",
        'ocr_new_file_question': "Yeni aranabilir PDF şuraya kaydedildi:\n{0}\n\nŞimdi açmak istiyor musunuz?",
        'ocr_open_new': "Yeni OCR dosyasını aç",
        'ocr_original_kept': "Orijinal dosya açık kalır. OCR dosyası kaydedildi.",
        'page_deleted_new_file': "Sayfa {0} silindi.\n\nOrijinal değişmeden kaldı.\nYeni dosya: {1}",
        'page_deleted_voice': "Sayfa {0} silindi, yeni dosya oluşturuldu.",
        'page_rotated_new_file': "Sayfa {0} döndürüldü.\n\nOrijinal değişmeden kaldı.\nYeni dosya: {1}",
        'page_rotated_voice': "Sayfa {0} döndürüldü, yeni dosya oluşturuldu.",
        'pages_deleted_new_file': "{0} sayfa silindi.\n\nOrijinal dosya değişmeden kaldı.\nYeni dosya: {1}",
        'pages_deleted_new_file_voice': "{0} sayfa silindi, yeni dosya oluşturuldu.",
        'pages_inserted_new_file': "{0} sayfa eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni dosya: {1}",
        'pages_inserted_new_file_ask': "{0} sayfa eklendi.\n\nOrijinal değişmeden kaldı.\nYeni dosya: {1}\n\nŞimdi açmak istiyor musunuz?",
        'pages_inserted_voice_new': "{0} sayfa eklendi, yeni dosya oluşturuldu.",
        'pages_moved_new_file': "{0} sayfa taşındı.\n\nOrijinal dosya değişmeden kaldı.\nYeni dosya: {1}",
        'pages_moved_new_file_voice': "{0} sayfa taşındı, yeni dosya oluşturuldu.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Bir daha gösterme",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Yedekleme ayarı</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Yedekleme AÇIK</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Orijinalin üzerine yazan tüm değişikliklerde</strong> (metin, imza, resim, şekil, OCR, döndürme, ekleme, sayfaları silme/taşıma) değişiklik uygulanmadan önce <strong>otomatik olarak zaman damgalı bir yedek oluşturulur</strong>.</p>
                <p style="margin: 5px 0 5px 20px;">• Yedek, orijinal dosyanın yanında bulunur (ör. <code>Belge_yedek_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ayrıca <strong>„Orijinalin üzerine yaz“</strong> seçeneğini etkinleştirdiyseniz, yine bir yedek oluşturulur.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Yedekleme KAPALI</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Hiçbir yedek oluşturulmaz</strong> – ne üzerine yazarken ne de sayfa işlemlerinde.</p>
                <p style="margin: 5px 0 5px 20px;">• Orijinal dosya, üzerine yazarken geri dönüşü olmayacak şekilde kaybolabilir.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Yalnızca deneyimli kullanıcılar için önerilir!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>İpucu:</strong> Yedekleme ayarı, „Orijinalin üzerine yaz“ seçeneğinden bağımsızdır. İkisini birleştirebilirsiniz.<br>
                Bu mesajı kalıcı olarak gizleyebilirsiniz.
            </div>
        </div>
        """,
        'backup_info_title': "Yedekleme davranışı",
        'backup_info_voice': "Sayfa işlemlerinde yedekleme davranışı hakkında bildirim. Yedekleme AÇIK orijinalin üzerine yazar, KAPALI yeni dosya oluşturur.",
        'show_backup_info': "Yedekleme ayarı hakkında bilgi",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Bir daha gösterme",
        'overwrite_enable_backup': "Yedeklemeyi etkinleştir (önerilir)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Orijinalin üzerine yaz</p>
            <p>Bu seçeneği etkinleştirirseniz, değişiklikler (metin, imza, resim, şekil, OCR, döndürme, ekleme) <strong>doğrudan orijinalin üzerine kaydedilir</strong> – <strong>yeni dosya oluşturulmaz</strong>.</p>
            <p>• Dosya adı değişmeden kalır.<br>
            • Zaman damgaları ve ekler yoksayılır.<br>
            • <strong>Yedek olmadan orijinal geri dönüşü olmayacak şekilde kaybolabilir.</strong></p>
            <p style="color: #FFD700;">Öneri: Otomatik yedekler almak için ek olarak yedekleme seçeneğini etkinleştirin.</p>
        </div>
        """,
        'overwrite_info_title': "Orijinalin üzerine yaz",
        'overwrite_info_voice': "Uyarı: Orijinalin üzerine yaz – yeni dosya yok. Yedekleme önerilir.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} sayfa eklendi.\n\nOrijinal dosyanın üzerine yazıldı.\nBir yedek oluşturuldu.",
        'pages_inserted_overwrite_no_backup': "{0} sayfa eklendi.\n\nOrijinal dosyanın üzerine yazıldı.\nHiçbir yedek oluşturulmadı.",
        'texts_saved_overwrite_with_backup': "Değişiklikler orijinalin üzerine kaydedildi.\n\nBir yedek oluşturuldu.",
        'texts_saved_overwrite_no_backup': "Değişiklikler orijinalin üzerine kaydedildi.\n\nHiçbir yedek oluşturulmadı.",
        'texts_crosses_saved_new_file': "{0} {1} ve {2} {3} eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",
        'texts_saved_new_file': "{0} {1} eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",
        'crosses_saved_new_file': "{0} {1} eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",
        'elements_saved_new_file': "{0} öğe eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",
        'signatures_saved_overwrite_with_backup': "İmza(lar) orijinalin üzerine kaydedildi.\n\nBir yedek oluşturuldu.",
        'signatures_saved_overwrite_no_backup': "İmza(lar) orijinalin üzerine kaydedildi.\n\nHiçbir yedek oluşturulmadı.",
        'images_saved_overwrite_with_backup': "Resim(ler) orijinalin üzerine kaydedildi.\n\nBir yedek oluşturuldu.",
        'images_saved_overwrite_no_backup': "Resim(ler) orijinalin üzerine kaydedildi.\n\nHiçbir yedek oluşturulmadı.",
        'forms_saved_overwrite_with_backup': "Şekil(ler) orijinalin üzerine kaydedildi.\n\nBir yedek oluşturuldu.",
        'forms_saved_overwrite_no_backup': "Şekil(ler) orijinalin üzerine kaydedildi.\n\nHiçbir yedek oluşturulmadı.",
        'signatures_saved_new_file': "{0} imza eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",
        'images_saved_new_file': "{0} resim eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",
        'forms_saved_new_file': "{0} şekil eklendi.\n\nOrijinal dosya değişmeden kaldı.\nYeni bir dosya oluşturuldu.\n\nYeni PDF yükleniyor...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Uyarı: Bu PDF döndürülmüş sayfalar içeriyor. Konumlandırma farklı olabilir.",
        'page_rotated_warning_title': "Döndürülmüş sayfa algılandı",
        'page_rotated_warning_message': "Geçerli sayfa {0} {1}° döndürülmüş.\n\nDöndürülmüş sayfalara öğe ekleme desteklenmiyor.\n\nSayfayı şimdi dik konuma döndürmek istiyor musunuz?",
        'page_rotated_warning_voice': "Uyarı: Sayfa döndürülmüş. Lütfen önce döndürün.",
        'paste_on_rotated_page_simple_warning': "Sayfa {0} üzerine ekleme mümkün değil!\n\nBu sayfa {1}° döndürülmüş.\n\nLütfen önce sayfayı 0°'ye döndürün (Menü: Düzenle → Sayfayı hizala).\n\nUyarı:\nSayfayı döndürmeden önce kaydetmezseniz, önceden kopyalanan öğe kaybolur.",
        'paste_on_rotated_page_voice': "Ekleme iptal edildi. Sayfa döndürülmüş. Lütfen önce sayfayı hizalayın.",
        'page_rotated_cancel': "İptal",
        'page_rotated_rotate_until_upright': "Sayfayı tekrar tekrar döndür (dik olana kadar)",
        'page_rotated_now_upright': "Sayfa artık dik konumda. Artık ekleyebilirsiniz.",
        'page_rotated_still_not_upright': "Sayfa dik konuma döndürülemedi. Lütfen manuel olarak düzeltin.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Yardım: Döndürülmüş sayfaları düzeltme",
        'help_rotated_pages_voice': "Döndürülmüş sayfaları düzeltme yardımı açılıyor.",
        'btn_help': "Yardım",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Sorun: Döndürülmüş sayfa – Ekleme doğru çalışmıyor</p>

            <p>Döndürülmüş bir sayfaya metin, imza veya şekil ekleme düzgün çalışmıyorsa, sayfayı harici bir PDF düzenleyici ile düzeltebilirsiniz.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Harici araçla çözüm (ör. macOS Önizleme)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Sayfayı dışa aktar</strong><br>
                &nbsp;&nbsp;Menüde <strong>Dosya → Sayfa olarak dışa aktar</strong> seçeneğine tıklayın veya istenen sayfayı tek bir PDF olarak kaydetmek için başka bir yöntem kullanın.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Sayfayı harici programda aç</strong><br>
                &nbsp;&nbsp;Dışa aktarılan PDF'yi bir PDF düzenleyicide açın (ör. <strong>macOS Önizleme</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Sayfayı döndür</strong><br>
                &nbsp;&nbsp;Sayfayı dik olacak şekilde döndürün (Önizleme'de: <strong>Araçlar → Döndür</strong> veya <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Kaydet</strong><br>
                &nbsp;&nbsp;Düzeltilmiş sayfayı kaydedin (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Sayfayı orijinal belgeye geri ekle</strong><br>
                &nbsp;&nbsp;PDFDarkView'e dönün ve düzeltilmiş sayfayı istenen konuma ekleyin:<br>
                &nbsp;&nbsp;<strong>Düzenle → Sayfa ekle</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatif: Sayfayı orijinalde döndür</p>
                <p style="margin: 5px 0 5px 20px;">• Yerleşik döndürme işlevini kullanın (<strong>Düzenle → Sayfayı döndür</strong>) sayfayı adım adım düzeltmek için.<br>
                • Her döndürmeden sonra eklemenin artık çalışıp çalışmadığını kontrol edebilirsiniz.<br>
                • Bu genellikle daha hızlı çözümdür – önce bunu deneyin!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>İpucu:</strong> Döndürülmüş sayfalarla sık sık karşılaşıyorsanız, ekleme iletişim kutusundaki uyarıyı kalıcı olarak gizleyebilirsiniz.<br>
                Konumlandırma daha sonra farklı olabilir – bu seçeneği yalnızca sonuçlarını biliyorsanız kullanın.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Sayfaları hizala",
        'menu_rotate_normalize_tooltip': "Sayfayı döndür veya 0°'ye sıfırla",
        'normalize_current_page': "Geçerli sayfayı dik konuma getir (0°'ye ayarla)",
        'normalize_all_pages': "Tüm sayfaları dik konuma getir (0°'ye ayarla)",
        'page_normalized': "Sayfa {0} dik konuma ayarlandı.",
        'all_pages_normalized': "Tüm sayfalar dik konuma ayarlandı.",
        'page_already_upright': "Sayfa {0} zaten dik.",
        'all_pages_already_upright': "Tüm sayfalar zaten dik.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF aranabilir metin içermiyor.</p><p>{0} dosyasına dışa aktarmak için OCR yapmak istiyor musunuz?</p>",
        'export_ocr_voice': "PDF metin içermiyor. {0} dosyasına dışa aktarmak için OCR gerekli.",
        'export_no_ocr_possible': "OCR olmadan dışa aktarma mümkün değil. Lütfen menü üzerinden OCR yapın.",
        'ocr_failed_export_not_possible': "OCR başarısız oldu. Dışa aktarma gerçekleştirilemiyor.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF Önizleme'de açılacaktır. Lütfen yazdırma işlemini orada başlatın.",
        'print_preview_manual': "PDF açıldı. Lütfen yazdırma komutunu manuel olarak yürütün (ör. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF'leri birleştir",
        'merge_pdfs': "PDF'leri birleştir",
        'merge_progress_title': "PDF'ler birleştiriliyor...",
        'merge_pdfs_list': "Sırayla PDF'ler (Sıralamak için sürükle ve bırak)",
        'merge_add_pdf': "PDF ekle",
        'merge_remove': "Kaldır",
        'merge_move_up': "Yukarı",
        'merge_move_down': "Aşağı",
        'merge_pdfs_info': "💡 İpucu: Sürükle ve bırakarak sırayı değiştirebilirsiniz",
        'merge_no_pdfs': "Hiçbir PDF seçilmedi. 'PDF ekle'ye tıklayın.",
        'merge_info': "{0} PDF seçildi (yaklaşık {1} sayfa)",
        'merge_open_file': "Dosyayı aç",
        'merge_merge': "Birleştir",
        'merge_error': "Birleştirme sırasında hata",
        'merge_min_two_pdfs_error': "Lütfen birleştirmek için en az iki PDF dosyası seçin.",
        'merge_select_pdfs': "Birleştirilecek PDF'leri seçin",
        'merge_error_file': "İşleme sırasında hata",
        'merge_cancelled': "Birleştirme iptal edildi",
        'merge_preparing': "Hazırlanıyor...",
        'merge_processing': "PDF {0} / {1} işleniyor",
        'merge_saving': "Birleştirilmiş PDF kaydediliyor...",
        'merge_complete': "Tamamlandı!",
        'merge_success_title': "Birleştirme başarılı",
        'merge_success_voice': "{0} PDF başarıyla birleştirildi.",
        'merge_success_message': "{0} PDF başarıyla birleştirildi.\n\nYeni belge artık {1} sayfadır.\n\nYeni dosya:\n{2}\n\nKaydetme konumu:\n{3}\n{2}\n\nBu PDF'yi açmak istiyor musunuz?",
        'replace_file_title': "Dosya değiştirilsin mi?",
        'replace_file_message': "Zaten açık bir PDF var. Yeni dosyayla değiştirmek istiyor musunuz?",
        'btn_yes': "Evet",
        'btn_no': "Hayır",
        'filename_merge_suffix': "birlestirilmis",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} açılıyor...",
        'progress_merge_reading': "{0} okunuyor...",
        'progress_merge_adding': "{0} sayfa ekleniyor...",
        'progress_merge_optimizing': "PDF optimize ediliyor...",
        'progress_merge_writing': "PDF yazılıyor...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF'yi kapatma",
        'action_close_window': "pencereyi kapatma",
        'action_open_new_pdf': "yeni bir PDF açma",
        'action_quit_app': "uygulamadan çıkma",
        'changes_saved': "Değişiklikler kaydedildi.",
        'file_close_title': "PDF dosyasını kapat",
        'save_before_action': "Değişiklikler {0} öncesinde kaydedilmeli mi? Evet veya Hayır?",
        'save_before_action_voice': "Değişiklikler {0} öncesinde kaydedilmeli mi? Evet veya Hayır?",
        'save_before_close_question': "Kapatmadan önce değişiklikler kaydedilmeli mi? Evet veya Hayır?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Aranabilir PDF oluşturuldu:\n\n{0}\n\n<b>gerekirse tekrar deneyin",
        "ocr_rotate_title": "OCR öncesi sayfaları hizala",
        "ocr_rotate_question": "PDF döndürülmüş sayfalar içeriyor.\nOCR öncesi tüm sayfaları 0°'ye hizalamak istiyor musunuz?\nBu, metin tanımayı önemli ölçüde iyileştirir.",
        "ocr_rotate_yes": "Evet, hizala",
        "ocr_rotate_no": "Hayır, OCR'yi doğrudan başlat",
        "ocr_rotate_voice": "PDF döndürülmüş sayfalar içeriyor. OCR öncesi tüm sayfalar hizalanmalı mı?",
        "ocr_not_performed_message": "Metin yok. Lütfen OCR yapın (menü \"Düzenle\" → \"OCR Yap\" veya Ctrl+R tuşu).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR Ayarları",
        "ocr_language_btn": "OCR dili seç",
        "ocr_language": "OCR dili(leri)",
        "ocr_language_current": "Geçerli dil:",
        "ocr_param_info": "Parametre hakkında bilgi",

        "ocr_force_ocr_label": "OCR'yi zorla",
        "ocr_deskew_label": "Eğikliği düzelt",
        "ocr_clean_label": "Görüntüyü temizle",
        "ocr_oversample_label": "Çözünürlük (DPI)",
        "ocr_pagesegmode_label": "Sayfa bölümleme",
        "ocr_oem_label": "OCR motor modu",
        "ocr_optimize_label": "PDF sıkıştırma",
        "ocr_jobs_label": "Paralel işlemler",
        "ocr_verbose_label": "Günlük ayrıntısı",

        "ocr_force_ocr_tooltip": "Metin zaten var olsa bile her sayfada OCR'yi zorla",
        "ocr_deskew_tooltip": "Eğik taramaları otomatik olarak hizala",
        "ocr_clean_tooltip": "Görüntüden gürültü ve yapaylıkları kaldır",
        "ocr_oversample_tooltip": "OCR öncesi görüntüyü bu DPI'ya yükselt",
        "ocr_pagesegmode_tooltip": "Sayfanın metin alanlarına nasıl bölüneceğini belirler",
        "ocr_oem_tooltip": "Tesseract'ın OCR motorunu seçer",
        "ocr_optimize_tooltip": "Çıktı PDF'in sıkıştırma seviyesi",
        "ocr_jobs_tooltip": "Paralel OCR işlemlerinin sayısı",
        "ocr_verbose_tooltip": "Günlük çıktısının ayrıntı düzeyi",
        "ocr_settings_explain_btn": "Açıklama",

        "ocr_force_ocr_explain": "<b>Her</b> sayfada metin tanımayı zorlar (zaten metin içerse bile).\n\nÖneri: Taranmış PDF'ler için <b>Açık</b>, zaten mevcut metni olan yerel PDF'ler için <b>Kapalı</b>.",

        "ocr_deskew_explain": "Hafif eğik taramaları düzeltir (yaklaşık 5°'ye kadar).\n\nÖneri: Taranmış belgeler için <b>Açık</b>, sayfalar zaten mükemmel düz ise <b>Kapalı</b>.",

        "ocr_clean_explain": "Görüntüden gürültüyü, noktaları ve küçük yapaylıkları kaldırır.\n<b>ÖNEMLİ:</b> Diyakritik işaretleri (harflerin üstünde/altında noktalar) bulunan Arapça, Tayca veya Vietnamca metinler için bu seçenek <b>devre dışı bırakılmalıdır</b>, aksi takdirde önemli karakterler kaybolabilir.",

        "ocr_oversample_explain": "Görüntüyü <b>metin tanımadan önce</b> belirtilen DPI'ya yükseltir.<br><br>• <b>72-150 DPI:</b> Çok hızlı, ancak düşük tanıma oranı<br>• <b>200-300 DPI:</b> Optimum aralık (Varsayılan: 300)<br>• <b>400+ DPI:</b> Neredeyse hiç daha iyi tanıma yok, ancak önemli ölçüde daha büyük dosyalar<br><br>Öneri: Karmaşık yazılar için 300 DPI (Arapça, Çince, Japonca), Batı dilleri için 200 DPI.",

        "ocr_pagesegmode_explain": "Tesseract'ın sayfayı metin alanlarına nasıl böleceğini belirler.\n\n• <b>3 - Otomatik (Varsayılan):</b> Karma düzenler için iyidir\n• <b>4 - Tek sütun:</b> Tek sütunlu metinler için\n• <b>5 - Dikey blok:</b> Dikey yazılar için (Japonca, Çince)\n• <b>6 - Tekdüze metin bloğu:</b> Sütunsuz akan metin için idealdir\n• <b>11 - Ham görüntü:</b> Kötü taramalar / el yazısı için\n\nÖneri: Basit metin belgeleri için <b>6</b>, karmaşık düzenler için <b>3</b>.",

        "ocr_oem_explain": "Tesseract'ın OCR motorunu seçer.\n\n• <b>0 - Legacy:</b> Eski motor (hızlı, ancak daha az hassas)\n• <b>1 - LSTM:</b> Sinirsel motor (daha yavaş, ancak daha hassas)\n• <b>2 - Legacy + LSTM:</b> Her iki sonucu birleştirir\n• <b>3 - Varsayılan (LSTM tercih edilir):</b> Çoğu durum için en iyi seçim\n\nÖneri: Maksimum tanıma doğruluğu için <b>3</b>.",

        "ocr_optimize_explain": "Çıktı PDF'ini sıkıştırır.\n\n• <b>0:</b> Optimizasyon yok (en hızlı işlem)\n• <b>1:</b> Hafif optimizasyon (iyi uzlaşma)\n• <b>2:</b> Orta düzey optimizasyon\n• <b>3:</b> Güçlü optimizasyon (en küçük dosya, ancak daha yavaş)\n\nÖneri: Günlük kullanım için <b>1</b>.",

        "ocr_jobs_explain": "OCR için paralel işlem sayısı.\n\n• <b>1:</b> Yavaş, ancak en düşük bellek tüketimi\n• <b>4-8:</b> Modern çok çekirdekli işlemciler için optimum\n• <b>12+:</b> Yüksek bellek kullanımıyla neredeyse daha hızlı işlem\n\nÖneri: CPU çekirdek sayısı (ör. 4 çekirdekli sistemlerde <b>4</b>).",

        "ocr_verbose_explain": "Konsoldaki günlük çıktısının ayrıntı düzeyi.\n\n• <b>0:</b> Çıktı yok\n• <b>1:</b> İlerleme ve durum mesajları\n• <b>2:</b> Ayrıntılı çıktı\n• <b>3:</b> Tam hata ayıklama çıktısı (çok kapsamlı)\n\nÖneri: Normal işlem için <b>1</b>.",

        "ocr_reset_title": "Ayarlar sıfırlandı",
        "ocr_reset_message": "Tüm OCR ayarları varsayılan değerlere sıfırlandı.",
        "info_tooltip": "Bu parametre hakkında daha fazla bilgi",
        "ocr_reset_defaults": "Varsayılana sıfırla",

        "ocr_psm_0": "Otomatik (Legacy motor)",
        "ocr_psm_1": "Otomatik sütun algılama",
        "ocr_psm_3": "Otomatik (Varsayılan)",
        "ocr_psm_4": "Tek sütun",
        "ocr_psm_5": "Dikey blok",
        "ocr_psm_6": "Tekdüze metin bloğu",
        "ocr_psm_7": "Tek metin satırı",
        "ocr_psm_8": "Tek kelime",
        "ocr_psm_11": "Ham görüntü (düzen analizi yok)",

        "ocr_oem_0": "Legacy motor (hızlı)",
        "ocr_oem_1": "LSTM motoru (sinirsel, hassas)",
        "ocr_oem_2": "Legacy + LSTM birleştirilmiş",
        "ocr_oem_3": "Varsayılan (LSTM tercih edilir)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR dili(leri)...",
        "ocr_language_title": "OCR dili(leri) seçin",
        "ocr_language_instruction": "Metin tanıma (OCR) için dili(leri) seçin.\nDikkat: Birden fazla dil, performans ve doğruluk pahasına gelir!\nYalnızca bir dil seçerseniz en iyi sonuçları elde edersiniz.",
        "ocr_language_predefined": "Önceden tanımlanmış kombinasyonlar",
        "ocr_language_custom": "Özel...",
        "ocr_language_selected": "Seçilen OCR dilleri",
        "ocr_language_changed": "OCR dili {0} olarak değiştirildi",
        "ocr_language_auto_detect": "Mevcut diller otomatik olarak algılanır.",
        "ocr_language_none_found": "Tesseract dil verisi bulunamadı! Lütfen dil paketlerini kurun (ör. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Özel dil seçimi",
        "ocr_language_available": "Mevcut diller (kurulu):",
        "ocr_language_select_hint": "Bir veya daha fazla dil seçin:",
        "ocr_language_confirm": "Uygula",
        "ocr_language_reset": "Varsayılana sıfırla (deu+eng+vie)",
        "ocr_language_priorities": "Önerilen diller (önceden kurulmuş):",

        "select_all_languages": "Tümünü seç",
        "clear_all_languages": "Seçimi temizle",
        "install_language_packs": "Eksik dil paketlerini yükle...",
        "install_hint": "💡 İpucu: Sisteminizde tüm diller kurulu değildir. Bu düğme aracılığıyla kurulum için yardım alacaksınız.",
        "ocr_language_install_title": "Tesseract dil paketlerinin kurulumu",

        "ocr_missing_languages": "Eksik OCR dil paketleri",
        "ocr_missing_languages_message": "Aşağıdaki seçili diller sisteminizde kurulu değil:\n\n{0}\n\nLütfen eksik dil paketlerini kurun ('Kurulum yardımı' altındaki yardıma bakın).\n\nKurulum yardımını şimdi açmak istiyor musunuz?",
        "ocr_missing_languages_voice": "Eksik dil paketleri. Lütfen eksik dilleri kurun.",
        "ocr_install_help_now": "Yardımı aç",
        "ocr_continue_anyway": "Yine de dene",
        "ocr_language_error_title": "OCR dili hatası",
        "ocr_language_error_message": "Metin tanıma sırasında hata: {0}\n\nLütfen OCR dili ayarlarınızı kontrol edin (Ayarlar → OCR dili).",
        "ocr_install_help_button": "Kurulum yardımı",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract dil paketlerini yükleyin</p>

        <p>OCR'nin belirli bir dilde çalışması için, ilgili dil verilerinin sisteminizde kurulu olması gerekir. İşletim sisteminiz için talimatları izleyin:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>Terminal</strong>'i açın (Finder → Programlar → Yardımcı Programlar → Terminal).</li>
        <li>Mevcut tüm dilleri şununla yükleyin:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Bu birkaç dakika sürebilir.)</li>
        <li>Veya yalnızca tek tek diller (ör. Vietnamca):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Mevcut Homebrew sürümlerinde, <code>*.traineddata</code> dosyasını manuel olarak indirmeniz gerekebilir (aşağıya bakın).</li>
        <li>Kurulumdan sonra: Bu iletişim kutusunu kapatın ve OCR dili seçimini yeniden açın – yeni diller otomatik olarak görünecektir.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Bir terminal açın (Ctrl+Alt+T).</li>
        <li>İstediğiniz dili yükleyin, örneğin Vietnamca için:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Önemli dil kodları: <code>deu</code> (Almanca), <code>eng</code> (İngilizce), <code>vie</code> (Vietnamca), <code>spa</code> (İspanyolca), <code>fra</code> (Fransızca), <code>ita</code> (İtalyanca), <code>nld</code> (Felemenkçe), <code>fin</code> (Fince), <code>swe</code> (İsveççe), <code>nor</code> (Norveççe).</li>
        <li>Mevcut tüm paketleri göster:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuel)</p>
        <ol>
        <li>İstediğiniz <code>*.traineddata</code> dosyalarını şu adresten indirin:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ör. Vietnamca için <code>vie.traineddata</code>).</li>
        <li>Dosyaları Tesseract dil klasörüne kopyalayın, genellikle:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Bireysel kuruluma göre ayarlayın.)</li>
        <li>Uygulamayı yeniden başlatın (veya OCR dili seçimini yeniden açın).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Tüm sistemler için alternatif</p>
        <ul>
        <li><strong>OCRmyPDF</strong> ve <strong>Tesseract</strong>'ı seçtiğiniz bir paket yöneticisi ile kurun. Çoğu kurulum zaten bazı standart dilleri (İngilizce, Almanca, Fransızca) içerir.</li>
        <li>Eksik diller her zaman kurulabilir – OCR dili seçimi yalnızca gerçekten var olan dilleri listeler.</li>
        </ul>

        <hr>
        <p><b>✅ Kurulumdan sonra:</b> Uygulamayı yeniden başlatmanız gerekmez – yeni eklenen diller hemen listede görünecektir.</p>
        <p><b>📖 Dil kodları için yardım:</b> Tam bir liste <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract belgelerinde</a> mevcuttur.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans yazı tipleri",
        "info_noto_font_voice": "Noto Sans yazı tipi kurulum kılavuzu",
        "btn_info_noto_font_install": "Yazı tipi bilgisi",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Google'ın ücretsiz Noto yazı tipleri nasıl kurulur</h2>

        <p><strong>Noto yazı tipleri</strong>, Google'ın açık kaynaklı bir yazı tipi ailesidir. Amaçları, <em>"tofu yok"</em> (yani boş kutular □) görmemek ve Unicode standardındaki her karakteri doğru şekilde görüntülemektir. Pek çok farklı dilde metin görüntülemesi gereken uygulamalar için ideal bir tamamlayıcıdır.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 macOS'ta kurulum</h3>

        <p><strong>Yöntem 1: Homebrew ile (ileri düzey kullanıcılar için)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Yöntem 2: "Font Book" aracılığıyla (Önerilir)</strong></p>

        <ol>
        <li>Resmi yazı tipi paketini indirin:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP dosyasını çıkarın</li>
        <li>Dosyaları <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code> konumuna kopyalayın</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Windows'ta kurulum (10 ve 11)</h3>

        <p><strong>Yöntem 1: Microsoft Store (Önerilir)</strong><br>
        "Google Noto Fonts" veya "Noto Sans"ı arayın ve <strong>Yükle</strong>'yi tıklayın.</p>

        <p><strong>Yöntem 2: Manuel kurulum</strong></p>

        <ol>
        <li>İndirin:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP'i çıkarın</li>
        <li>.ttf / .otf dosyalarını seçin</li>
        <li>Sağ tıklayın → <strong>Yükle</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        veya<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\İsim\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Linux'ta kurulum</h3>

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

        <p>Doğrulama:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Yer imlerini yönet",
        "bookmark_add": "Yer imi ekle",
        "bookmark_add_tooltip": "Geçerli sayfayı yer imi olarak kaydet",
        "bookmark_remove": "Yer imini kaldır",
        "bookmark_remove_tooltip": "İşaretli yer imini sil",
        "bookmark_remove_all": "Tümünü kaldır",
        "bookmark_remove_all_tooltip": "Bu PDF'in tüm yer imlerini sil",
        "bookmark_jump": "Yer imine git",
        "bookmark_jump_tooltip": "Seçili sayfaya git",
        "bookmark_name": "Ad",
        "bookmark_page": "Sayfa",
        "bookmark_no_bookmarks": "Yer imi yok.\nGeçerli sayfayı yer imi olarak kaydetmek için 'Ekle'yi tıklayın.",
        "bookmark_added": "{0}. sayfa için yer imi eklendi: {1}",
        "bookmark_removed": "Yer imi kaldırıldı: {0}",
        "bookmark_all_removed": "Tüm yer imleri kaldırıldı.",
        "bookmark_name_default": "Sayfa {0}",
        "bookmark_name_prompt": "Yer imi için ad:\n(uzun metin 50 karaktere kısaltılacaktır)",
        "bookmark_name_prompt_title": "Yer imi adı",
        "bookmark_confirm_remove_all": "Tüm {0} yer imini kaldırmak istediğinizden emin misiniz?",
        "menu_bookmarks": "Yer imleri",
        "bookmark_manage": "Yer imlerini yönet",
        "bookmark_next": "Sonraki yer imi",
        "bookmark_prev": "Önceki yer imi",
        "bookmark_page_display": "Sayfa {0}",
        "bookmark_exists": "Bu sayfa için bu ada sahip bir yer imi zaten var.",
        "bookmark_select_first": "Lütfen önce bir yer imi seçin.",
        "bookmark_confirm_remove": "'Sayfa {0}: {1}' yer imini kaldırmak istediğinizden emin misiniz?",
        "bookmark_jumped_to": "{1}. sayfadaki '{0}' yer imine gidildi.",
        "bookmark_jumped_to_voice": "Yer imi {0}, sayfa {1}",
        "btn_close": "Kapat",

        "bookmark_list": "Yer imleriniz",
        "bookmark_rename": "Yer imini yeniden adlandır",
        "bookmark_rename_tooltip": "Seçili yer iminin adını değiştir",
        "bookmark_rename_title": "Yer imini yeniden adlandır",
        "bookmark_rename_prompt": "{0}. sayfadaki yer imi için yeni ad:\n(maks. 50 karakter)",
        "bookmark_renamed": "Yer imi '{0}', '{1}' olarak yeniden adlandırıldı.",
        "bookmark_item_tooltip": "Sayfa {0}: {1}\nGitmek için çift tıklayın",
        "bookmark_name_exists_question": "Bu sayfada '{0}' adında bir yer imi zaten var.\nYine de yeniden adlandırsın mı?",

        "context_bookmarks": "Yer imleri",
        "context_bookmark_add_here": "Bu sayfa için yer imi ekle",
        "context_bookmarks_existing": "Mevcut yer imleri:",
        "context_bookmarks_jump": "Yer imine git:",
        "context_bookmarks_none": "Yer imi yok",
        "context_bookmarks_clear_all": "Tüm {0} yer imini kaldır",

        "bookmark_search_placeholder": "Yer imlerini ara... (ad veya sayfa)",
        "bookmark_search_results": "\"%s\" için %d yer imi bulundu",
        "bookmark_no_search_results": "\"%s\" için yer imi bulunamadı",
        "bookmark_no_search_results_label": "\"%s\" için sonuç yok",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF meta verilerini düzenle",
        "metadata_title": "Başlık",
        "metadata_title_placeholder": "Belge başlığı",
        "metadata_title_tooltip": "Belgenin başlığı (başlık çubuğunda görüntülenir)",
        "metadata_author": "Yazar",
        "metadata_author_placeholder": "Yazarın adı",
        "metadata_author_tooltip": "Belgenin oluşturucusu",
        "metadata_subject": "Konu",
        "metadata_subject_placeholder": "Belgenin konusu",
        "metadata_subject_tooltip": "İçeriğin kısa bir açıklaması",
        "metadata_keywords": "Anahtar kelimeler",
        "metadata_keywords_placeholder": "Virgülle ayrılmış anahtar kelimeler",
        "metadata_keywords_tooltip": "Belgeyi kategorilendirmek için anahtar kelimeler",
        "metadata_creator": "Oluşturan",
        "metadata_creator_placeholder": "PDF'i oluşturan uygulama",
        "metadata_creator_tooltip": "Belgenin oluşturulduğu yazılım",
        "metadata_producer": "Üretici",
        "metadata_producer_placeholder": "PDF'i dönüştüren uygulama",
        "metadata_producer_tooltip": "PDF'i dönüştüren yazılım",
        "metadata_creation_date": "Oluşturma tarihi",
        "metadata_creation_date_tooltip": "Belgenin oluşturulma tarihi",
        "metadata_mod_date": "Değiştirme tarihi",
        "metadata_mod_date_tooltip": "Son değiştirme tarihi",
        "metadata_pdf_info": "📄 PDF bilgisi",
        "metadata_pages": "Sayfa sayısı",
        "metadata_file_size": "Dosya boyutu",
        "metadata_pdf_version": "PDF sürümü",
        "metadata_encrypted": "Şifrelenmiş",
        "metadata_encrypted_yes": "Evet (parola korumalı)",
        "metadata_encrypted_no": "Hayır",
        "metadata_reload": "📂 PDF'den yeniden yükle",
        "metadata_reset": "Değişiklikleri at",
        "metadata_reloaded": "Meta veriler PDF'den yeniden yüklendi.",
        "metadata_reset_done": "Tüm meta veri alanları sıfırlandı.",
        "metadata_no_file": "PDF dosyası yüklenmedi.",
        "metadata_save_error": "Meta veriler kaydedilirken hata oluştu",
        "metadata_saved": "Meta veriler başarıyla kaydedildi.",
        "metadata_pdf_version_unknown": "PDF (bilinmiyor)",
        "metadata_saved_message": "Meta veriler başarıyla kaydedildi.",
        "metadata_saved_voice": "Meta veriler kaydedildi.",

        "metadata_custom": "🔧 Özel meta veriler",
        "metadata_custom_placeholder": "{\n  \"benim_alanım\": \"benim_değerim\",\n  \"diğer_alan\": 123\n}",
        "metadata_custom_tooltip": "Özel meta veriler için JSON biçimi (isteğe bağlı)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "\"{0}\" şablonu seçildi - Eklemek için çift tıklayın",
        "text_use_template": "Metin bloğu kullan",
        "text_type": "Tür",
        "text_search_templates": "Metin bloklarını ara...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Dışa / İçe aktarma bilgisi",
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

        <h3>📦 Ne dışa aktarılır? (Genel bakış)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Genel uygulama ayarları</span></li>
            <li class="detail">• Koyu/Açık mod</li>
            <li class="detail">• Görüntüler için koyu mod ters çevirme</li>
            <li class="detail">• Gri eşik değeri</li>
            <li class="detail">• Dil</li>
            <li class="detail">• Pencere geometrisi</li>
            <li class="detail">• Yakınlaştırma modu</li>
            <li class="detail">• Gezinme (Gezinme çubuğu görünür)</li>
            <li class="detail">• Konuşma çıktısı (açık/kapalı)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Yedekleme ayarları</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Dosya adlandırma (Zaman damgası, Ayırıcı, Sonekler)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Ekleme ayarları</span></li>
            <li class="detail">• İmzalar</li>
            <li class="detail">• Metin ve metin blokları</li>
            <li class="detail">• İşaretler, görüntüler ve şekiller</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR ayarları</span></li>
            <li class="detail">• Dil</li>
            <li class="detail">• OCR'yi zorla · Sayfa modu</li>
            <li class="detail">• Görüntü ön işleme: Eğikliği düzelt, Temizle, Aşırı örnekleme</li>
            <li class="detail">• Paralel iş sayısı</li>
            <li class="detail">• Ters çevirme modu</li>
            <li class="detail">• Gri eşik değeri</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Yer imleri</span></li>
            <li class="detail">• PDF dosyası başına tüm yer imleri (Sayfa, Ad, Oluşturma zamanı)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Parola veritabanı</span></li>
            <li class="detail">• Kaydedilmiş PDF parolaları (isteğe bağlı olarak şifrelenmiş veya düz metin)</li>
            <li class="detail">• Ana parola karması (ayarlanmışsa)</li>
            <li class="detail">• Doğrulama verileri</li>
        </ul>

        <h4>⚠️ Önemli notlar</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 İçe aktarırken:</strong>
            <ul>
                <li><span class="warning">➜ TÜM mevcut ayarlar tamamen üzerine yazılacaktır</span></li>
                <li>• Uygulamayı yeniden başlatmak zorunludur</li>
                <li>• Mevcut imzalar, metin blokları ve yer imleri değiştirilecektir</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Ana parola ve dışa aktarma modu:</strong>
            <ul>
                <li>• Ana parola etkin olduğunda şunları seçebilirsiniz:</li>
                <li>  - <span style="color: #98FB98;"><strong>Şifresi çözülmüş</strong></span> (parolalar ZIP içinde düz metin olarak bulunur)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Şifrelenmiş</strong></span> (yalnızca hedef sistemde ana parola ile okunabilir)</li>
                <li>• Ana parola karması <strong>her zaman</strong> şifrelenmiş olarak saklanır</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Güvenlik bildirimi:</strong>
            <ul>
                <li>• Dışa aktarılan ZIP dosyası hassas veriler içerir (<strong>parolalar, yer imleri, imzalar</strong>)</li>
                <li>• Lütfen güvenli bir yerde saklayın (örn. şifrelenmiş USB bellek, parola yöneticisi)</li>
                <li>• Dosya kaybolursa, kaydedilen PDF parolaları geri dönüşü olmayacak şekilde kaybolur</li>
            </ul>
        </div>

        <h4>📁 Dışa aktarma biçimi</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Ayarlar tek bir ZIP dosyasına kaydedilir:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Bu ZIP, tam <code>settings.json</code> (yapılandırmanızdan) ve ayrıca gömülü imza görüntü dosyaları ve şifrelenmiş parolalar içerir.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "İmzalar - Kılavuz",
        'signature_guide_html': """
        📝 <strong>İmzalar - Hızlı Kılavuz</strong><br>
        <ul>
        <li>Ana şifreyi ayarlayın</li>
        <li>İmzaları <em>Ayarlar</em> menüsünde yapılandırın (boyut, zaman damgası, …)</li>
        <li>İstenen konumda <strong>SAĞ TIKLAYARAK</strong> ekleyin (oturum başına bir kez ana şifre gerekir)</li>
        <li>İmzayı fare veya ok tuşlarıyla taşıyın</li>
        <li>Arka arkaya birden fazla imza ekleyin</li>
        <li>Her imzayı ayrı ayrı özelleştirin</li>
        <li>Tek imzayı iptal edin</li>
        <li>Tüm imzaları bir kerede kaydedin / iptal edin</li>
        <li>Alternatif olarak, menü çubuğu da kullanılabilir.</li>
        </ul>
        """,
        'signature_guide_voice': "İmzalar için hızlı kılavuz. Ana şifreyi ayarlayın. İmzaları ayarlarda yapılandırın. Sağ tıklayarak ekleyin.",

        'image_guide_title': "Resim Ekleme - Kılavuz",
        'image_guide_html': """
        📷 <strong>PDF'e Resim Ekleme - Hızlı Kılavuz</strong><br>
        <ol>
        <li>İstenen konumda sağ tıklayın</li>
        <li><em>„Resim ekle“</em> → Resmi seçin</li>
        <li>Resmi konumlandırın: Fareyle sürükleyin</li>
        <li>Boyutu ayarlayın: Köşelerden/kenarlardan sürükleyin</li>
        <li>En boy oranını koruyun: <strong>[A]</strong> tuşu</li>
        <li>Diğer ayarlamalar: Resim üzerinde sağ tıklayın</li>
        </ol>
        <p><strong>İpucu:</strong> Bağlam menüsünde ayarları düzenleyebilirsiniz.</p>
        """,
        'image_guide_voice': "Resimler için hızlı kılavuz. Sağ tıklayın, resim ekleyin, seçin. Fareyle konumlandırın, köşelerden boyutu ayarlayın. En boy oranı için A tuşu.",

        'form_guide_title': "Şekil Ekleme - Kılavuz",
        'form_guide_html': """
        📐 <strong>PDF'e Şekil Ekleme - Hızlı Kılavuz</strong><br>
        <ol>
        <li>Şekil türünü seçin (dikdörtgen, elips, çizgi, ok)</li>
        <li>Konuma tıklayın:
            <ul>
            <li>Dikdörtgen/elips için: Bir tıklama şekli yerleştirir</li>
            <li>Çizgi/ok için: Başlangıç ve bitiş noktası için iki tıklama</li>
            </ul>
        </li>
        <li>Şekli konumlandırın: Fareyle sürükleyin</li>
        <li>Boyutu ayarlayın: Köşelerden/kenarlardan sürükleyin</li>
        <li>Şekli kaydedin: <strong>Enter</strong></li>
        <li>Şekli iptal edin: <strong>ESC</strong></li>
        <li>Diğer ayarlamalar: Şekil üzerinde sağ tıklayın</li>
        </ol>
        <p><strong>İpucu:</strong> Bağlam menüsünde ayarları düzenleyebilirsiniz.</p>
        """,
        'form_guide_voice': "Şekiller için hızlı kılavuz. Şekil türünü seçin. Dikdörtgen veya elips için bir kez tıklayın, çizgi veya ok için iki kez. Fareyle konumlandırın, köşelerden boyutu ayarlayın. Enter ile kaydedin, Escape ile iptal edin.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "önceki",
        "btn_next_result": "sonraki",
        "ocr_text_window": "OCR metin penceresi",
        "bookmark_existing": "Mevcut yer imleri",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR Karşılaştırması Mac - Windows",
        'ocr_method_mac_win_title': "Mac ve Windows arasındaki OCR farkları",
        'ocr_method_mac_win_voice': "Mac daha iyidir",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – macOS ve Windows arasındaki farklar</strong></p>

        <p><strong>macOS (önerilir)</strong></p>
        <p>Araç:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Sonuç:</p>
        <ul>
        <li>Orijinal düzeni büyük ölçüde koruyan, gömülü metne sahip aranabilir bir PDF.</li>
        </ul>
        <p>Avantajlar:</p>
        <ul>
        <li>Mükemmel metin tanıma kalitesi (eğri sayfalarda bile).</li>
        <li>Vektör grafiklerinin ve yazı tiplerinin korunması.</li>
        <li>Alt işlem değerlendirmesi yoluyla GUI ilerleme çubuğu.</li>
        <li>Tüm OCR parametreleri üzerinde tam kontrol (Deskew, Clean, Oversample, optimizasyon).</li>
        <li>Metin arama, ana pencerede (PDF görünümü) doğrudan kullanılabilir.</li>
        </ul>
        <p>Dezavantajlar:</p>
        <ul>
        <li>Ek sistem araçları gerektirir (ocrmypdf, Ghostscript, unpaper, pngquant – Uygulama paketinde bulunur).</li>
        <li>Daha karmaşık hata işleme (kilitlenmeler, zaman aşımları).</li>
        </ul>

        <p><strong>Windows (kararlı alternatif)</strong></p>
        <p>Araç:</p>
        <ul>
        <li>pytesseract (Tesseract'a doğrudan bağlantı) + reportlab + PyPDF2</li>
        </ul>
        <p>Sonuç:</p>
        <ul>
        <li>Görsel olarak bir resim PDF'ine karşılık gelen, ancak saydam metin aracılığıyla aranabilen bir PDF.</li>
        </ul>
        <p>Avantajlar:</p>
        <ul>
        <li>Şu anda hiçbiri aklıma gelmiyor.</li>
        </ul>
        <p>Dezavantajlar:</p>
        <ul>
        <li>PDF aslında görünmez metne sahip bir görüntüdür; karmaşık belgelerde (sütunlar, tablolar) düzen biraz sapabilir.</li>
        <li>Otomatik eğrilik düzeltmesi (--deskew) veya görüntü temizleme (--clean) yoktur.</li>
        <li>GUI ilerleme çubuğu yalnızca işlenen sayfa sayısına bağlı olarak kabaca güncellenir.</li>
        <li>OCR hızı biraz daha yavaştır (çünkü her sayfa ayrı ayrı işlenir).</li>
        <li>Metin arama, OCR metin penceresine yönlendirilir.</li>
        </ul>

        <p><strong>Ortak Özellikler</strong></p>
        <ul>
        <li>Her iki yöntem de kaynak dosyayla aynı dizinde aranabilir bir PDF oluşturur.</li>
        <li>OCR ayarları (dil, DPI, sayfa bölümleme modu, OCR motoru modu) OCRSettingsDialog aracılığıyla yapılandırılabilir ve her iki uygulamada da geçerlidir.</li>
        </ul>

        <p><strong>Tavsiye:</strong></p>
        <ul>
        <li>macOS: ocrmypdf ikili dosyası en iyi sonuçları verir – Bir Mac satın alın ve sürümü kullanın (Apple Silicon veya Intel çipli Mac'ler için PDFDarkView). OCR sonuçları Windows'tan daha iyidir!</li>
        <li>Windows: pytesseract çözümünü kullanın. Kararlıdır ve çoğu belge için tamamen yeterli kalite sağlar.</li>
        </ul>

        <p><strong>Önemli Not:</strong></p>
        <ul>
        <li>Her iki sürüm de kullanıcı arayüzüne tamamen entegre edilmiştir – kullanıcı herhangi bir fark fark etmez.</li>
        <li>Program, hangi OCR motorunun kullanılacağına işletim sistemine göre otomatik olarak karar verir.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "İmza oluştur (taramadan)",
        "signature_create_title": "Taranmış imzayı seçin (PDF/resim)",
        "image_pdf_filter": "Resimler ve PDF",
        "signature_pdf_empty": "PDF sayfa içermiyor.",
        "signature_created_success": "İmza başarıyla oluşturuldu: {0}",
        "signature_create_error": "İmza oluşturulurken hata:\n{0}",
        "rembg_missing": "rembg kurulu değil.\nLütfen kurun: pip install rembg\nHata: {0}",
        "signature_name_title": "İmza için dosya adı",
        "signature_name_message": "Lütfen yeni imza için bir dosya adı girin (şeffaf arka planlı PNG olarak kaydedilecektir):",
        "signature_name_label": "Dosya adı:",
        "signature_name_voice": "İmza için dosya adını girin",
        "signature_processing": "İşlem devam ediyor...",
        "signature_creation_title": "İmza oluşturuluyor",
        "signature_overwrite_warning": "Dosya '{0}' zaten mevcut. Üzerine yazılsın mı?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"İmza için PDF hazırlayın",
        "signature_prepare_instruction":"Lütfen tek bir sayfada taranmış bir imza içeren bir PDF seçin.\n\nEn iyi tanıma için aşağıdaki koşulları sağlayın:\n• İmza beyaz kağıt üzerine siyah mürekkeple (tükenmez kalem veya ince uçlu kalem) yazılmış olmalıdır.\n• İmza, başka şekilde boş olan A4 sayfasının üst üçte birinde bulunmalıdır.\n• PDF en az 300 dpi'da taranmış olmalıdır.\n• İmza net ve çok ince olmamalıdır.\n• Rahatsız edici arka plan desenleri veya çizgiler olmamalıdır.",
        "signature_prepare_voice":"Lütfen taranmış imzaya sahip bir PDF seçin. İyi kalite ve kontrasta dikkat edin.",
        "sig_thickness_label":"Çizgi kalınlığı:",
        "sig_thickness_normal":"Normal (ince)",
        "sig_thickness_bold":"Kalın (önerilir)",
        "sig_thickness_very_bold":"Çok kalın",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI ve OCR dilleri ekleme - Kılavuz",
        'language_guide_title': "GUI ve OCR dilleri ekleme",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>İstediğiniz çeviri dosyasını <code>translations_xy.py</code> adresinden indirin<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        ve aşağıdaki dizine yerleştirin:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Web tarayıcınızı açın.</li>
        <li>Şu adrese gidin: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Ekranın sağ kenarında "Releases" bölümünü bulun ve <strong>"latest"</strong> olarak işaretleneni seçin.</li>
        <li>Bir sonraki sürüm sayfasında, en alttaki <code>Source Code.zip</code> dosyasını indirin.</li>
        <li>ZIP dosyasını açın.</li>
        <li>Açılan klasörde ihtiyacınız olan tüm dil dosyalarını bulun ve bunları dizine kopyalayın:<br/>
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
        "menu_watermark":"Filigran ekle",
        "fullpage_text_watermark_title":"Metin filigranı",
        "fullpage_image_watermark_title":"Resim filigranı",
        "filename_with_watermark":"_filigranli",
        "watermark_text":"Metin:",
        "watermark_text_placeholder":"Filigran metniniz...",
        "watermark_font_family":"Yazı tipi:",
        "watermark_font_size":"Yazı tipi boyutu:",
        "watermark_format":"Biçimlendirme:",
        "watermark_bold":"Kalın",
        "watermark_italic":"İtalik",
        "watermark_color":"Renk:",
        "watermark_choose_color":"Renk seçin...",
        "watermark_opacity":"Opaklık / Şeffaflık:",
        "watermark_direction":"Okuma yönü:",
        "watermark_direction_l_r":"Sol → Sağ",
        "watermark_direction_bl_tr":"Sol alt → Sağ üst",
        "watermark_direction_tl_br":"Sol üst → Alt",
        "watermark_direction_b_t":"Alt → Üst",
        "watermark_direction_t_b":"Üst → Alt",
        "watermark_preview":"Önizleme:",
        "watermark_preview_sample":"Örnek metin",
        "watermark_empty_text":"Lütfen metin girin.",
        "watermark_applied":"Filigran tüm sayfalara uygulandı.",
        "watermark_saved":"Filigran kaydedildi.",
        "image_scale":"Boyut:",
        "image_preview":"Resim önizlemesi:",
        "no_image_selected":"Resim seçilmedi",
        "browse":"Göz at...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Karartmalar",
        "redact_add_black": "Karartma (siyah)",
        "redact_add_white": "Karartma (beyaz / sil)",
        "redact_added_black": "Siyah karartma eklendi",
        "redact_added_white": "Beyaz karartma eklendi",
        "redact_apply_all": "Tüm karartmaları uygula ve kaydet",
        "redact_discard_all": "Tüm karartmaları iptal et",
        "redact_discard": "Bu karartmayı iptal et",
        "no_redactions": "Karartma yok",
        "redact_confirm_title": "Karartmaları kalıcı olarak uygula",
        "redact_confirm_message": "Uyarı: İşaretlenen alanlar kalıcı olarak silinecektir (siyah veya beyaz).\nYedekleme oluşturulacaktır (etkinleştirilmişse).\n\nDevam et?",
        "redact_apply": "Evet, şimdi karart",
        "redact_saved": "{0} karartma başarıyla uygulandı ve kaydedildi.",
        "redact_saved_voice": "{0} karartma uygulandı",
        "redact_error": "Karartma sırasında hata",
        "filename_redacted":"_karartilmis",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Sayfa numaralarını ekle',
        'page_numbers_format': 'Numara formatı:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arapça)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Romen küçük)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Romen büyük)',
        'page_numbers_format_letter': 'A, B, C ... (Harfler)',
        'page_numbers_format_custom': 'Özel',
        'page_numbers_custom_pattern': 'Desen:',
        'page_numbers_custom_placeholder': 'örn. "Sayfa {nummer}" veya "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Mevcut sayfa numarası için {nummer}, toplam için {total} kullanın',
        'page_numbers_position': 'Konum:',
        'page_numbers_pos_tl': 'Sol üst',
        'page_numbers_pos_tc': 'Üst orta',
        'page_numbers_pos_tr': 'Sağ üst',
        'page_numbers_pos_ml': 'Sol orta',
        'page_numbers_pos_mc': 'Ortalanmış',
        'page_numbers_pos_mr': 'Sağ orta',
        'page_numbers_pos_bl': 'Sol alt',
        'page_numbers_pos_bc': 'Alt orta',
        'page_numbers_pos_br': 'Sağ alt',
        'page_numbers_margins': 'Kenar boşlukları:',
        'page_numbers_margin_x': 'Yatay mesafe:',
        'page_numbers_margin_y': 'Dikey mesafe:',
        'page_numbers_range': 'Sayfa aralığı:',
        'page_numbers_all_pages': 'Tüm sayfalar',
        'page_numbers_custom_range': 'Özel aralık',
        'page_numbers_from': 'Başlangıç:',
        'page_numbers_to': 'Bitiş:',
        'page_numbers_progress': 'Sayfa numaraları ekleniyor...',
        'page_numbers_start': 'Sayfa numarası ekleme başlatılıyor...',
        'page_numbers_cancel': 'Sayfa numarası ekleme iptal edildi',
        'page_numbers_success': 'Sayfa numaraları başarıyla eklendi.\n\nYeni PDF\'i açmak ister misiniz?\n\n{0}',
        'page_numbers_complete': 'Sayfa numaraları eklendi',
        'page_numbers_error_format': 'Sayfa numaraları eklenirken hata: {0}',
        'page_numbers_content_type': 'İçerik türü:',
        'page_numbers_tab_simple': 'Basit numara',
        'page_numbers_tab_range': 'Sayfa X / Y',
        'page_numbers_tab_date': 'Tarih',
        'page_numbers_tab_custom': 'Serbest metin',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Sayfa {aktuell} / {gesamt}',
        'page_numbers_range_custom': 'Özel',
        'page_numbers_range_placeholder': 'örn. "Sayfa {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Tarih formatı:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Ocak 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Özel',
        'page_numbers_date_placeholder': 'örn. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Konum:',
        'page_numbers_date_before': 'Sayfa numarasından önce tarih',
        'page_numbers_date_after': 'Sayfa numarasından sonra tarih',
        'page_numbers_date_only': 'Yalnızca tarih (sayfa numarası yok)',
        'page_numbers_custom_text': 'Özel metin:',
        'page_numbers_custom_placeholder_text': 'Sayfa numarası için {seite}, toplam için {gesamt} kullanın\nörn. "Gizli - Sayfa {seite}" veya "{seite} / {gesamt}"',
        "filename_with_page_number":"_sayfa_numarali",
        "filename_with_page_declaration":"_sayfa_belirtecili",
        "filename_with_pagenumber":"_sayfa_numarali",
        "filename_with_date":"_tarihli",
        "filename_with_my_page_declaration":"_ozel_sayfa_belirtecili",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Kaydedilmemiş değişiklikler",
        "unsaved_changes_message_darkmode": "Kaydedilmemiş eklemeler var.\nDeğiştirmeden önce kaydetmek ister misiniz?",
        "save_and_switch": "Kaydet ve değiştir",
        "discard_and_switch": "Şimdi değiştir",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Sayfaları resim olarak dışa aktar',
        'export_images_menu': 'Resim olarak dışa aktar (PNG/JPEG)',
        'export_images_format': 'Resim formatı:',
        'export_images_dpi': 'Çözünürlük (DPI):',
        'export_images_quality': 'JPEG kalitesi:',
        'export_images_range': 'Sayfa aralığı:',
        'export_images_all_pages': 'Tüm sayfalar',
        'export_images_custom_range': 'Özel aralık',
        'export_images_from': 'Başlangıç:',
        'export_images_to': 'Bitiş:',
        'export_images_options': 'Seçenekler:',
        'export_images_single_files': 'Her sayfa ayrı dosya olarak',
        'export_images_subfolder': 'Alt klasöre dışa aktar',
        'export_images_subfolder_info': '"PDFadi_resimler" alt klasörüne',
        'export_images_same_folder': 'PDF ile aynı klasörde',
        'export_images_apply_darkmode': 'PDFDarkView ayarlarını uygula (Karanlık Mod)',
        'export_images_target_folder': 'Hedef klasör:',
        'export_images_browse': 'Göz at...',
        'export_images_preview': 'Önizleme:',
        'export_images_preview_info': 'Dışa aktarma ayarlarını seçin',
        'export_images_preview_info_detail': '{0} sayfa {1} olarak\nÇözünürlük: {2} DPI\nDosya adı: {3}\n{4}',
        'export_images_select_folder': 'Hedef klasörü seçin',
        'export_images_start': 'Resim dışa aktarma başlatılıyor...',
        'export_images_progress': 'Resimler dışa aktarılıyor...',
        'export_images_saving': 'Sayfa {0}/{1} kaydediliyor...',
        'export_images_success': 'Dışa aktarma başarılı!\n\n{0} resim şuraya kaydedildi:\n{1}',
        'export_images_complete': 'Resim dışa aktarma tamamlandı',
        'export_images_open_folder': '📁 Klasörü aç',
        'export_images_cancel': 'Resim dışa aktarma iptal edildi',
        'export_images_error_format': 'Resimler dışa aktarılırken hata: {0}',
        'export_images_pdf2image_missing': '"pdf2image" kütüphanesi kurulu değil.\n\nLütfen şununla kurun:\npip install pdf2image\n\nWindows için Poppler da gereklidir:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Uzun süreli arşivleme için PDF/A dönüşümü',
        'pdfa_menu': 'PDF/A dönüşümü (arşivlemeye uygun)',
        'pdfa_info': 'PDF\'yi PDF/A formatına dönüştürür.\n\nPDF/A, uzun süreli arşivleme için özel olarak tasarlanmıştır ve belgenin gelecekte doğru görüntülenmesini sağlar.',
        'pdfa_standard': 'PDF/A standardı:',
        'pdfa_standard_select': 'Sürüm:',
        'pdfa_1': 'PDF/A-1 (basit, geniş uyumlu)',
        'pdfa_2': 'PDF/A-2 (modern, daha iyi sıkıştırma)',
        'pdfa_3': 'PDF/A-3 (en yeni sürüm, ek dosyalara izin verir)',
        'pdfa_standards_explanation': '📖 Standartların açıklaması:\n\n'
            '• PDF/A-1: Temel, eski sistemlerle uyumlu (yaklaşık 2005)\n'
            '• PDF/A-2: Daha modern, daha iyi sıkıştırma, şeffaflık desteği (yaklaşık 2011)\n'
            '• PDF/A-3: En yeni sürüm, dosya eklerinin gömülmesine izin verir (yaklaşık 2013)\n\n'
            'Öneri: PDF/A-2, uyumluluk ve modern özellikler arasında iyi bir uzlaşmadır.',
        'pdfa_options': 'Seçenekler:',
        'pdfa_compress_enable': 'PDF\'yi sıkıştır (daha küçük dosya)',
        'pdfa_metadata_preserve': 'Meta verileri koru (başlık, yazar, vb.)',
        'pdfa_target_folder': 'Hedef klasör:',
        'pdfa_browse': 'Göz at...',
        'pdfa_select_folder': 'Hedef klasörü seçin',
        'pdfa_ocr_info_unknown': '🔍 Metin içeriği kontrol edilemedi.',
        'pdfa_ocr_info_not_needed': '✅ Metin mevcut - OCR gerekli değil.\nPDF/A doğrudan oluşturulabilir.',
        'pdfa_ocr_info_recommended': '⚠️ Yeterli metin bulunamadı.\n\nAranabilir PDF\'ler için önce OCR çalıştırmanızı öneririz.\nNot: PDF/A, OCR olmadan da çalışır - ancak metin aranabilir olmayacaktır.',
        'pdfa_ocr_info_error': '❌ Kontrol edilirken hata: {0}',
        'pdfa_start': 'PDF/A dönüşümü başlatılıyor...',
        'pdfa_progress': 'PDF/A dönüşümü devam ediyor...',
        'pdfa_success': 'PDF/A dönüşümü başarılı!\n\nŞu şekilde kaydedildi:\n{0}\n\nYeni PDF\'i açmak ister misiniz?',
        'pdfa_complete': 'PDF/A dönüşümü tamamlandı',
        'pdfa_cancel': 'PDF/A dönüşümü iptal edildi',
        'pdfa_error_format': 'PDF/A dönüşümü sırasında hata:\n\n{0}',
        'pdfa_ocrmypdf_missing': '"ocrmypdf" kütüphanesi kurulu değil.\n\nLütfen şununla kurun:\npip install ocrmypdf',
        'btn_convert': 'Dönüştür',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF\'yi optimize et (dosya boyutunu küçült)',
        'optimize_menu': 'PDF\'yi optimize et (dosya boyutu)',
        'optimize_info': 'Çeşitli optimizasyon yöntemleriyle PDF dosyasının boyutunu küçültür.\n\nSıkıştırma seviyesi ne kadar yüksek olursa, dosya o kadar küçülür - resimlerde olası kalite kaybıyla.',
        'optimize_level': 'Sıkıştırma seviyesi:',
        'optimize_level_low': 'Düşük (hızlı, küçük tasarruf)',
        'optimize_level_medium': 'Orta (iyi uzlaşma)',
        'optimize_level_high': 'Yüksek (büyük tasarruf)',
        'optimize_level_maximum': 'Maksimum (maksimum tasarruf, yavaş)',
        'optimize_level_explanation': 'Öneri: "Orta", hız ve dosya boyutu arasında iyi bir uzlaşmadır.',
        'optimize_options': 'Seçenekler:',
        'optimize_compress_images': 'Resimleri sıkıştır (JPEG kalitesini düşür)',
        'optimize_clean_objects': 'Kullanılmayan nesneleri kaldır',
        'optimize_preserve_metadata': 'Meta verileri koru (başlık, yazar, vb.)',
        'optimize_image_quality': 'Resim kalitesi:',
        'optimize_range': 'Sayfa aralığı:',
        'optimize_all_pages': 'Tüm sayfalar',
        'optimize_custom_range': 'Özel aralık',
        'optimize_from': 'Başlangıç:',
        'optimize_to': 'Bitiş:',
        'optimize_target_folder': 'Hedef klasör:',
        'optimize_browse': 'Göz at...',
        'optimize_select_folder': 'Hedef klasörü seçin',
        'optimize_info_box': 'Bilgi',
        'optimize_info_text': 'Optimizasyon, büyük PDF\'ler için birkaç dakika sürebilir.\n\nResimler düşük kalitede kaydedilir, bu da dosya boyutunu önemli ölçüde azaltabilir.',
        'optimize_start': 'PDF optimizasyonu başlatılıyor...',
        'optimize_progress': 'PDF optimize ediliyor...',
        'optimize_cancel': 'PDF optimizasyonu iptal edildi',
        'optimize_complete': 'PDF optimizasyonu tamamlandı',
        'optimize_error_format': 'PDF optimizasyonu sırasında hata:\n\n{0}',
        'optimize_success_message': 'PDF optimizasyonu başarılı!\n\nŞu şekilde kaydedildi:\n{0}\n\nÖnce: {1}\nSonra: {2}\nTasarruf: {3:.1f}%\n\n{4}\n\nOptimize edilmiş PDF\'i açmak ister misiniz?',
        'optimize_success_message_no_size': 'PDF optimizasyonu başarılı!\n\nŞu şekilde kaydedildi:\n{0}\n\nBoyut bilgisi mevcut değil.\n\nOptimize edilmiş PDF\'i açmak ister misiniz?',
        'optimize_result_positive': 'Dosya {0:.1f}% küçültüldü.',
        'optimize_result_zero': 'Dosya boyutunda değişiklik yok.',
        'optimize_result_negative': 'Dosya {0:.1f}% büyüdü.\nOptimizasyon atlandı, orijinal dosya korundu.',
        'btn_optimize': 'Optimizasyonu başlat',
        'filename_optimize_low_suffix': '_optimize_edilmis_dusuk',
        'filename_optimize_medium_suffix': '_optimize_edilmis',
        'filename_optimize_high_suffix': '_optimize_edilmis_yuksek',
        'filename_optimize_maximum_suffix': '_optimize_edilmis_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF\'yi kırp',
        'crop_menu': 'PDF\'yi kırp (Crop)',
        'crop_range': 'Şuna uygula:',
        'crop_all_pages': 'Tüm sayfalar',
        'crop_current_page': 'Yalnızca mevcut sayfa',
        'crop_values': 'Kırpma değerleri (puan cinsinden):',
        'crop_left': 'Sol:',
        'crop_right': 'Sağ:',
        'crop_top': 'Üst:',
        'crop_bottom': 'Alt:',
        'crop_presets': 'Ön ayarlar:',
        'crop_preset_white': 'Beyaz kenarları algıla',
        'crop_reset': 'Sıfırla',
        'crop_mouse_hint': '🖱️ Alanı kabaca seçmek için bir dikdörtgen sürükleyin.\nArdından SpinBox\'lardaki değerleri hassas şekilde ayarlayabilirsiniz.\nFareyle manuel ayarlama mümkün değildir.',
        'crop_apply': 'Kırp',
        'crop_scope_all': 'Tüm sayfalar',
        'crop_scope_current': 'Mevcut sayfa',
        'crop_new_size': 'Yeni boyut: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'PDF yüklenmedi',
        'crop_preview_error': 'Önizleme yüklenirken hata',
        'crop_start': 'Kırpma başlatılıyor...',
        'crop_progress': 'PDF kırpılıyor...',
        'crop_success': 'PDF başarıyla kırpıldı!\n\nŞu şekilde kaydedildi:\n{0}\n\nKırpılmış PDF\'i açmak ister misiniz?',
        'crop_complete': 'Kırpma tamamlandı',
        'crop_cancel': 'Kırpma iptal edildi',
        'crop_error_format': 'Kırpma sırasında hata:\n\n{0}',
        'filename_crop_suffix': '_kirpilmis',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF\'yi düzleştir (Flatten)',
        'flatten_menu': 'PDF\'yi düzleştir (Flatten)',
        'flatten_info': 'PDF\'yi düzleştirmek, tüm düzenlenebilir öğeleri sayfa içeriğine "gömer".\n\nBundan sonra form alanları, açıklamalar, metinler, çarpı işaretleri, imzalar, resimler ve şekiller ayrı ayrı düzenlenemez.',
        'flatten_explanation_title': '📖 Bu ne işe yarar?',
        'flatten_explanation_text': 'Düzleştirme aşağıdaki durumlarda gereklidir:\n\n'
            '• 📄 Belgeyi yazdırmaya hazırlamak istiyorsanız\n'
            '• 🔒 Birinin form alanlarını değiştirmesini engellemek istiyorsanız\n'
            '• 📎 Açıklamaları ve yorumları belgeye "kalıcı" olarak gömmek istiyorsanız\n'
            '• 🖼️ Eklenen metinleri, çarpı işaretlerini, imzaları, resimleri ve şekilleri belgeye kalıcı olarak sabitlemek istiyorsanız\n'
            '• 📦 Dosyayı arşivlemeye hazırlamak istiyorsanız\n\n'
            'Düzleştirme PDF\'yi küçültür ve öğelerin yanlışlıkla taşınmasını veya silinmesini önler.',
        'flatten_what_title': 'Ne düzleştirilir?',
        'flatten_what_list': '• ✅ Form alanları (metin alanları, onay kutuları, düğmeler)\n'
            '• ✅ Açıklamalar (yorumlar, vurgulamalar, notlar)\n'
            '• ✅ Katmanlar (metinler, çarpı işaretleri, imzalar, resimler, şekiller)',
        'flatten_options': 'Seçenekler:',
        'flatten_forms': 'Form alanlarını düzleştir',
        'flatten_annotations': 'Açıklamaları düzleştir',
        'flatten_overlays': 'Katmanları düzleştir (metinler, çarpı işaretleri, imzalar, resimler, şekiller)',
        'flatten_target_folder': 'Hedef klasör:',
        'flatten_browse': 'Göz at...',
        'flatten_select_folder': 'Hedef klasörü seçin',
        'flatten_warning': '⚠️ Önemli: Düzleştirme geri alınamaz bir işlemdir!\n\nDüzleştirmeden sonra düzenlenebilir öğeler ayrı ayrı değiştirilemez veya silinemez.\nGerekirse önceden yedekleme oluşturun.',
        'flatten_apply': 'Düzleştir',
        'flatten_start': 'Düzleştirme başlatılıyor...',
        'flatten_progress': 'PDF düzleştiriliyor...',
        'flatten_success': 'PDF başarıyla düzleştirildi!\n\nŞu şekilde kaydedildi:\n{0}\n\nDüzleştirilmiş PDF\'i açmak ister misiniz?',
        'flatten_complete': 'Düzleştirme tamamlandı',
        'flatten_cancel': 'Düzleştirme iptal edildi',
        'flatten_error_format': 'Düzleştirme sırasında hata:\n\n{0}',
        'filename_flatten_suffix': '_düzleştirilmis',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF katmanlama (Overlay)',
        'overlay_menu': 'PDF katmanlama (Overlay)',
        'overlay_info': 'Bir PDF\'i (katman) başka bir PDF\'in üzerine yerleştirir.\n\nKatman PDF\'i, temel PDF\'in üzerine yerleştirilir. Bu, filigranlar, logolar, antetli kağıtlar veya mühürler için kullanışlıdır.',
        'overlay_explanation_title': '📖 Bu ne işe yarar?',
        'overlay_explanation_text': 'Katmanlama aşağıdaki durumlarda gereklidir:\n\n'
            '• 🏢 Şirket logosunu filigran olarak her sayfaya yerleştirme\n'
            '• 📄 Boş bir PDF\'e antetli kağıt yerleştirme\n'
            '• 🖊️ Bir belgeye mühür katmanı yerleştirme\n'
            '• 🔖 Tüm sayfalara filigran yerleştirme\n'
            '• 📑 Bir şablona form katmanı yerleştirme',
        'overlay_type': 'Katman türü:',
        'overlay_type_fullpage': 'Tam sayfa (kaplayan)',
        'overlay_type_transparent': 'Tam sayfa (şeffaf - önerilir)',
        'overlay_type_stamp': 'Mühür (konumlandırılabilir)',
        'overlay_type_info_fullpage': '📄 Katman PDF\'i tam sayfanın üzerine tam olarak yerleştirilir.\nBeyaz arka plan kaldırılabilir, böylece yalnızca içerik görünür kalır.',
        'overlay_type_info_transparent': '🔍 Katman PDF\'i şeffaf arka planla tam sayfanın üzerine yerleştirilir.\nBeyaz arka plan otomatik olarak kaldırılır - filigranlar ve logolar için ideal!',
        'overlay_type_info_stamp': '🖊️ Katman PDF\'i mühür olarak konumlandırılır ve ölçeklendirilir.\nBelirli konumlardaki logolar, mühürler veya imzalar için mükemmel.',
        'overlay_remove_background': 'Beyaz arka planı kaldır:',
        'overlay_remove_background_enable': 'Katman PDF\'inden beyaz arka planı kaldır (katmanı şeffaf yapar)',
        'overlay_remove_background_tooltip': 'Katman PDF\'inden beyaz alanları kaldırarak altındaki metnin görünmesini sağlar.',
        'overlay_threshold': 'Eşik değeri:',
        'overlay_threshold_hint': '(1-254, yüksek = daha fazla beyaz kaldırılır)',
        'overlay_select_file': 'Katman PDF\'ini seçin:',
        'overlay_file_placeholder': 'Lütfen katmanlama için bir PDF dosyası seçin',
        'overlay_browse': 'Göz at...',
        'overlay_select_overlay': 'Katman PDF\'ini seçin',
        'overlay_range': 'Sayfa aralığı:',
        'overlay_all_pages': 'Tüm sayfalar',
        'overlay_custom_range': 'Özel aralık',
        'overlay_from': 'Başlangıç:',
        'overlay_to': 'Bitiş:',
        'overlay_position': 'Konum:',
        'overlay_position_center': 'Orta',
        'overlay_position_top_left': 'Sol üst',
        'overlay_position_top_right': 'Sağ üst',
        'overlay_position_bottom_left': 'Sol alt',
        'overlay_position_bottom_right': 'Sağ alt',
        'overlay_size': 'Boyut:',
        'overlay_size_original': 'Orijinal boyut',
        'overlay_size_fit_page': 'Sayfaya sığdır',
        'overlay_size_custom': 'Özel (%)',
        'overlay_opacity': 'Şeffaflık:',
        'overlay_target_folder': 'Hedef klasör:',
        'overlay_browse_folder': 'Göz at...',
        'overlay_select_folder': 'Hedef klasörü seçin',
        'overlay_warning': '⚠️ Not: Katman PDF\'i temel PDF\'in üzerine yerleştirilir ve içine "gömülür".\n\nKaydettikten sonra katman PDF\'inin öğeleri ayrı ayrı düzenlenemez.',
        'overlay_apply': 'Katmanla',
        'overlay_start': 'Katmanlama başlatılıyor...',
        'overlay_progress': 'PDF katmanlanıyor...',
        'overlay_success': 'PDF başarıyla katmanlandı!\n\nŞu şekilde kaydedildi:\n{0}\n\nKatmanlanmış PDF\'i açmak ister misiniz?',
        'overlay_complete': 'Katmanlama tamamlandı',
        'overlay_cancel': 'Katmanlama iptal edildi',
        'overlay_error_format': 'Katmanlama sırasında hata:\n\n{0}',
        'overlay_no_file': 'Katman PDF\'i seçilmedi.\n\nLütfen katmanlamak için bir PDF dosyası seçin.',
        'filename_overlay_suffix': '_katmanlanmis',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'PDF\'den resimleri çıkar',
        'extract_images_menu': 'Tüm resimleri çıkar',
        'extract_images_info': 'PDF\'den tüm resimleri çıkarır ve bunları ayrı dosyalar olarak kaydeder.\n\nResimler orijinal formatlarında kaydedilir veya seçilen bir formata dönüştürülür.',
        'extract_images_format': 'Resim formatı:',
        'extract_images_quality': 'JPEG kalitesi:',
        'extract_images_options': 'Seçenekler:',
        'extract_images_subfolder': 'Alt klasöre çıkar ("PDFadi_resimler")',
        'extract_images_unique': 'Yalnızca benzersiz resimler (kopyalardan kaçının)',
        'extract_images_range': 'Sayfa aralığı:',
        'extract_images_all_pages': 'Tüm sayfalar',
        'extract_images_custom_range': 'Özel aralık',
        'extract_images_from': 'Başlangıç:',
        'extract_images_to': 'Bitiş:',
        'extract_images_target_folder': 'Hedef klasör:',
        'extract_images_browse': 'Göz at...',
        'extract_images_select_folder': 'Hedef klasörü seçin',
        'extract_images_info_box': 'Bilgi',
        'extract_images_info_text': 'Çıkarma işlemi, büyük PDF\'ler için birkaç dakika sürebilir.\n\nResimler orijinal adlarıyla kaydedilir (sayfa_resim).',
        'extract_images_extract': 'Çıkar',
        'extract_images_start': 'Çıkarma başlatılıyor...',
        'extract_images_progress': 'Resimler çıkarılıyor...',
        'extract_images_success': '✅ Resimler başarıyla çıkarıldı!\n\n{0} resim şuraya kaydedildi:\n{1}',
        'extract_images_complete': 'Resim çıkarma tamamlandı',
        'extract_images_cancel': 'Çıkarma iptal edildi',
        'extract_images_error_format': 'Resimler çıkarılırken hata:\n\n{0}',
        'extract_images_open_folder': '📁 Klasörü aç',
        'extract_images_no_images': 'PDF\'de resim bulunamadı.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Tek sayfada birden fazla sayfa (N-Up)',
        'nup_menu': 'Tek sayfada birden fazla sayfa (N-Up)',
        'nup_info': 'Birden fazla PDF sayfasını tek bir sayfada düzenler.\n\nKompakt baskılar, özetler veya el ilanları için idealdir.',
        'nup_layout': 'Düzen:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Önizleme:',
        'nup_preview_info': '{0} sayfa → sayfa başına {1} sayfa → {2} sayfa\nDüzen: {3}',
        'nup_order': 'Sıralama:',
        'nup_order_horizontal': 'Yatay (satır satır)',
        'nup_order_vertical': 'Dikey (sütun sütun)',
        'nup_order_horizontal_reverse': 'Yatay ters',
        'nup_order_vertical_reverse': 'Dikey ters',
        'nup_range': 'Sayfa aralığı:',
        'nup_all_pages': 'Tüm sayfalar',
        'nup_custom_range': 'Özel aralık',
        'nup_from': 'Başlangıç:',
        'nup_to': 'Bitiş:',
        'nup_options': 'Seçenekler:',
        'nup_margins': 'Kenar boşlukları:',
        'nup_margin_between': 'Sayfalar arası boşluk:',
        'nup_page_numbers': 'Sayfa numaralarını ekle',
        'nup_target_folder': 'Hedef klasör:',
        'nup_browse': 'Göz at...',
        'nup_select_folder': 'Hedef klasörü seçin',
        'nup_create': 'Oluştur',
        'nup_start': 'N-Up başlatılıyor...',
        'nup_progress': 'N-Up oluşturuluyor...',
        'nup_success': 'N-Up başarıyla oluşturuldu!\n\nŞu şekilde kaydedildi:\n{0}\n\nYeni PDF\'i açmak ister misiniz?',
        'nup_complete': 'N-Up tamamlandı',
        'nup_cancel': 'N-Up iptal edildi',
        'nup_error_format': 'N-Up sırasında hata:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Sayfa boyutunu değiştir',
        'pagesize_menu': 'Sayfa boyutunu değiştir',
        'pagesize_info': 'PDF\'in sayfa boyutunu değiştirir.\n\nİçerik otomatik olarak yeni boyuta uyarlanır.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Standart bir format seçin:',
        'pagesize_custom': 'Özel boyut:',
        'pagesize_width': 'Genişlik:',
        'pagesize_height': 'Yükseklik:',
        'pagesize_orientation': 'Yönlendirme:',
        'pagesize_portrait': 'Dikey',
        'pagesize_landscape': 'Yatay',
        'pagesize_scale_options': 'Ölçekleme seçenekleri:',
        'pagesize_fit': 'Sığdır (en boy oranını koru)',
        'pagesize_stretch': 'Uzat (boz)',
        'pagesize_center': 'Ortala (orijinal boyut)',
        'pagesize_range': 'Sayfa aralığı:',
        'pagesize_all_pages': 'Tüm sayfalar',
        'pagesize_custom_range': 'Özel aralık',
        'pagesize_from': 'Başlangıç:',
        'pagesize_to': 'Bitiş:',
        'pagesize_target_folder': 'Hedef klasör:',
        'pagesize_browse': 'Göz at...',
        'pagesize_select_folder': 'Hedef klasörü seçin',
        'pagesize_apply': 'Uygula',
        'pagesize_start': 'Sayfa boyutu değiştirme başlatılıyor...',
        'pagesize_progress': 'Sayfa boyutu değiştiriliyor...',
        'pagesize_success': 'Sayfa boyutu başarıyla değiştirildi!\n\nŞu şekilde kaydedildi:\n{0}\n\nYeni PDF\'i açmak ister misiniz?',
        'pagesize_complete': 'Sayfa boyutu değiştirme tamamlandı',
        'pagesize_cancel': 'Sayfa boyutu değiştirme iptal edildi',
        'pagesize_error_format': 'Sayfa boyutu değiştirilirken hata:\n\n{0}',
        'pagesize_preview_info': 'Yeni boyut: {0} x {1} pt',
        'filename_pagesize_suffix': '_yeni_boyut',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF bilgisi',
        'pdf_info_menu': 'PDF bilgilerini göster',
        'pdf_info_voice': 'PDF bilgileri gösteriliyor',
        'pdf_info_error': 'PDF bilgileri gösterilirken hata:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Klavye kısayollarını göster",
        "shortcuts_dialog_title": "Klavye Kısayolları",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 DOSYA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF aç</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF kapat</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Farklı kaydet...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Belgeyi koru</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Yazdır</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Hemen yazdır (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Uygulamadan çık</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 DIŞA AKTAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Pages olarak dışa aktar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>DOCX olarak dışa aktar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>TXT olarak dışa aktar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Resim olarak dışa aktar (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Resimleri çıkar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ BELGE İŞLEME</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Birden fazla sayfa)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A dönüşümü (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF\'yi düzleştir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF katmanla</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF\'yi optimize et</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ DÜZENLE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Ara</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Yer imi ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Yer imlerini yönet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Sonraki yer imi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Önceki yer imi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR çalıştır</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SAYFA YÖNETİMİ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Mevcut sayfayı döndür</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Tüm sayfaları döndür</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Mevcut sayfayı normalleştir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Tüm sayfaları normalleştir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Sayfaları sil</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Sayfaları çıkar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Sayfa ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Sayfaları taşı</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDF\'leri birleştir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Sayfa boyutunu değiştir</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 EKLE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Metin ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Çarpı işareti ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>İmza 1 ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>İmza 2 ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Resim ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Dikdörtgen ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Elips ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Çizgi ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Ok ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Sayfa numaralarını ekle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Metin filigranı</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Resim filigranı</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ KARARTMALAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Karartma (siyah)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Karartma (beyaz)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Tüm karartmaları uygula</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ GELİŞMİŞ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF\'yi kırp</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Meta verileri düzenle</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ GÖRÜNÜM</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Karanlık/Aydınlık mod değiştir</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Metin penceresini göster</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Sayfa genişliği (Yakınlaştır)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>İki sayfa (Yakınlaştır)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Genel bakış (Yakınlaştır)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ AYARLAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Şifre yönetimi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR ayarları</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>İmza ayarları</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Dosya adı biçimlendirme</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Ayarları dışa aktar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Ayarları içe aktar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ BİLGİ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF bilgilerini göster</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Ses çıkışını aç/kapat</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Menü çubuğuna odaklan</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Yeni sürüm mevcut",
        "update_available_message": "Yeni bir sürüm <b>{0}</b> mevcut.\n\nGüncellemeyi indirmek için sürüm sayfasını ziyaret edin:\n{1}",
        "update_available_voice": "Yeni sürüm {0} mevcut. Lütfen güncellemeyi GitHub sayfasından indirin.",
        "update_open_release": "Sürüm sayfasını aç",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Tüm çevirileri indir",
        "ask_download_all_translations": """Almanca, İngilizce ve Vietnamca dışında {total_languages} GUI dili daha mevcut.\n\nBunlar sağlansın / güncellensin mi?\n\nNot:\nGereksiz dilleri daha sonra dizinden manuel olarak silebilirsiniz:\n{translations_path}
        \nİptal ederseniz, GUI dillerini daha sonra 'Araçlar → Çevirileri güncelle' menüsünden indirebilirsiniz.""",
        "menu_update_translations": "Çevirileri güncelle",
        "translations_updated": "Çeviriler güncellendi",
        "translations_update_success": "{} çeviri başarıyla güncellendi ({} yeni, {} güncellendi).",
        "translations_update_error": "Çeviriler güncellenirken hata oluştu",
        "translations_update_no_changes": "Tüm çeviriler zaten güncel.",
        "translations_update_offline": "İnternet bağlantısı yok. Çeviriler güncellenemedi.",
        "translations_update_in_progress": "Çeviriler arka planda güncelleniyor...",
        "translations_downloading": "Çeviriler indiriliyor...",
        "translations_path_hint": "Çeviriler için kullanıcı dizini",
        "translations_update_not_available_title": "Güncelleme mevcut değil",
        "translations_update_not_available_message": """Çevirileri güncelleme yalnızca yüklü sürümde mevcuttur.\n\nGeliştirme modunda çeviriler zaten günceldir.""",
        "translations_update_no_internet_title": "İnternet bağlantısı yok",
        "translations_update_no_internet_message": """İnternet bağlantısı kurulamadı.\n\nÇeviriler GitHub'dan indirilemiyor.\n\nOlası çözümler:
        • İnternet bağlantınızı kontrol edin
        • Olası bir güvenlik duvarını geçici olarak devre dışı bırakın
        • Daha sonra tekrar deneyin
        \nÇevirileri GitHub'dan manuel olarak da indirebilirsiniz:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Güncelleme zaten devam ediyor",
        "btn_retry": "Tekrar dene",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "PDF Dark View'a Hoş Geldiniz",
        "welcome_title_not_supported": "PDF Dark View'a Hoş Geldiniz",
        "welcome_message": "PDF Dark View'a Hoş Geldiniz!\n\nSistem diliniz '{language}' olarak algılandı.\nBu dili kullanıcı arayüzü için kullanmak istiyor musunuz?\n\nDili 'Ayarlar → Dil' üzerinden istediğiniz zaman değiştirebilirsiniz.",
        "welcome_message_language_not_available": "PDF Dark View'a Hoş Geldiniz!\n\nSistem diliniz '{language}' olarak algılandı.\nBu dil henüz yüklenmemiş.\n\n{language} için çevirileri şimdi GitHub'dan indirmek ister misiniz?\n\n(Dil daha sonra otomatik olarak kullanıcı arayüzü için kullanılacaktır.)",
        "welcome_message_language_not_supported": "PDF Dark View'a Hoş Geldiniz!\n\nSistem diliniz '{language}' olarak algılandı.\nNe yazık ki, bu dil için henüz çeviri yok.\n\nKullanıcı arayüzü {fallback_language} dilinde görüntülenecektir.\n\nDili 'Ayarlar → Dil' üzerinden istediğiniz zaman değiştirebilirsiniz.\nİsterseniz, kendi diliniz için bir çeviriye katkıda bulunabilirsiniz:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Evet, sistem dilini kullan",
        "welcome_keep_english": "Hayır, İngilizce'yi koru",
        "welcome_download_language": "Evet, {language} indir",

        # ============================================
        # 107. SON KULLANILAN YOLLAR
        # ============================================

        'menu_recent': 'Son kullanılanlar',
        'menu_recent_dirs': 'Dizinler...',
        'menu_recent_files': 'Dosyalar...',
        'recent_manage': 'Yönet...',
        'recent_enable_tracking': 'Son yolları kaydet (gizlilik)',
        'recent_enable_info': 'Yol kaydetmemek için bu seçeneği devre dışı bırakın',
        'recent_tracking_disabled': 'Yol takibi devre dışı',
        'recent_enabled': 'etkin',
        'recent_disabled': 'devre dışı',
        'recent_tracking_status': 'Yol takibi {0}',
        'recent_dialog_title': 'Son kullanılan yollar',
        'recent_tab_directories': 'Dizinler',
        'recent_tab_files': 'Dosyalar',
        'recent_dirs_instruction': 'Dizinde dosya iletişim kutusunu açmak için çift tıklayın',
        'recent_files_instruction': 'PDF\'i doğrudan açmak için çift tıklayın',
        'recent_no_directories': '(kayıtlı dizin yok)',
        'recent_no_files': '(kayıtlı dosya yok)',
        'recent_default_current': '⭐ Varsayılan: {0}',
        'recent_set_as_default': '⭐ Varsayılan olarak ayarla',
        'recent_default_set_title': 'Varsayılan dizin ayarlandı',
        'recent_default_set_message': '"{0}" dizini, PDF açmak için varsayılan olarak ayarlandı.',
        'recent_default_set_voice': 'Varsayılan dizin ayarlandı',
        'recent_directory_not_found': 'Dizin bulunamadı',
        'recent_file_not_found': 'Dosya bulunamadı',
        'recent_remove_selected': 'Kaldır',
        'recent_remove_title': 'Yolu kaldır',
        'recent_remove_confirm': '"{0}" yolunu listeden kaldırmak istediğinize emin misiniz?',
        'recent_path_removed': 'Yol kaldırıldı',
        'recent_clear_all': 'Tümünü kaldır',
        'recent_clear_title': 'Tüm yolları kaldır',
        'recent_clear_confirm_type': 'Tüm {0} öğesini silmek istediğinize emin misiniz?',
        'recent_cleared': 'Liste temizlendi',
        'recent_path_not_found_title': 'Yol bulunamadı',
        'recent_path_not_found_message': '"{0}" yolu artık mevcut değil.',
        'recent_open_file': 'Dosyayı aç',
        'btn_open_recent': 'Aç',
        'recent_open_file_question': '"{0}" dosyasını PDF olarak açmak istiyor musunuz?',
        'recent_not_pdf': 'Seçilen dosya bir PDF değil.',
        'recent_more_entries': 'Daha fazla giriş...',
        'btn_remove': 'Kaldır',
        'btn_clear': 'Tümünü temizle',
        'recent_context_open': 'Aç',
        'recent_context_reveal': 'Finder\'da göster',
        'recent_context_set_default': '⭐ Varsayılan olarak ayarla',
        'recent_context_open_terminal': '💻 Terminali aç',
        'recent_context_file_info': 'Dosya bilgisi',
        'recent_context_open_with_default': '📄 Varsayılan uygulama ile aç',
        'recent_context_remove': 'Listeden kaldır',
        'recent_context_clear_all': 'Tümünü kaldır',
        'recent_file_info_title': 'Dosya bilgisi',
        'recent_file_info_name': 'Ad',
        'recent_file_info_path': 'Yol',
        'recent_file_info_size': 'Boyut',
        'recent_file_info_modified': 'Değiştirilme',
        'recent_file_info_pages': 'Sayfalar',
        'recent_error_reveal': 'Finder\'da açarken hata',
        'recent_error_terminal': 'Terminali açarken hata',
        'recent_error_info': 'Dosya bilgisi alınırken hata',
        'open_user_data_folder': 'Kullanıcı veri dizinini göster',

        # ============================================
        # 108. ÇİFT/TEK SAYFALARI SİL
        # ============================================
        "pages_delete_even": "Tüm çift sayfaları sil",
        "pages_delete_odd":  "Tüm tek sayfaları sil",
        "progress_even_pages": "Çift sayfalar siliniyor",
        "progress_odd_pages": "Tek sayfalar siliniyor",
        "progress_mark_delete_even": "{} çift sayfa silinmek üzere işaretlendi",
        "progress_mark_delete_odd":  "{} tek sayfa silinmek üzere işaretlendi",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program kapatılıyor",

    }
