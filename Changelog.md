# Changelog

All notable changes to **Claude Code Dark** are documented here.

This format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [1.0.5] - 2026-07-09

### Changed
- Explorer Pane: Dimmed file names and sidebar text to `#C3C2B7` to reduce distraction while coding.
- UI Contrast: Updated remaining black text inside orange/blue badges and remote status bars to off-white (`#F8F8F6`) for perfect readability.

### Fixed
- Status Bar: Explicitly set the "no folder open" status bar color to `#181817`, overriding VS Code's default purple (`#68217A`).

## [1.0.4] - 2026-07-09

### Changed
- Global Typography: Softened pure white (`#FFFFFF`) to off-white (`#F8F8F6`) across all code syntax, UI text, and badges to reduce eye strain.
- Hover Styles: Deepened hover backgrounds for lists, settings, and the status bar (now `#42423F` and `#323233`).
- Sidebar & Badges: Replaced all orange highlights, buttons, and badges in the Side Bar with Claude Blue (`#264F78`) featuring high-contrast white text.
- Debug Status Bar: Improved readability during debugging by explicitly setting the status bar background to Claude Blue (`#264F78`) with crisp white text.
- Description.
- Debug Toolbar Icons: Mapped debug actions to specific Claude palette colors (Yellow for Continue/Pause/Step Out, Green for Step Over, Blue for Step Into).
- Notifications: Darkened notification pop-up backgrounds to `#1D1D1C` with a softer `#C3C2B7` text color.
- Integrated Terminal: Updated the terminal background color to `#1D1D1C`.

## [1.0.3] - 2026-07-08

### Fixed
- Changed the logo.

## [1.0.2] - 2026-07-08

### Fixed
- Changed font from bold to normal.

## [1.0.1] - 2026-07-08

### Added
- Initial release
- Full syntax highlighting mapped from the Claude Code CLI palette
- Editor chrome (tabs, sidebar, status bar, panels, minimap)
- Git decorations (added, modified, deleted, conflicted)
- Diagnostics (errors, warnings, hints)
- Integrated terminal theming