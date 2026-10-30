# ⚡ The Debian KDE Rice Bible

Oct 30, 2026 · @Arihant Jain

## 00 // TL;DR: The 60-Minute Glow-Up

Biggest visual jump per minute: palette, then icons/fonts, then Kvantum, then panels, then terminal. Everything here is free; anything marked "later" needs a newer Plasma than Debian 13's 6.3.

1. **Safety net (5 min):** `sudo apt install timeshift pipx`, take a snapshot, `pipx install konsave`, `konsave -s stock`. (Section 01)
2. **Pick a palette + wallpaper (5 min):** Catppuccin, Nord, Tokyo Night, Gruvbox or Cyberpunk. (Sections 02, 07)
3. **Colors + app style (10 min):** `sudo apt install qt-style-kvantum`, install your theme + its Kvantum variant. (Sections 02, 03)
4. **Icons, cursor, font (5 min):** `sudo apt install papirus-icon-theme`, add Bibata + a Nerd Font. (Section 04)
5. **Panels (10 min):** floating "fit content" dock + thin top bar, then Panel Colorizer. (Section 05)
6. **Terminal (10 min):** `sudo apt install fastfetch starship btop zsh`, enable Konsole blur, pick a Starship preset. (Section 09)
7. **Effects (5 min):** Magic Lamp + Wobbly in Desktop Effects, KDE Rounded Corners `.deb`. (Section 06)
8. **Apps (10 min):** textfox for Firefox, Vesktop + a theme for Discord. (Section 11)

Save it: `konsave -s rice-v1`. Save GRUB/Plymouth/SDDM (section 08) for an evening when you have a live USB nearby. Want a ready-made look? Jump to section 16.

## 01 // Before You Rice (2-minute read, saves hours)

