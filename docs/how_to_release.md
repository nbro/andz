# How to Release?

> We use [semantic versioning](https://semver.org/).

Once there are enough changes in `master`, we can release a new version.

1. Switch to `master` and pull

   ```
   git switch master && git pull
   ```

2. Bump the version and create the release branch:
   ```
   poetry version patch && git switch -c "rel-$(poetry version -s)"
   ```
   Use `poetry version minor` or `poetry version major` instead of `patch` when appropriate.
3. Add these changes:
   ```
   git add -u
   ```
4. Commit these changes:
   ```
   git commit -m "Bump andz version to $(poetry version -s)"
   ```
5. Push the release branch to the remote:
   ```
   git push --set-upstream origin HEAD
   ```
6. Create a PR, ask for code review, and merge into `master` once approved
7. Create a new tag in `master`, and push it to trigger the release workflow that publishes to PyPI:
   ```
   git switch master && git pull && git tag "$(poetry version -s)" && git push origin --tags
   ```
