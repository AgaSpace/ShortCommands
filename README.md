# ShortCommands
A live ShortCommands plugin for Terraria.

## Overview
This plugin allows adding "commands" that are aliases of existing commands, typically for the purpose of "shortcut" commands, e.g., using /h instead of /history, or /bye <player> instead of /ban add <player> Goodbye!. You can also bind multiple commands to a single shortcommands using ';' as a separator.

These shortcut commands do not show up in the /help command list (mainly to avoid tons of different command aliases for the command being displayed). The shortcommands are configurable in the ShortCommands.json config file and can be reloaded live with /screload.

The commands also accept parameters. Use {0} {1} {2}, etc. to replace individual parameters, or {+} to insert the entire remaining parameter list.

Examples:
"bye": "ban add {0} Goodbye!"
>{0} would be replaced by the first given parameter, making "/bye Zaicon You suck!" execute as "/ban add Zaicon Goodbye!".​

"destroy": "killr {0} was destroyed by {+}"
>{0} would be replaced with the first given parameter, and {+} would be replaced with the rest of the parameters. "/destroy Zaicon a large fireball" would execute as "/killr Zaicon was destroyed by a large fireball".​

"kill": "killr {0} died by {+}"
>Nothing would happen, because ShortCommands will ignore any existing command.​

"lag": "butcher;clear item {0};clear projectile {0}"
>This would execute all three commands: /butcher, /clear item <some number>, and /clear projectile <same number>.​

## Permissions
shortcmd.reload: Allows reloading of the config file with /screload.

## Installation Guide
1. Place plugin dll into ServerPlugins folder.
2. Restart server.
3. Open ShortCommands.json, make any desired changes, save file, and execute /screload.

Source: [Short Commands | TShock for Terraria](https://tshock.co/xf/index.php?resources/shortcommands.10/)
