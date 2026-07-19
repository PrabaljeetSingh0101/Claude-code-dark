# Changelog

All notable changes to **Claude Code Dark** are documented here.

This format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [1.1.1] - 2026-07-19

### Fixed
- **Bracket Highlights**: Removed duplicate yellow (`#FBBC04`) on levels 1 and 2. Shifted all bracket colors forward and added Claude Orange (`#D77757`) as the new 6th level for a complete, distinct color cycle: Yellow → Blue → Green → Purple → Red → Orange.

## [1.1.0] - 2026-07-19

### Changed
- **Editorial Minimalism**: Enforced 'Invisible Chrome' by making all structural UI panel borders and notification borders completely transparent (`#00000000`).
- **Strategic Spotlight**: Replaced 'Tech Blue' (`#6A9BCC`) borders with a 'Warm Silver' (`#C3C2B7`) spotlight on strictly active elements (tabs, panels, etc.).
- **Typography & Warmth**: Changed primary foreground text across the editor from clinical white (`#EAECF0`) to a warm parchment white (`#E7E6E1`) for a printed paper aesthetic.
- **Brand Accents**: Updated activity bar notification badge to True Claude Orange (`#D77757`) to act as a focused focal point.
- **Terminal & Notifications**: Aligned terminal cursor color to 2026 dark defaults (`#bfbfbf`) and updated notifications background to the official Claude snackbar color (`#323232`).

## [1.0.8] - 2026-07-15

### Changed
- Accents & Borders: Swapped out the Claude Orange (`#D77757`) for Claude Blue (`#6A9BCC`) on various UI borders, active panel titles, input options, and list highlights for a cooler, calmer aesthetic.
- Notifications: Lightened the notification background to `#323232` and removed the toast border.
- Terminal: Changed terminal cursor color to a neutral grey (`#bfbfbf`).

## [1.0.7] - 2026-07-13

### Changed
- Global Typography: Refined the primary text color (foreground) across the entire theme to `#EAECF0` for a crisp, natural contrast.
- Title Bar: Softened the menu text color (File, Edit, View, etc.) to `#C3C2B7` to blend smoothly into the dark window frame.

## [1.0.6] - 2026-07-11

### Added
- Sticky Scroll: Added a subtle bottom border (`#30302E`) to visually separate sticky function headers from the main code.

### Changed
- Unified Outer Frame: Darkened the Activity Bar, Status Bar, Title Bar, and Tab Bar to a uniform deep dark color (`#141413`).
- Command Palette: Updated the quick input background to `#2c2c2a`.
- Breakpoints: Changed breakpoint indicator from soft red to a striking classic red (`#E51400`).

### Fixed
- IntelliSense Readability: Fixed an issue where matched search text disappeared when a suggestion was selected by explicitly defining focus highlight colors (`#FBBC04`).

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