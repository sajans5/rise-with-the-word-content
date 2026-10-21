# Rise With The Word — content expansion bundle (2026-10-21)

This bundle is an upload-ready, reviewable supplement for the public content feed at
https://github.com/sajans5/rise-with-the-word-content

## What's new in the bundle
- `content/stories-additions.json`: 19 original Bible-story summaries with references, a practical lesson and a prayer.
- `content/quiz-additions.json`: 15 extra multiple-choice questions with answer indexes and explanations.
- `content/trivia-additions.json`: 15 additional educational facts.
- `merge_content_update.py`: safe merge helper for a local clone/download of the live feed. It preserves current entries, validates IDs and answer indexes, increments versions, and calculates exact SHA-256 hashes.
- `ROADMAP_AND_PROGRESS.md`: verified starting counts, milestones and status.
- `DATA_QUALITY_AND_LICENSE_POLICY.md`: data validation, licensing and Catholic-calendar safeguards.
- `AUDIT_REPORT.json`: research and status snapshot.

## Important
This does not itself change the live GitHub repository. The connected GitHub integration returned 403 when attempting a contents write, so no live commit was made. Upload files manually or grant a GitHub connection write permission, then merge the addition arrays into the existing JSON packs.
The bundle does not include full Bible translation text. Text from a translation should only be added after its redistribution licence and Catholic-canon coverage are verified.

## Merge workflow
1. Download/clone `rise-with-the-word-content`.
2. Copy `content/` and `merge_content_update.py` into a working folder.
3. Run `python3 merge_content_update.py /path/to/your/local/feed-folder`.
4. Review `CONTENT_UPDATE_REPORT.json` and inspect the JSON diffs.
5. Upload the modified `stories.json`, `quiz.json`, `trivia.json`, `manifest.json`, plus the progress/policy documents to the repository root.
6. If GitHub Pages is enabled, wait for deployment and test the manifest URL and Content Sync inside the Android app.

Do not mark the update complete until a live URL, checksums and Android sync have been verified.
