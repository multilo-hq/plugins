# Multilo plugins

Multilo's official plugin marketplace. Multilo adds it for you on first start (Customize → Plugins → Discover) and keeps its plugins up to date automatically.

## Layout

- `.multilo-plugin/marketplace.json`: the list of plugins.
- `plugins/`: plugins made by Multilo.
- `external_plugins/`: plugins from partners and the community, each reviewed before it is listed.

Each plugin is a folder:

```
my-plugin/
  .multilo-plugin/plugin.json   # name, version, description, author
  skills/<name>/SKILL.md
  commands/<name>.md
  agents/<name>.md
  hooks/hooks.json
  .mcp.json
  README.md
```

A skill on its own is published the same way: one skill, one plugin, named after the skill (a `skills/<name>/SKILL.md` and nothing else is a complete plugin). Multilo's marketplace lists plugins only.

Raise `version` in `plugin.json` with every change: Multilo updates a plugin when its version changes.

## Adding a plugin

1. Put the plugin folder in `plugins/` or `external_plugins/`.
2. Add an entry to `plugins` in `.multilo-plugin/marketplace.json`:

   ```json
   { "name": "my-plugin", "source": "./external_plugins/my-plugin", "description": "What it does", "version": "1.0.0", "category": "research", "author": { "name": "You" } }
   ```

   A plugin kept in its own repository can use `"source": { "source": "github", "repo": "owner/repo" }`.
3. Open a pull request. Every plugin and every update is reviewed before it is merged.

Plugins can run hooks and MCP servers on the user's computer. Multilo asks the user to approve each hook and each server before it runs.
