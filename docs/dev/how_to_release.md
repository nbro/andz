# How to Release?
 
Once there are enough changes in `dev` to release a new version, we can merge `dev` into `master`.  Here are the steps.

1. Checkout the development branch: `git checkout dev`
2. Make sure it's up-to-date with the remote: `git pull`
3. Create the release branch: `git checkout -b rel-x.y.z`, where `x.y.z` is the new version of the package. See [semantic versioning](https://semver.org/).
4. Update the `CHANGELOG.md` by adding a new section with the title `vx.y.z` with the new changes
5. Update the version of this package in `pyproject.toml` with `poetry version x.y.z`. 
6. Add these changes: `git add -u`
7. Commit these changes: `git commit -m "Bump ands version to x.y.z"`
8. Push them to the remote: `git push --set-upstream origin rel-x.y.z`
9. Ask for code review, if there's another developer
10. Once the PR has been approved, merge the changes into `dev` (**not** `master`)
11. Switch to `dev`: `git checkout dev`
12. `git pull`
13. Find out the hash of the commit mentioned above with `git log --oneline`
14. Tag that commit with `git tag vx.y.z <commit-hash>`
15. Make sure the commit has been tagged with `git log --oneline`
16. Push the tag to the remote: `git push --tags`
17. Make sure it have been pushed. If you find it [here](https://github.com/nbro/ands/tags), then it has been pushed.
18. `git checkout master`
19. Merge `dev` into `master`: `git merge dev`
20. Push these changes to the remote: `git push`
