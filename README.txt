RISE WITH THE WORD — STARTER CONTENT FEED

This folder is ready to publish with GitHub Pages. It contains:
- 28 original Bible story introductions with references, lessons and prayers
- 20 saint/feast entries for recurring calendar dates
- 25 Scripture quiz questions with answers and explanations
- 20 Catholic/Bible trivia facts
- Reading-reference metadata examples only (not full Bible text)
- A calendar pack placeholder; the app already includes a built-in liturgical calculation module

PUBLISH:
1. Create a public GitHub repository named rise-with-the-word-content.
2. Upload every file in this folder to the repository root (not the parent folder).
3. Go to Settings > Pages; choose Deploy from a branch, branch main, folder /(root), then Save.
4. Wait until GitHub Pages is published.
5. Your feed URL is https://YOUR-USERNAME.github.io/rise-with-the-word-content/manifest.json
6. In Rise With The Word, open Me > Settings > Content feed, paste that URL and Save.
7. Open Me > Content Sync and tap Check for updates now.

UPDATING CONTENT:
Whenever you change a JSON file, increase that pack's version in manifest.json and update its SHA-256 hash to match the file bytes. If you do not change the version, the app may keep the previously downloaded pack.

IMPORTANT:
- This starter pack uses the app's documented JSON shape. It does not yet include 3,500-word stories.
- Saint entries are a starter selection, not a complete official universal or Kerala diocesan calendar. Rank/color abbreviations follow the app template; verify local observances before release.
- Reading references are examples and must be checked against the correct local lectionary for each date. They are not full Gospel text.
- Use only Scripture translations and media that are licensed for in-app reproduction.
- Do not publish private prayer intentions, journal notes, or personal information in this public repository.
