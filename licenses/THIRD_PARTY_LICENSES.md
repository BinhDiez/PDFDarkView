# Third-Party Licenses / Lizenzen Dritter

This project bundles the following third-party libraries. The list is
informational and not legal advice. For the distributed binaries, the
strictest applicable license governs the combined work.

Dieses Projekt bündelt die folgenden Bibliotheken von Drittanbietern.
Die Liste ist informativ und keine Rechtsberatung. Für die verteilten
Binärpakete gilt die strengste anwendbare Lizenz für das Gesamtwerk.

## PyMuPDF (fitz) — AGPL-3.0 or Artifex Commercial

PyMuPDF is dual-licensed under the GNU Affero General Public License v3.0
(AGPL-3.0) and a commercial license from Artifex Software.

Because this application bundles PyMuPDF in its distributed binaries
(macOS .app, Windows .exe), the binaries are conveyed under the terms of
the AGPL-3.0. The corresponding source code is this public repository.

Full license text: see `licenses/AGPL-3.0.txt` in the bundle.
Official source: https://www.gnu.org/licenses/agpl-3.0.txt

If you cannot comply with AGPL-3.0, you must obtain a commercial license
from Artifex: https://artifex.com/licensing

## PySide6 / Qt — LGPL-3.0

PySide6 and the Qt libraries are licensed under the LGPL-3.0. In the
packaged binaries, the Qt shared libraries are shipped alongside the
executable (dynamic linking), which satisfies the LGPL relinking
requirement.

Full license text: see `licenses/LGPL-3.0.txt` in the bundle.
Official source: https://www.gnu.org/licenses/lgpl-3.0.txt

## qtawesome — MIT

Copyright © 2015–2025 Spyder Project Contributors.
MIT License. The bundled icon fonts are under their respective licenses
(Font Awesome: SIL OFL 1.1; Material Design Icons: Apache-2.0;
Phosphor: MIT).

Full MIT text: see `LICENSE.txt`.
OFL text: see `licenses/OFL-1.1.txt`.
Apache text: see `licenses/Apache-2.0.txt`.

## pyttsx3 — MPL-2.0

Mozilla Public License 2.0.

Full license text: see `licenses/MPL-2.0.txt`.

## Pillow (PIL) — HPND

The Python Imaging Library (Pillow) is distributed under the HPND license.

Full license text: see `licenses/HPND.txt`.

## PyPDF2 — BSD-3-Clause

BSD 3-Clause License.

Full license text: see `licenses/BSD-3-Clause.txt`.

## NumPy — BSD-3-Clause

(If bundled via lazy import / PyInstaller collection.)
Full license text: see `licenses/BSD-3-Clause.txt`.

## OCRmyPDF — MPL-2.0

(If bundled.)
Full license text: see `licenses/MPL-2.0.txt`.

## Tesseract OCR — Apache-2.0

(External binary; not bundled by this project's PyInstaller build unless
explicitly included.)
Full license text: see `licenses/Apache-2.0.txt`.

## Poppler — GPL-2.0 / GPL-3.0

(External binary; not bundled by this project's PyInstaller build unless
explicitly included.)
Full license text: see `licenses/AGPL-3.0.txt` (the GPL text is incorporated
by reference in the AGPL) or https://www.gnu.org/licenses/gpl-3.0.txt.
