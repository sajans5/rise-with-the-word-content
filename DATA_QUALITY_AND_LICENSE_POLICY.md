# Rise With The Word — Content Data Quality & Licence Policy

## Scripture and translation policy
1. Original summaries, reflections, prayers, quizzes and trivia may be written for this project, but Bible text must come from a specific, identified translation.
2. Before reproducing a translation, review the publisher's actual terms for digital redistribution and offline app embedding. A public repository does not automatically make its Bible text public domain.
3. Record translation name, source URL, licence, pinned version/commit and review date.
4. Never fill a missing passage with invented text or silently mix translations.
5. A passage reference is metadata, not the actual passage text.

## Catholic canon and calendar
- The Roman Catholic canon comprises 73 books. Catalogue presence does not prove text completeness.
- The existing Malayalam source in the Android project contains text for 66 books; Tobit, Judith, Wisdom, Sirach, Baruch, 1 Maccabees and 2 Maccabees remain missing from that dataset.
- Distinguish the General Roman Calendar from an India-specific or diocesan Ordo. Keep Roman Rite, Syro-Malabar and Syro-Malankara calendars separate.
- Record `sourceName`, `sourceUrl`, `verified`, `verifiedAt`, `rite`, `region` and notes where appropriate.
- Do not mark Mass readings verified until they have been checked against the applicable approved Ordo/lectionary.

## Feed validation
- JSON must parse as UTF-8.
- Story IDs must be unique; each story needs a title, reference, summary, lesson and prayer.
- Quiz questions need at least two options; `answer` must be an integer inside the options range; explanation must be non-empty.
- Trivia must be non-empty and factual claims should be checked before publication.
- Every manifest pack must point to an existing file. Increment version after changing pack contents.
- Optional SHA-256 must match the exact bytes served by GitHub Pages.
- Do not store personal prayers, journals, API keys, private data or executable code in public content packs.

## Public repositories reviewed during research
- https://github.com/godlytalias/Bible-Database — README declares GPL-3.0 and credits Wordproject; review obligations before redistribution.
- https://github.com/eldhosejoys/bible-data — README states source files came from VerseView and is framed as development data; that statement alone is not a clear redistribution licence.
- https://github.com/yesudas/all-bible-databases — do not assume one repository title establishes rights for every embedded translation.

No third-party Bible translation text is included in this update bundle.
