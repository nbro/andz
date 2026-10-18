# How to Release?

> We use [semantic versioning](https://semver.org/).

Once there are enough changes in `master`, we can release a new version.

1. Switch to the development branch:

   ```
   git switch master && git pull
   ```

2. Make sure it's up-to-date with the remote:
   ```
   git pull
   ```
3. Bump the version and create the release branch:
   ```
   poetry version patch
   git switch -c "rel-$(poetry version -s)"
   ```
   Use `poetry version minor` or `poetry version major` instead of `patch` when appropriate.
4. Add these changes:
   ```
   git add -u
   ```
5. Commit these changes:
   ```
   git commit -m "Bump andz version to $(poetry version -s)"
   ```
6. Push the release branch to the remote:
   ```
   git push --set-upstream origin HEAD
   ```
7. Create a PR and ask for code review.
8. Once the PR has been approved, merge the release branch into `master`.
9. Create a new tag:
   ```
   git tag "$(poetry version -s)"
   ```
10. Push it to the remote, which triggers the GitHub workflow that releases the package to PyPI:
    ```
    git push origin --tags
    ```
