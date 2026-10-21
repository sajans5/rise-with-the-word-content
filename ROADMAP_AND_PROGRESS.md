# Rise With The Word — Roadmap & Progress Log

Last reviewed: 2026-10-21  
Content repository: https://github.com/sajans5/rise-with-the-word-content  
Android project: the uploaded `Rise_With_The_Word_Android_Studio_Project(9).zip`

## Verified live-feed baseline before this update
- 28 original Bible-story summaries
- 20 saint/feast entries
- 25 quiz questions
- 20 Catholic/Bible trivia facts
- Calendar pack is empty
- Readings pack contains two reference examples only; it is not a complete official lectionary and contains no full Bible text

## Current content additions prepared
- 19 additional original story summaries, prayers and lessons
- 15 additional quiz questions with answer indexes and explanations
- 15 additional trivia facts
- A license/provenance policy and this progress/roadmap document

These additions are in separate JSON files so they can be reviewed and merged without overwriting the existing feed.

## Roadmap
### P0 — feed integrity
- [x] Identify the live public content repository and inspect current file structure.
- [x] Record the baseline counts and the empty calendar-pack gap.
- [x] Prepare new data-only content packs.
- [x] Document provenance, verification, and checksum rules.
- [ ] Merge additions into the live JSON files and increment manifest versions.
- [ ] Verify GitHub Pages deployment and in-app Content Sync from an Android device.

### P1 — content growth
- [ ] Merge stories toward 100 well-reviewed stories.
- [ ] Merge quiz bank toward 100 questions and validate answer indexes.
- [ ] Merge trivia toward 100 facts.
- [ ] Add Malayalam translations after a competent Malayalam-language review.

### P2 — official readings and calendar
- [ ] Import only from an approved Indian Roman Rite Ordo / authorized data source.
- [ ] Record source URL, region, rite, and verification date for each date.
- [ ] Never describe continuous Bible reading as the official Mass lectionary.
- [ ] Keep Roman Rite, Syro-Malabar and Syro-Malankara data separate.

### P3 — Bible data
- [ ] Maintain explicit licence metadata per translation.
- [ ] Secure permission or identify a lawful redistribution route for a Catholic 73-book Malayalam text.
- [ ] Validate book, chapter and verse coverage after an authorized source is selected.

### P4 — Android release
- [ ] Correct the English passage asset generation/loading pipeline.
- [ ] Run JSON/data audits.
- [ ] Run GitHub Actions Android build and inspect its run logs.
- [ ] Install and test on a real Android device: Bible reader, language switch, Gospel navigation, offline mode, speech, sync, accessibility and private notes.
- [ ] Sign a release only after release keys and Play Store preparation are managed securely.

## Critical status distinction
The content repository is a public feed and is not the Android source repository. Changes to feed JSON can update an app configured to use that feed; they do not fix missing binary assets or Kotlin/HTML application defects by themselves.

## Change log
- 2026-10-21: Research confirmed candidate public Bible-data repositories but no third-party Bible text was copied because licence obligations and Catholic-canon completeness require further review. Identified that the live feed has no calendar records. Prepared 19 stories, 15 quiz questions and 15 trivia facts in append-only files. GitHub content-write API returned a 403, so no live repository commit was made.
