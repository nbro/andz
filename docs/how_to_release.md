# How to Release?

> We use [semantic versioning](https://semver.org/).

Once there are enough changes in `master`, we can release a new version

1. Switch to the development branch: `git switch master`
2. Make sure it's up-to-date with the remote: `git pull`
3. Create the release branch: `git switch -c rel-x.y.z`, where `x.y.z` is the new version of the package.
4. Set the new version: `poetry version x.y.z`.
5. Add these changes: `git add -u`
6. Commit these changes: `git commit -m "Bump andz version to x.y.z"`
7. Push them to the remote: `git push --set-upstream origin rel-x.y.z`
8. Create a PR and ask for code review
9. Once the PR has been approved, merge `rel-x.y.z` into `master`
10. Create a new tag `git tag x.y.z`
11. Push it to the remote `git push origin --tags`, which triggers the GitHub workflow that releases the package to PyPI

 [1]: https://github.com/nbro/andz/releases/new