Your baseline is Debian 13 "Trixie": Plasma 6.3.6, Frameworks 6.13, Qt 6.8.2, Wayland by default ([Debian KDE plan](https://wiki.debian.org/PkgQtKde/TrixieReleasePlans), [linuxiac](https://linuxiac.com/?p=179486)). Run `plasmashell --version` to confirm. Many new widgets target Plasma 6.4+, so check each add-on's minimum version before installing.

| Step | Why | Command |
| --- | --- | --- |
| Snapshot the system | Undo a broken GRUB/Plymouth/SDDM change | `sudo apt install timeshift` |
| Save your desktop as a profile | Swap whole rices with one command | `pipx install konsave` then `konsave -s stock` ([Konsave](https://github.com/Prayag2/konsave)) |
| Back up panels separately | Panels break most often | copy `~/.config/plasma-org.kde.plasma.desktop-appletsrc` |
| Use `pipx`, not `pip` | Debian 13 blocks system-wide pip | `sudo apt install pipx` |

**Security (you'll like this one):** in March 2024 a KDE Store global theme called "Grey Layout" ran `rm -rf` and wiped every drive the user had mounted ([BleepingComputer](https://www.bleepingcomputer.com/news/linux/kde-advises-extreme-caution-after-theme-wipes-linux-users-files/), [Reddit thread](https://www.reddit.com/r/kde/comments/1bixmbx/do_not_install_global_themes_some_wipe_out_all/)). KDE's warning: third-party global themes and widgets can run arbitrary code, and the store isn't audited.

- Install colors, icons and cursors as separate pieces instead of all-in-one "global theme" packs
- Prefer GitHub repos you can read; grep install scripts for `rm`, `curl`, `sudo` before running
- Only use `sudo` for things that live in system paths (SDDM, GRUB, Plymouth)

**Wayland gotchas:** picom, polybar, oneko, xpenguins and xscreensaver are X11-only. You don't need picom anyway: KWin already does blur, shadows and animations. Compiled KWin effects (Better Blur, Rounded Corners) must be rebuilt after every Plasma upgrade; Debian stable rarely changes KWin, which helps.

## 02 // Global Themes & Color Schemes

Pick ONE palette first; every later choice (icons, terminal, Firefox, Discord) follows it. Catppuccin, Nord, Tokyo Night, Gruvbox and Dracula have ports for almost every app below.

**Popular (safe bets)**

| Theme | Vibe | Link |
| --- | --- | --- |
| Catppuccin | Pastel dark/light, 4 flavours x 14 accents, auto installer | [catppuccin/kde](https://github.com/catppuccin/kde) |
| Sweet | Neon purple/pink on near-black | [EliverLara/Sweet-kde](https://github.com/EliverLara/Sweet-kde) |
| Nordic | Cold Nord blues | [EliverLara/Nordic](https://github.com/EliverLara/Nordic) |
| Layan | Soft gradient purple, very "unixporn" | [vinceliuice/Layan-kde](https://github.com/vinceliuice/Layan-kde) |
| WhiteSur | macOS Big Sur clone | [vinceliuice/WhiteSur-kde](https://github.com/vinceliuice/WhiteSur-kde) |
| Colloid | Clean flat, has Nord/Dracula/Gruvbox tweaks | [vinceliuice/Colloid-kde](https://github.com/vinceliuice/Colloid-kde) |
| Orchis | Material-style, rounded | [vinceliuice/Orchis-kde](https://github.com/vinceliuice/Orchis-kde) |
| Graphite | Grey minimal, pro look | [vinceliuice/Graphite-kde-theme](https://github.com/vinceliuice/Graphite-kde-theme) |
| Utterly Nord | Glassy, translucent Nord | [HimDek/Utterly-Nord-Plasma](https://github.com/HimDek/Utterly-Nord-Plasma) |
| Dracula | Classic purple dark (KDE folder inside) | [dracula/gtk](https://github.com/dracula/gtk) |

**Niche (stand-out picks)**

| Theme | Vibe | Link |
| --- | --- | --- |
| Cyberpunk Neon | Cyan + hot pink neon, KDE + Konsole + more | [Roboron3042/Cyberpunk-Neon](https://github.com/Roboron3042/Cyberpunk-Neon) |
| Monochrome KDE | Pure black and white | [pwyde/monochrome-kde](https://github.com/pwyde/monochrome-kde) |
| AeroThemePlasma | Full Windows 7 Aero glass replica (targets Plasma 6.8, so look for an older release) | [aeroshell-desktop/aerothemeplasma](https://github.com/aeroshell-desktop/aerothemeplasma) |
| Ant / Andromeda | Dracula-ish and deep-space blue | [EliverLara/Ant](https://github.com/EliverLara/Ant), [Andromeda-KDE](https://github.com/EliverLara/Andromeda-KDE) |
| Utterly Sweet / Round | Glassy candy, very round | [Utterly-Sweet](https://github.com/HimDek/Utterly-Sweet-Plasma), [Utterly-Round](https://github.com/HimDek/Utterly-Round-Plasma-Style) |
| Materia / Arc | Old-school favourites, still clean | [materia-kde](https://github.com/PapirusDevelopmentTeam/materia-kde), [arc-kde](https://github.com/PapirusDevelopmentTeam/arc-kde) |
| Qogir, McMojave, Vimix, Fluent, Lavanda | More vinceliuice sets | [Qogir](https://github.com/vinceliuice/Qogir-kde), [McMojave](https://github.com/vinceliuice/McMojave-kde), [Vimix](https://github.com/vinceliuice/Vimix-kde), [Fluent](https://github.com/vinceliuice/Fluent-kde), [Lavanda](https://github.com/vinceliuice/Lavanda-kde) |
| Aritim Dark | Muted dark (author calls it abandoned) | [Mrcuve0/Aritim-Dark](https://github.com/Mrcuve0/Aritim-Dark) |

**KDE Store hacker finds** ([cyberpunk search](https://store.kde.org/search/projectSearchText/cyberpunk/f/tags/)): Daemon-2.0 (Kvantum, Cyberpunk 2077-inspired), CyberHack (Matrix-like glowing Kvantum), Xenon (alien-shaped glowing window decoration), CyberGRUB-2077 (bootloader).

**Built-in, zero-install:** System Settings > Colors > accent color "from wallpaper" tints the whole desktop automatically.

## 03 // App Style & Window Decorations

This layer decides how every window looks: transparency, rounded corners, title-bar buttons. Version-pin anything compiled, because Debian 13 is on Plasma 6.3.

| Tool | What it does | Debian 13 install | Link |
| --- | --- | --- | --- |
| Kvantum | SVG theme engine: translucent, blurred app styles | `sudo apt install qt-style-kvantum` ([Debian pkg](https://packages.debian.org/src:kvantum)) | [tsujan/Kvantum](https://github.com/tsujan/Kvantum) |
| Klassy | Wild title-bar buttons, outlines, round corners | Latest needs Plasma 6.6, so build branch `plasma6.3` / tag `v6.3` | [paulmcauley/klassy](https://github.com/paulmcauley/klassy) |
| Darkly | Translucent app style (Lightly's Plasma 6 successor) | Use release `v0.5.25` (for Plasma below 6.5) | [Bali10050/Darkly](https://github.com/Bali10050/Darkly) |
| KDE Rounded Corners | Rounds and outlines every window, X11 + Wayland | Ready-made Debian 13 `.deb` linked in README | [matinlotfali/KDE-Rounded-Corners](https://github.com/matinlotfali/KDE-Rounded-Corners) |
| Sierra Breeze Enhanced | macOS-style traffic-light buttons | Build from source | [kupiqu/SierraBreezeEnhanced](https://github.com/kupiqu/SierraBreezeEnhanced) |
| Lightly | Original translucent style | Archived, skip it, use Darkly | [Luwx/Lightly](https://github.com/Luwx/Lightly) |

**Kvantum themes to pair with your palette:** [Catppuccin](https://github.com/catppuccin/kvantum), [KvLibadwaita](https://github.com/GabePoel/KvLibadwaita) (GNOME look), [Gruvbox](https://github.com/TheGlitchh/Gruvbox-Kvantum), plus the 20+ built-ins in `qt-style-kvantum-themes`. Kvantum Manager has a per-theme blur toggle.

**Built-in Breeze tricks:** System Settings > Window Decorations > Breeze > set button size, border "No borders", and enable "Draw a circle around close button" for an instant cleaner look.

## 04 // Icons, Cursors & Fonts

Icons and fonts are the cheapest, safest upgrade: no code runs, nothing breaks. Drop icon/cursor folders in `~/.local/share/icons`, fonts in `~/.local/share/fonts`, then `fc-cache -fv`.

**Icons**

| Pack | Vibe | Tier | Link |
| --- | --- | --- | --- |
| Papirus | The default answer; `sudo apt install papirus-icon-theme` | Popular | [repo](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme) |
| papirus-folders | Recolor Papirus folders to match your accent | Popular | [repo](https://github.com/PapirusDevelopmentTeam/papirus-folders), [Catppuccin version](https://github.com/catppuccin/papirus-folders) |
| Tela / Tela-circle | Bright, rounded, many colors | Popular | [Tela](https://github.com/vinceliuice/Tela-icon-theme), [Tela-circle](https://github.com/vinceliuice/Tela-circle-icon-theme) |
| Colloid | Flat, pastel, matches Colloid theme | Popular | [repo](https://github.com/vinceliuice/Colloid-icon-theme) |
| WhiteSur / McMojave-circle | macOS-style | Popular | [WhiteSur](https://github.com/vinceliuice/WhiteSur-icon-theme), [McMojave](https://github.com/vinceliuice/McMojave-circle) |
| Kora | Soft 3D-ish, very polished | Popular | [bikass/kora](https://github.com/bikass/kora) |
| Fluent / Qogir | Windows 11 feel / flat minimal | Popular | [Fluent](https://github.com/vinceliuice/Fluent-icon-theme), [Qogir](https://github.com/vinceliuice/Qogir-icon-theme) |
| Candy | Neon gradient icons, pairs with Sweet | Niche | [EliverLara/candy-icons](https://github.com/EliverLara/candy-icons) |
| Reversal | Colorful, many accent variants | Niche | [repo](https://github.com/yeyushengfan258/Reversal-icon-theme) |
| BeautyLine, YAMIS, Cyberpunk Technotronic | Neon line / monochrome / synthwave | Niche | [KDE Store](https://store.kde.org) |

**Cursors**

| Cursor | Vibe | Link |
| --- | --- | --- |
| Bibata | Rounded, the r/unixporn standard | [ful1e5/Bibata\_Cursor](https://github.com/ful1e5/Bibata_Cursor) |
| Catppuccin | Matches the palette | [catppuccin/cursors](https://github.com/catppuccin/cursors) |
| Phinger | Pointy, playful | [phisch/phinger-cursors](https://github.com/phisch/phinger-cursors) |
| Nordzy / Volantes | Nord / soft material | [Nordzy](https://github.com/guillaumeboehm/Nordzy-cursors), [Volantes](https://github.com/varlesh/volantes-cursors) |
| Breeze Hacked | Breeze cursor with custom colors | [clayrisser/breeze-hacked-cursor-theme](https://github.com/clayrisser/breeze-hacked-cursor-theme) |
| Apple | macOS cursor | [ful1e5/apple\_cursor](https://github.com/ful1e5/apple_cursor) |

**Fonts**

| Font | Use | Get it |
| --- | --- | --- |
| Nerd Fonts | Required for icons in prompts, fetch tools, TUIs | [ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts) releases |
| JetBrains Mono / Fira Code | Ligature terminal fonts | `fonts-jetbrains-mono`, `fonts-firacode` (apt) |
| Iosevka | Narrow, fits more on a laptop screen | [be5invis/Iosevka](https://github.com/be5invis/Iosevka) |
| Maple Mono | Rounded, cursive italics, very rice-y | [subframe7536/maple-font](https://github.com/subframe7536/maple-font) |
| Monaspace | 5 mixable families from GitHub Next | [githubnext/monaspace](https://github.com/githubnext/monaspace) |
| Cascadia Code | Microsoft's terminal font | [microsoft/cascadia-code](https://github.com/microsoft/cascadia-code) |
| Inter / Geist | UI font swap for a modern look | [rsms/inter](https://github.com/rsms/inter), [vercel/geist-font](https://github.com/vercel/geist-font) |

## 05 // Panels, Docks & Widgets

Panel Colorizer is the single biggest upgrade here: it turns plain Plasma panels into floating "islands", WM-style bars or docks. Latte Dock is dead; don't install it, Plasma's own panels replace it.

**Free built-in moves (no installs):** right-click panel > Edit Mode > Floating + width "Fit content" = instant macOS-style dock. Add a second thin panel at the top for a status bar. Swap the launcher via right-click > Show Alternatives > Application Dashboard (fullscreen).

| Widget | What it adds | Tier | Link |
| --- | --- | --- | --- |
| Panel Colorizer | Islands, per-widget colors, blur, shadows, presets, auto-switch when windows maximize | Popular | [luisbocanegra/plasma-panel-colorizer](https://github.com/luisbocanegra/plasma-panel-colorizer) |
| Application Title Bar | Window title + buttons inside the top panel (GNOME/macOS look) | Popular | [antroids/application-title-bar](https://github.com/antroids/application-title-bar) |
| Kurve | Audio visualizer bars in the panel (uses `cava`) | Popular | [luisbocanegra/kurve](https://github.com/luisbocanegra/kurve) |
| Resources Monitor | CPU / RAM / network graphs in the panel | Popular | [orblazer/plasma-applet-resources-monitor](https://github.com/orblazer/plasma-applet-resources-monitor) |
| Panel Spacer Extended | Spacer with mouse gestures and actions | Popular | [luisbocanegra/plasma-panel-spacer-extended](https://github.com/luisbocanegra/plasma-panel-spacer-extended) |
| Command Output | Shows any command's output in the panel: public IP, VPN, `tailscale status` | Niche, very cyber | [Zren/plasma-applet-commandoutput](https://github.com/Zren/plasma-applet-commandoutput) |
| Kara | i3/Hyprland-style workspace dots pager (now needs compiling) | Niche | [dhruv8sh/kara](https://github.com/dhruv8sh/kara) |
| Window Buttons / Window Title | Separate min-max-close and title applets | Niche | [applet-window-buttons6](https://github.com/moodyhunter/applet-window-buttons6), [window-title](https://github.com/dhruv8sh/plasma6-window-title-applet) |
| Tiled Menu | Windows 10-style tile start menu | Niche | [Zren/plasma-applet-tiledmenu](https://github.com/Zren/plasma-applet-tiledmenu) |
| Liquid Glass widgets | macOS Tahoe / iOS glass widgets (new) | Niche | [jaxparrow07/liquidglass-kde-widgets](https://github.com/jaxparrow07/liquidglass-kde-widgets) |
| Conky | Classic desktop system-stats overlay; `sudo apt install conky-all` | Classic | [brndnmtthws/conky](https://github.com/brndnmtthws/conky) (Wayland "with caveats") |

Also in Get New Widgets: Kpple Menu (Apple menu), Plasma Drawer (launcher), Modern Clock, Apdatifier (update notifier). Panel Colorizer and Kurve say to use a Plasma close to the latest; if the newest version errors on 6.3, install an older `.plasmoid` from the repo's Releases page.

## 06 // KWin Effects & Tiling

KWin effects are where KDE beats every other desktop for eye candy. Start with the built-ins (System Settings > Desktop Effects): Wobbly Windows, Magic Lamp, Fall Apart, Glide, Blur, Overview. Desktop Cube: enable it there if listed, otherwise build [zzag/kwin-effects-cube](https://github.com/zzag/kwin-effects-cube).

**Effects**

| Effect | What it looks like | Debian 13 (Plasma 6.3) | Link |
| --- | --- | --- | --- |
| Better Blur | Blur behind ANY window (frosted Konsole, Dolphin, Discord) | Build release `v1.3.6` (covers 6.0 to 6.3.5) | [taj-ny/kwin-effects-forceblur](https://github.com/taj-ny/kwin-effects-forceblur) |
| Better Blur DX | Maintained successor of Better Blur | Plasma 6.5+ only, so later | [xarblu/kwin-effects-better-blur-dx](https://github.com/xarblu/kwin-effects-better-blur-dx) |
| Glass | Apple "liquid glass" refraction + blur | Plasma 6.6+ Wayland only, so later | [4v3ngR/kwin-effects-glass](https://github.com/4v3ngR/kwin-effects-glass) |
| KDE Rounded Corners | Rounded, outlined windows | Debian 13 `.deb` in README | [matinlotfali/KDE-Rounded-Corners](https://github.com/matinlotfali/KDE-Rounded-Corners) |
| Burn My Windows | Windows open/close with Fire, Glitch, Doom, Hexagon, Energize | KWin 5.25+, KDE Store or GitHub | [Schneegans/Burn-My-Windows](https://github.com/Schneegans/Burn-My-Windows) |
| Geometry Change | Smooth animation when windows move/resize/tile | KWin script | [peterfajdiga/kwin4\_effect\_geometry\_change](https://github.com/peterfajdiga/kwin4_effect_geometry_change) |

**Tiling (keep KDE, get Hyprland-style workflow)**

| Tool | Style | Debian 13 | Link |
| --- | --- | --- | --- |
| Built-in tiling | Draw your own tile layout, Shift-drag to snap | Press `Meta+T` | Plasma |
| Krohnkite | Auto-tiling like dwm/i3, gaps, layouts | KWin 6 script, `kpackagetool6` | [anametologin/krohnkite](https://github.com/anametologin/krohnkite) |
| Karousel | Scrollable columns like niri/PaperWM | Extract to `~/.local/share/kwin/scripts/` | [peterfajdiga/karousel](https://github.com/peterfajdiga/karousel) |
| KZones | Windows FancyZones-style drop zones | KWin Scripts > Get New | [gerritdevriese/kzones](https://github.com/gerritdevriese/kzones) |
| Polonium | Polished auto-tiler | Needs Plasma 6.4+, so later | [zeroxoneafour/polonium](https://github.com/zeroxoneafour/polonium) |

After any Plasma upgrade, compiled effects (Better Blur, Rounded Corners) need a clean rebuild or reinstall, or they silently stop loading.

## 07 // Wallpapers (static, live, shader, auto-color)

The wallpaper sets the palette for everything else, so choose it early, then let a color generator theme the desktop from it.

**Static wallpaper repos (huge, curated)**

| Repo | Style |
| --- | --- |
| [dharmx/walls](https://github.com/dharmx/walls) | Massive categorized collection |
| [D3Ext/aesthetic-wallpapers](https://github.com/D3Ext/aesthetic-wallpapers) | Rice-friendly aesthetic picks |
| [FrenzyExists/wallpapers](https://github.com/FrenzyExists/wallpapers), [makccr/wallpapers](https://github.com/makccr/wallpapers), [mylinuxforwork/wallpaper](https://github.com/mylinuxforwork/wallpaper) | Mixed, popular with r/unixporn |
| [zhichaoh/catppuccin-wallpapers](https://github.com/zhichaoh/catppuccin-wallpapers), [orangci/walls-catppuccin-mocha](https://github.com/orangci/walls-catppuccin-mocha) | Catppuccin |
| [AngelJumbo/gruvbox-wallpapers](https://github.com/AngelJumbo/gruvbox-wallpapers) | Gruvbox |
| [linuxdotexe/nordic-wallpapers](https://github.com/linuxdotexe/nordic-wallpapers) | Nord |

**Live / animated (all free)**

| Tool | What it does | Link |
| --- | --- | --- |
| Smart Video Wallpaper Reborn | Video wallpaper on desktop + lock screen, pauses when windows cover it | [luisbocanegra/plasma-smart-video-wallpaper-reborn](https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn) |
| Shader Wallpaper | 270+ GLSL shaders, Shadertoy import, reacts to mouse and windows; Debian 13 build steps included | [y4my4my4m/kde-shader-wallpaper](https://github.com/y4my4my4m/kde-shader-wallpaper) |
| Waywallen | Wallpaper manager (image, video, Wallhaven plugins), Flatpak on Flathub | [waywallen/waywallen](https://github.com/waywallen/waywallen) |
| Dynamic Wallpaper | macOS-style wallpapers that shift with the sun/time | [zzag/plasma5-wallpapers-dynamic](https://github.com/zzag/plasma5-wallpapers-dynamic) (master = Plasma 6) |
| Wallhaven Reborn | Auto-rotates fresh wallpapers from Wallhaven | [Blacksuan19/plasma-wallpaper-wallhaven-reborn](https://github.com/Blacksuan19/plasma-wallpaper-wallhaven-reborn) |
| Wallpaper Effects | Blur/dim the wallpaper when windows are active | [luisbocanegra/plasma-wallpaper-effects](https://github.com/luisbocanegra/plasma-wallpaper-effects) |

**Colors from your wallpaper (auto-theming)**

| Tool | What it does | Link |
| --- | --- | --- |
| KDE Material You Colors | Generates Plasma light/dark color schemes from the current wallpaper (+ pywal) | [luisbocanegra/kde-material-you-colors](https://github.com/luisbocanegra/kde-material-you-colors) |
| pywal16 | Maintained pywal fork: terminal + app palettes from an image | [eylles/pywal16](https://github.com/eylles/pywal16) |
| matugen | Material You palette generator with templates for any app | [InioX/matugen](https://github.com/InioX/matugen) |

Original [pywal](https://github.com/dylanaraps/pywal) hasn't been updated in years; pywal16 is the active 16-color fork. Wallpaper Engine (paid) alternatives are in section 15.

## 08 // Boot & Login (GRUB, Plymouth, SDDM)

These run as root before your desktop exists, so take a Timeshift snapshot first and keep a live USB handy. Payoff: the machine looks custom from the first second.

**GRUB themes** (set `GRUB_THEME=` in `/etc/default/grub`, then `sudo update-grub`)

| Theme | Vibe | Link |
| --- | --- | --- |
| grub2-themes | Tela, Vimix, Stylish, WhiteSur; one install script | [vinceliuice/grub2-themes](https://github.com/vinceliuice/grub2-themes) |
| Elegant | Blurred wallpaper + floating menu | [vinceliuice/Elegant-grub2-themes](https://github.com/vinceliuice/Elegant-grub2-themes) |
| Fallout | Fallout terminal style, peak hacker vibe | [shvchk/fallout-grub-theme](https://github.com/shvchk/fallout-grub-theme) |
| Catppuccin | Palette-matched | [catppuccin/grub](https://github.com/catppuccin/grub) |
| Distro themes | Big distro logos (Debian included) | [AdisonCavani/distro-grub-themes](https://github.com/AdisonCavani/distro-grub-themes) |
| HyperFluent / Xenlism | Windows-11-ish / minimal | [Coopydood/HyperFluent-GRUB-Theme](https://github.com/Coopydood/HyperFluent-GRUB-Theme), [xenlism/Grub-themes](https://github.com/xenlism/Grub-themes) |
| Game/anime sets | Sekiro, Star Rail, anime | [sekiro](https://github.com/semimqmo/sekiro_grub_theme), [StarRail](https://github.com/voidlhf/StarRailGrubThemes), [13atm01](https://github.com/13atm01/GRUB-Theme) |
| Gorgeous GRUB | Curated list of dozens more | [Jacksaur/Gorgeous-GRUB](https://github.com/Jacksaur/Gorgeous-GRUB) |

Preview themes without rebooting: [hartwork/grub2-theme-preview](https://github.com/hartwork/grub2-theme-preview). Dual-boot tip: if Windows vanishes from the menu, add `GRUB_DISABLE_OS_PROBER=false` and rerun `update-grub`.

**rEFInd (prettier boot manager for dual boot):** `sudo apt install refind`, then theme it with [refind-theme-regular](https://github.com/bobafetthotmail/refind-theme-regular), [rEFInd-Minimal](https://github.com/EvanPurkhiser/rEFInd-Minimal) or [catppuccin/refind](https://github.com/catppuccin/refind).

**Plymouth (boot animation)**

- [adi1090x/plymouth-themes](https://github.com/adi1090x/plymouth-themes): huge collection ported from Android boot animations (angular, cuts, hexagon, etc.)
- [catppuccin/plymouth](https://github.com/catppuccin/plymouth)
- Debian steps: `sudo apt install plymouth`, copy the theme to `/usr/share/plymouth/themes/`, register it with `update-alternatives`, add `splash` to `GRUB_CMDLINE_LINUX_DEFAULT`, run `sudo update-grub && sudo update-initramfs -u`

**SDDM (login screen)**

| Theme | Vibe | Link |
| --- | --- | --- |
| sddm-astronaut | A series of Qt6 themes incl. animated wallpapers; README lists exact Debian 13 packages | [Keyitdev/sddm-astronaut-theme](https://github.com/Keyitdev/sddm-astronaut-theme) |
| SilentSDDM | Modern, very configurable (needs SDDM 0.21+) | [uiriansan/SilentSDDM](https://github.com/uiriansan/SilentSDDM) |
| Catppuccin | Palette-matched | [catppuccin/sddm](https://github.com/catppuccin/sddm) |
| Where Is My SDDM Theme | Ultra-minimal password-only | [stepanzubkov/where-is-my-sddm-theme](https://github.com/stepanzubkov/where-is-my-sddm-theme) |
| Sugar Dark / Chili | Classics (older, may need Qt5 bits) | [sugar-dark](https://github.com/MarianArlt/sddm-sugar-dark), [chili](https://github.com/MarianArlt/sddm-chili) |

**Splash screen** (the logo between login and desktop): System Settings > Colors & Themes > Splash Screen > Get New.

## 09 // Terminal & Shell Glow-Up

The terminal is in every screenshot, so it's worth 30 minutes. Fast win: `sudo apt install fastfetch starship btop zsh`, then pick a Starship preset.

**Terminal emulators**

| Terminal | Why | Link |
| --- | --- | --- |
| Konsole (built-in) | Profiles > Appearance: background blur + transparency, Catppuccin/Dracula schemes | [catppuccin/konsole](https://github.com/catppuccin/konsole), [dracula/konsole](https://github.com/dracula/konsole) |
| Yakuake | Quake-style drop-down terminal on F12; `sudo apt install yakuake` | KDE app |
| Kitty | GPU-fast, shows images, `kitty +kitten themes` browser | [kovidgoyal/kitty](https://github.com/kovidgoyal/kitty) |
| WezTerm | Lua-configured, tabs, multiplexing | [wez/wezterm](https://github.com/wez/wezterm) |
| Alacritty | Minimal, fast, TOML config | [alacritty/alacritty](https://github.com/alacritty/alacritty) |
| Ghostty | Newer native terminal, popular on r/unixporn | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) |

Color scheme dumps for every terminal: [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) (has Konsole/Kitty/WezTerm exports), [Gogh](https://github.com/Gogh-Co/Gogh).

**Shell + prompt**

| Tool | What it does | Install / Link |
| --- | --- | --- |
| Starship | Fast cross-shell prompt; presets like Tokyo Night, Gruvbox Rainbow, Pastel Powerline | `apt install starship` ([repo](https://github.com/starship/starship), [Catppuccin](https://github.com/catppuccin/starship)) |
| Oh My Zsh | Zsh plugin framework | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) |
| zsh-autosuggestions + syntax-highlighting | Fish-like grey suggestions and colored commands | [autosuggestions](https://github.com/zsh-users/zsh-autosuggestions), [syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) |
| Oh My Posh | Prompt engine with tons of themes | [JanDeDobbeleer/oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh) |
| Powerlevel10k | Iconic, but README says no new features are coming | [romkatv/powerlevel10k](https://github.com/romkatv/powerlevel10k) |
| Atuin | Searchable shell history with end-to-end encrypted sync | [atuinsh/atuin](https://github.com/atuinsh/atuin) |

**Prettier everyday CLI**

| Tool | Replaces | Link |
| --- | --- | --- |
| eza | `ls` with icons, colors, git status | [eza-community/eza](https://github.com/eza-community/eza) |
| bat | `cat` with syntax highlighting | [sharkdp/bat](https://github.com/sharkdp/bat) |
| zoxide + fzf | Smart `cd` + fuzzy finder | [zoxide](https://github.com/ajeetdsouza/zoxide), [fzf](https://github.com/junegunn/fzf) |
| btop / bottom | `top`, but gorgeous and themeable | [btop](https://github.com/aristocratos/btop) (`apt install btop`), [bottom](https://github.com/ClementTsang/bottom) |

**Fetch tools (the screenshot centerpiece)**

| Tool | Note | Link |
| --- | --- | --- |
| fastfetch | The standard now (neofetch is archived); `apt install fastfetch` on Debian 13, preset configs in repo | [fastfetch-cli/fastfetch](https://github.com/fastfetch-cli/fastfetch) |
| hyfetch | fetch with flag color gradients | [hykilpikonna/hyfetch](https://github.com/hykilpikonna/hyfetch) |
| pfetch / macchina | Tiny / fast and themeable | [pfetch](https://github.com/dylanaraps/pfetch), [macchina](https://github.com/Macchina-CLI/macchina) |
| onefetch | Fetch for a git repo (languages, authors) | [o2sh/onefetch](https://github.com/o2sh/onefetch) |
| neofetch-themes | Pre-made ASCII art fetch layouts | [Chick2D/neofetch-themes](https://github.com/Chick2D/neofetch-themes) |

**TUI apps that look amazing**

| App | What | Link |
| --- | --- | --- |
| Yazi | File manager with image previews | [sxyazi/yazi](https://github.com/sxyazi/yazi) |
| superfile | Colorful multi-panel file manager | [yorukot/superfile](https://github.com/yorukot/superfile) |
| lazygit / lazydocker | Git and Docker dashboards (good for your Docker box) | [lazygit](https://github.com/jesseduffield/lazygit), [lazydocker](https://github.com/jesseduffield/lazydocker) |
| Zellij / tmux | Multiplexers; tmux + [tpm](https://github.com/tmux-plugins/tpm) + [catppuccin/tmux](https://github.com/catppuccin/tmux) | [zellij](https://github.com/zellij-org/zellij) |
| Neovim distros | Instant IDE-looking Neovim | [LazyVim](https://github.com/LazyVim/LazyVim), [NvChad](https://github.com/NvChad/NvChad), [AstroNvim](https://github.com/AstroNvim/AstroNvim) |

## 10 // Hacker-Aesthetic Eye Candy

Pure "movie hacker" fun, plus real security tools that happen to look incredible. Most are one `apt install` away.

**Toys (zero purpose, maximum vibe)**

| Tool | What it does | Get it |
| --- | --- | --- |
| cool-retro-term | Glowing CRT monitor terminal (amber/green, scanlines, curvature) | `apt install cool-retro-term`, [repo](https://github.com/Swordfish90/cool-retro-term) |
| hollywood | Splits the terminal into panes of fake technobabble | `apt install hollywood` ([Debian](https://packages-pkgmirror-csail.debian.org/pt-br/trixie/s390x/games/hollywood)), [repo](https://github.com/dustinkirkland/hollywood) |
| no-more-secrets (`nms`) | The "Sneakers" movie decryption effect on any text: `ls -l \| nms` | [bartobri/no-more-secrets](https://github.com/bartobri/no-more-secrets) |
| genact | Fake activity: compiling, botnets, crypto mining | [svenstaro/genact](https://github.com/svenstaro/genact) |
| cmatrix / unimatrix / neo | Matrix rain, 3 flavours | `apt install cmatrix`, [unimatrix](https://github.com/will8211/unimatrix), [neo](https://github.com/st3w/neo) |
| cava | Terminal audio visualizer | `apt install cava`, [repo](https://github.com/karlstav/cava) |
| pipes.sh, asciiquarium, tty-clock, sl | Pipes screensaver, ASCII fish tank, big clock, steam train | [pipes.sh](https://github.com/pipeseroni/pipes.sh), [asciiquarium](https://github.com/cmatsuoka/asciiquarium), [tty-clock](https://github.com/xorg62/tty-clock), [sl](https://github.com/mtoyoda/sl) |
| figlet / toilet / lolcat | Big ASCII banners in rainbow | `apt install figlet toilet lolcat` |
| krabby | Random creature sprite on terminal start | [yannjor/krabby](https://github.com/yannjor/krabby) |
| wttr.in | Weather in the terminal: `curl wttr.in` | [chubin/wttr.in](https://github.com/chubin/wttr.in) |

**Real security/network tools that look amazing (screenshot AND study material)**

| Tool | What it does | Link |
| --- | --- | --- |
| Sniffnet | Gorgeous GUI network traffic monitor | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) |
| termshark | Wireshark-style TUI on top of tshark | [gcla/termshark](https://github.com/gcla/termshark) |
| trippy | Live traceroute + ping TUI with charts | [fujiapple852/trippy](https://github.com/fujiapple852/trippy) |
| gping | Ping with a live graph | [orf/gping](https://github.com/orf/gping) |
| bandwhich | Bandwidth per process / connection | [imsnif/bandwhich](https://github.com/imsnif/bandwhich) |
| wtf | Terminal dashboard of anything | [wtfutil/wtf](https://github.com/wtfutil/wtf) |

**Skip:** eDEX-UI, the famous sci-fi terminal, was archived in October 2021 ([repo](https://github.com/GitSquared/edex-ui)). An unmaintained Electron app is a real attack surface, so use cool-retro-term + btop + Sniffnet for the same look.

## 11 // App Theming (Firefox, Discord, Spotify, VS Code, Obsidian)

A themed desktop with a stock white browser breaks the illusion. Match each app to your section 02 palette.

| App | Mod / theme | Vibe | Link |
| --- | --- | --- | --- |
| Firefox | textfox | Makes Firefox look like a TUI, huge on r/unixporn | [adriankarlen/textfox](https://github.com/adriankarlen/textfox) |
| Firefox | Lepton (Firefox-UI-Fix) | Cleaner, tighter Proton UI | [black7375/Firefox-UI-Fix](https://github.com/black7375/Firefox-UI-Fix) |
| Firefox | ShyFox | Auto-hiding sidebar + toolbar (README: currently unmaintained) | [Naezr/ShyFox](https://github.com/Naezr/ShyFox) |
| Firefox | GNOME theme / Catppuccin | Libadwaita look / palette colors | [firefox-gnome-theme](https://github.com/rafaelmardojai/firefox-gnome-theme), [catppuccin/firefox](https://github.com/catppuccin/firefox) |
| Browser swap | Zen Browser | FOSS Firefox fork with vertical tabs and built-in theming | [zen-browser/desktop](https://github.com/zen-browser/desktop) |
| Discord | Vesktop + Vencord | Desktop client with plugins and CSS themes | [Vencord/Vesktop](https://github.com/Vencord/Vesktop) |
| Discord theme | system24 | TUI-style Discord | [refact0r/system24](https://github.com/refact0r/system24) |
| Discord theme | midnight / Catppuccin | Dark glassy / palette | [midnight](https://github.com/refact0r/midnight-discord), [catppuccin/discord](https://github.com/catppuccin/discord) |
| Spotify | Spicetify | Themes + extensions for the official client | [spicetify/cli](https://github.com/spicetify/cli) |
| VS Code | VSCodium + Catppuccin | FOSS build of VS Code, palette theme | [VSCodium](https://github.com/VSCodium/vscodium), [catppuccin/vscode](https://github.com/catppuccin/vscode) |
| Obsidian | Minimal / AnuPpuccin | Two of the most-used community themes | [kepano/obsidian-minimal](https://github.com/kepano/obsidian-minimal), [AnuPpuccin](https://github.com/AnubisNekhet/AnuPpuccin) |
| Flatpaks | Flatseal | Give Flatpak apps access to your GTK theme/fonts | [tchx84/Flatseal](https://github.com/tchx84/Flatseal) |

**Heads-up:** Vencord's own README states client mods are against Discord's Terms of Service (no known bans, but it's your call). ncspot (terminal Spotify) needs Spotify Premium, so it's out; see section 15.

**GTK apps on KDE:** System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style. For more Firefox inspiration, browse r/FirefoxCSS.

## 12 // Launchers & Niche Cool Software

KRunner (`Alt+Space`) is already excellent; the tools below are for a launcher that looks as good as it works, plus a few delightful oddities.

| Tool | What it does | Tier | Link |
| --- | --- | --- | --- |
| KRunner | Built-in launcher, calculator, unit converter, shell commands | Built-in | `Alt+Space` |
| Vicinae | Raycast-style command palette: apps, clipboard history, snippets, emoji, window switcher | Niche, rising | [vicinaehq/vicinae](https://github.com/vicinaehq/vicinae) |
| Kando | Radial pie menu that pops at your cursor, fully themeable | Niche, very cool | [kando-menu/kando](https://github.com/kando-menu/kando) |
| Albert / Ulauncher | Classic keyboard launchers with themes | Popular | [Albert](https://github.com/albertlauncher/albert), [Ulauncher](https://github.com/Ulauncher/Ulauncher) |
| Rofi | The r/unixporn launcher, but its Wayland support targets wlroots compositors | Popular (other WMs) | [davatorium/rofi](https://github.com/davatorium/rofi) |
| Shijima-Qt | Desktop mascots (Shimeji) that walk on your windows; supports Plasma 6 Wayland and X11 | Niche, adorable | [pixelomer/Shijima-Qt](https://github.com/pixelomer/Shijima-Qt) |
| KDE Connect | Phone notifications, clipboard, media control from your Android | Built-in | `apt install kdeconnect` |

**Dotfile managers (so your rice survives reinstalls)**

| Tool | Best for | Link |
| --- | --- | --- |
| Konsave | Whole-Plasma snapshots, export as `.knsv` | [Prayag2/konsave](https://github.com/Prayag2/konsave) |
| GNU Stow | Symlink normal config folders from a git repo | `apt install stow` |
| chezmoi | Templated dotfiles across machines, with secrets support | [twpayne/chezmoi](https://github.com/twpayne/chezmoi) |
| plasma-manager | Declarative KDE config (NixOS / home-manager only) | [nix-community/plasma-manager](https://github.com/nix-community/plasma-manager) |

A common pattern in the dotfiles repos below: Stow for terminal/shell configs, Konsave for Plasma state.

## 13 // Dotfiles Repos to Steal From

Almost every repo below targets Arch (AUR package names). On Debian, read their component list and install each piece from the links in sections 02 to 07; their Konsave/Stow files still apply.

**KDE Plasma 6 rices (with screenshots)**

| Repo | Look | Key parts |
| --- | --- | --- |
| [MrGilfy/umbra](https://github.com/MrGilfy/umbra) | Monochrome: pure black, white outlines, floating dock | Klassy, YAMIS icons, Ghostty, Konsave export |
| [anas1412/dotfiles](https://github.com/anas1412/dotfiles) | Tokyo Night on Wayland | Kvantum, kwin-effects-glass, Kitty, fish, Stow |
| [Blacksuan19/Dotfiles](https://github.com/Blacksuan19/Dotfiles) | Tiling-first "Plasma for twm users" | Krohnkite, Darkly, Rounded Corners, Colloid, Konsave + Stow |
| [Jarex985/kde-dotfiles](https://github.com/Jarex985/kde-dotfiles) | Modern Plasma 6.6 islands | Klassy, Panel Colorizer presets, Material You, Better Blur DX, Kurve |
| [Nadir-Alishly/kde-plasma-rice](https://github.com/Nadir-Alishly/kde-plasma-rice) | Step-by-step written guide | Floating dock, wallpaper-driven colors |
| [milomillow/kde-rice-dots](https://github.com/milomillow/kde-rice-dots) | Two rices, fetch-art focused | Fastfetch config |
| [Prayag2/kde\_onedark](https://github.com/Prayag2/kde_onedark) | One Dark global theme by the Konsave author | Theme + 4 wallpapers |
| [AlexNabokikh/nix-config](https://github.com/AlexNabokikh/nix-config) | Fully declarative KDE via plasma-manager | NixOS only, great to read |

**Older KDE rices (Plasma 5 era: inspiration, not copy-paste)**

| Repo | Note |
| --- | --- |
| [ComplexPlatform/KDE-dotfiles](https://github.com/ComplexPlatform/KDE-dotfiles) | 6 themed looks (Cherry Blossom, Urban, Coffee, Foggy Mountain...), uses Latte/Polybar |
| [ketgg/k-dots](https://github.com/ketgg/k-dots) | Aesthetic KDE, README warns Plasma 6 unsupported |
| [WillPower3309/dotfiles](https://github.com/WillPower3309/dotfiles) | KDE + i3 hybrid, Spicetify, Unimatrix |
| [yayuuu/my-configs](https://github.com/yayuuu/my-configs) | "My Plasma thinks it's GNOME" (repo has since moved to niri) |

**Curated lists (hundreds more, with images)**

| List | What's inside |
| --- | --- |
| [shvedes/awesome-kde](https://github.com/shvedes/awesome-kde) | KDE apps, plugins and resources for Plasma 6 |
| [0PandaDEV/awesome-unixporn](https://github.com/0PandaDEV/awesome-unixporn) | Best r/unixporn posts with dotfiles, grouped by DE/WM |
| [zemmsoares/awesome-rices](https://github.com/zemmsoares/awesome-rices) | Big screenshot gallery of rices + dotfiles |
| [fosslife/awesome-ricing](https://github.com/fosslife/awesome-ricing) | Every ricing tool, categorized |
| [webpro/awesome-dotfiles](https://github.com/webpro/awesome-dotfiles) | How to manage dotfiles well |

**Not KDE, but steal the colors and ideas:** [end-4/dots-hyprland](https://github.com/end-4/dots-hyprland), [HyDE](https://github.com/HyDE-Project/HyDE), [JaKooLit/Hyprland-Dots](https://github.com/JaKooLit/Hyprland-Dots), [mylinuxforwork/dotfiles](https://github.com/mylinuxforwork/dotfiles), [gh0stzk/dotfiles](https://github.com/gh0stzk/dotfiles) (18 bspwm themes), [rxyhn/yoru](https://github.com/rxyhn/yoru), [elenapan/dotfiles](https://github.com/elenapan/dotfiles), [adi1090x/polybar-themes](https://github.com/adi1090x/polybar-themes).

## 14 // Reddit Inspiration Gallery

Best workflow: open a post, read OP's "details" comment (they list theme, icons, widgets), then find each piece in this doc. Posts tagged `[KDE]` or `[Plasma]` on r/unixporn are the ones you can actually reproduce.

**r/unixporn KDE posts**

| Post | What to steal | Link |
| --- | --- | --- |
| "\[KDE\] My first rice" (1.7k upvotes) | Layan Kvantum + Arc Plasma style, centered dock | [post](https://www.reddit.com/r/unixporn/comments/1fvwbue/kde_my_first_rice/) |
| "\[KDE\] I love it" | Apple Sequoia global theme, Lightly transparency, BeautyDream icons, Fastfetch | [post](https://www.reddit.com/r/unixporn/comments/1fyyywo/kde_i_love_it/) |
| "\[KDE\] I just learned how to customize kde" | Edna global theme, SF fonts, Kitty + Starship | [post](https://www.reddit.com/r/unixporn/comments/1k1x2bq/kde_i_just_learned_how_to_customize_kde/) |
| "\[KDE\] My Plasma thinks it's Gnome" | GNOME-style top bar on Plasma | [post](https://www.reddit.com/r/unixporn/comments/1l96act/kde_my_plasma_thinks_its_gnome/) |
| "\[KDE\] Arch Linux" (Gruvbox) | Gruvbox Plasma theme in action | [post](https://www.reddit.com/r/unixporn/comments/tfh7l5/kde_arch_linux/) |
| "\[KDE\] First rice, how well did I do?" | Classic Plasma 5 Latte layout (ideas only) | [post](https://www.reddit.com/r/unixporn/comments/r2aqyd/kde_first_rice_how_well_did_i_do/) |
| "\[wmderland\] chill" | KDE + custom WM hybrid with dotfiles | [post](https://www.reddit.com/r/unixporn/comments/b7pbs8/wmderland_chill/) |
| Hyprland rice you can clone on KDE | EndeavourOS users say Panel Colorizer + Krohnkite gets you this look | [post](https://www.reddit.com/r/unixporn/comments/1fknhp2/hyprland_first_time_using_actual_arch_instead_of/) |

**r/kde threads worth bookmarking**

| Thread | Why | Link |
| --- | --- | --- |
| Panel Colorizer v1.0.0 released (448 upvotes) | Dev's own showcase + preset tips | [thread](https://www.reddit.com/r/kde/comments/1g5r6rs/panel_colorizer_v100_released/) |
| "Default panel look" | How to build the popular segmented panel | [thread](https://www.reddit.com/r/kde/comments/1gcin8t/default_panel_look/) |
| Monthly Screenshot Thread | Fresh Plasma desktops every month | [thread](https://www.reddit.com/r/kde/comments/1hju54e/monthly_screenshot_thread/) |
| "Do not install global themes" | The `rm -rf` incident, straight from the victim | [thread](https://www.reddit.com/r/kde/comments/1bixmbx/do_not_install_global_themes_some_wipe_out_all/) |
| plasma-manager on NixOS | Declarative KDE config deep-dive | [thread](https://www.reddit.com/r/NixOS/comments/1lbv8hn/ive_avoided_kde_for_years_because_of_dotfile/) |

**Bottomless galleries**

- [r/unixporn top KDE posts this year](https://www.reddit.com/r/unixporn/search/?q=KDE&sort=top&t=year) · [r/unixporn wiki](https://www.reddit.com/r/unixporn/wiki/index) · r/UsabilityPorn · r/FirefoxCSS
- [KDE Discuss: "Share your desktop!"](https://discuss.kde.org/t/share-your-desktop/490) (years of Plasma screenshots)
- [EndeavourOS: Share Your Desktop 2026](https://forum.endeavouros.com/t/share-your-desktop-2026/77330) (lots of Klassy + Panel Colorizer setups)
- [Plasma 6 dotfiles write-up ("Plasma-Round")](https://aolabs.dev/projects/kde-plasma-6-dotfiles/) (Stow + Konsave walkthrough)

## 15 // Paid → FOSS Swaps

Everything in this doc is free. These are the paid tools people often see in rice screenshots, and what to use instead.

| Paid thing | Why people want it | Free/FOSS swap |
| --- | --- | --- |
| Wallpaper Engine (Steam) | Animated / interactive wallpapers | [Smart Video Wallpaper Reborn](https://github.com/luisbocanegra/plasma-smart-video-wallpaper-reborn), [Shader Wallpaper](https://github.com/y4my4my4m/kde-shader-wallpaper), [Waywallen](https://github.com/waywallen/waywallen). Note: [linux-wallpaperengine](https://github.com/Almamu/linux-wallpaperengine) is FOSS but says you must own Wallpaper Engine for its assets |
| Spotify Premium (needed by ncspot) | Terminal Spotify client | [Spicetify](https://github.com/spicetify/cli) on the regular client, or your own music in [Elisa](https://github.com/KDE/elisa) / [Strawberry](https://github.com/strawberrymusicplayer/strawberry) |
| Raycast Pro / Alfred Powerpack (macOS) | Fancy command palette | [Vicinae](https://github.com/vicinaehq/vicinae), KRunner, [Albert](https://github.com/albertlauncher/albert) |
| Magnet / window snapping apps | Snap zones | [KZones](https://github.com/gerritdevriese/kzones), built-in `Meta+T` tiling |
| Stardock WindowBlinds / DeskScapes | Custom window skins, animated desktop | [Kvantum](https://github.com/tsujan/Kvantum) + Klassy, [Burn My Windows](https://github.com/Schneegans/Burn-My-Windows), live wallpapers above |
| iStat Menus | Pretty system stats | [Resources Monitor](https://github.com/orblazer/plasma-applet-resources-monitor) widget, [btop](https://github.com/aristocratos/btop), Conky |
| Operator Mono / MonoLisa / Berkeley Mono | Cursive-italic coding fonts | [Maple Mono](https://github.com/subframe7536/maple-font), [Victor Mono](https://github.com/rubjo/victor-mono), [Monaspace](https://github.com/githubnext/monaspace) |
| Apple SF Pro (license-restricted) | Clean macOS UI font | [Inter](https://github.com/rsms/inter), [Geist](https://github.com/vercel/geist-font) |
| Obsidian Sync | Sync your vault | Syncthing (you already use it) |
| Typora | Pretty Markdown editor | [Ghostwriter](https://github.com/KDE/ghostwriter) (KDE app) |
| Discord Nitro cosmetics | Custom look | Vesktop themes (ToS caveat in section 11) |

## 16 // Starter Rice Recipes (pick a column, follow it down)

Four complete looks built only from parts that work on Debian 13 / Plasma 6.3. Do one column top to bottom, `konsave -s <name>` it, then try another.

| Layer | NETRUNNER (cyberpunk) | MOCHA (Catppuccin) | CUPERTINO (macOS) | FJORD (Nord tiling) |
| --- | --- | --- | --- | --- |
| Colors | Cyberpunk Neon | catppuccin/kde Mocha | WhiteSur dark | Nordic or Utterly Nord |
| App style | Kvantum: CyberHack or Daemon-2.0 | Kvantum Catppuccin | Kvantum WhiteSur | Kvantum + Darkly v0.5.25 |
| Window deco | Klassy (plasma6.3 branch), neon outline | Breeze, no borders | Sierra Breeze Enhanced | Klassy, thin outline |
| Icons | Candy | Papirus + catppuccin folders | WhiteSur icons | Tela-circle (nord) |
| Cursor | Breeze Hacked (custom neon) | Catppuccin cursors | Apple cursor | Nordzy |
| Fonts | JetBrains Mono NF | Maple Mono NF + Inter | Inter / Geist | Iosevka NF |
| Panel | Panel Colorizer islands + Command Output (IP/VPN) | Panel Colorizer preset, floating | Top bar + Application Title Bar, floating "fit content" dock | Thin top bar + Kara pager |
| Effects | Better Blur v1.3.6, Burn My Windows "Glitch" | Rounded Corners, Magic Lamp | Rounded Corners, Magic Lamp, Glide | Krohnkite + Geometry Change |
| Wallpaper | Shader Wallpaper (matrix/neon shaders) | catppuccin-wallpapers | Dynamic Wallpaper (day/night) | nordic-wallpapers |
| Terminal | cool-retro-term for show, Kitty for work; btop, nms, hollywood | Konsole Catppuccin + Starship Catppuccin + tmux Catppuccin | Kitty + Starship, fastfetch | Kitty + Starship Nord-ish preset, Yazi |
| Apps | textfox, system24 Discord | catppuccin Firefox/Discord/VSCodium | Zen Browser, Vicinae | Lepton Firefox, lazygit |
| Boot/login | Fallout GRUB, adi1090x Plymouth, SilentSDDM | catppuccin grub + sddm + plymouth | WhiteSur GRUB (grub2-themes), astronaut SDDM | Elegant GRUB, Where-Is-My-SDDM |

Build order that minimizes breakage: colors > icons/cursor/fonts > Kvantum > window decoration > panels > effects > terminal > apps > boot/login last.

## Sources

Every GitHub link in this doc was checked to exist, and version notes come from each project's README, on 2026-10-30.

- [Debian Qt/KDE team: Trixie release plan](https://wiki.debian.org/PkgQtKde/TrixieReleasePlans) and [linuxiac: Debian 13 ships Plasma 6.3.6](https://linuxiac.com/?p=179486)
- [Debian Wiki: Plasma 6](https://wiki.debian.org/Plasma%206)
- [BleepingComputer: KDE theme wipes user's files](https://www.bleepingcomputer.com/news/linux/kde-advises-extreme-caution-after-theme-wipes-linux-users-files/)
- [Debian package: kvantum](https://packages.debian.org/src:kvantum), [Debian package: hollywood](https://packages-pkgmirror-csail.debian.org/pt-br/trixie/s390x/games/hollywood)
- [Wikipedia: KDE Plasma 6 release history](https://en.wikipedia.org/wiki/KDE_Plasma_6)
- READMEs for version limits: [Klassy](https://github.com/paulmcauley/klassy), [Darkly](https://github.com/Bali10050/Darkly), [Better Blur](https://github.com/taj-ny/kwin-effects-forceblur), [Better Blur DX](https://github.com/xarblu/kwin-effects-better-blur-dx), [Glass](https://github.com/4v3ngR/kwin-effects-glass), [Polonium](https://github.com/zeroxoneafour/polonium), [AeroThemePlasma](https://github.com/aeroshell-desktop/aerothemeplasma), [fastfetch](https://github.com/fastfetch-cli/fastfetch), [Starship](https://github.com/starship/starship), [Vencord](https://github.com/Vendicated/Vencord), [ncspot](https://github.com/hrkfdn/ncspot), [eDEX-UI](https://github.com/GitSquared/edex-ui)
- [KDE Store](https://store.kde.org) and [EndeavourOS "What is Ricing?" thread](https://forum.endeavouros.com/t/what-is-ricing/75569?page=2)
- Reddit posts: linked in section 14

---

### About this repo

Live site: deployed on Vercel from `index.html`. To rebuild the site after editing this README:

```bash
pip install markdown
python3 build/build.py README.md build/template.html index.html
```
