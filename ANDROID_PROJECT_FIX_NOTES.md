# Android Project — Findings and Next Fixes

Audited uploaded ZIP: `Rise_With_The_Word_Android_Studio_Project(9).zip` (project documents reference v4.6 progress).

## Screenshot issues to address
1. **Genesis screen says Bible text is added by GitHub Actions.** The APK needs an actual generated/bundled Bible database at the asset path expected by `app/src/main/assets/js/bible.js`. A workflow message is not a substitute for the asset. Review `tools/build_bible.py`, `tools/build_offline_bible_db.py`, `app/src/main/assets/js/bible.js`, and the read order in `index.html`; make CI build data into the exact expected path and fail if the full-English asset is missing.
2. **Today's Gospel English passage is empty.** The screen says text is not available in the bundled English Bible. Check the passage lookup interface used by `readings.js` against the actual exported Bible object; avoid a second name/shape assumption. Add a fixture check for Matthew 11:1–5 and Genesis 6:5–9:17 after building data.
3. **Bible catalogue shows 73 books but Malayalam text only for 66.** The catalogue UI must distinguish the seven missing-text books and never imply 73-book text completeness. A compatible Catholic Malayalam source needs licence and coverage verification first.
4. **Daily Gospel says continuous Bible plan — NOT official Mass lectionary.** Preserve this distinction. Do not silently display a sequential Gospel chapter as the liturgical Mass Gospel.
5. **No verified Android build was run in this environment.** The workflow below is a candidate CI workflow. It must be committed and tested in GitHub; a green CI run and real-device test are still required.

## Proposed build pipeline
- Run all current project data audits.
- Run the existing Bible build scripts with explicit, lawful source inputs.
- Assert exact expected output path and a nonempty dataset.
- Assert the English passage lookup function returns text for representative Genesis and Gospel references.
- Build debug APK and upload as an Actions artifact.

## Critical warning
The supplied archive does not contain a GitHub Actions workflow under `.github/workflows/` or the Gradle wrapper (`gradlew` and `gradle/wrapper`). This means the current README workflow instructions are not reproducible from this ZIP alone. Add a standard Gradle wrapper in Android Studio or commit the existing wrapper from the source repository before expecting GitHub Actions to build. The workflow file in this bundle includes an explicit failure if both are absent, rather than presenting a false green build.
