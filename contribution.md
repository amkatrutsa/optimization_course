## Contributing

If you find any bugs, please fix them and send pull-request. 
If you want add some enhancement or something new, please open an issue for discussion. 

To send pull-request, you should make the following steps

1. Fork this repository
2. Clone the forked repository
3. Add original repositore as remote one 
4. Create a branch in your local repository with specific name for your changes, e.g. ```bugfix```
5. Switch to this branch
6. Change something that you assume make this repository better
7. Commit your changes in the branch ```bugfix``` with a meaningful comment, e.g. ```Fix typo```
8. Switch to the branch ```master```
9. Pull new commits to the branch ```master``` from this repository, not forked one
10. Switch to branch ```bugfix```
11. Make ```git rebase master``` to take all new commits from original repository to branch ```bugfix```
12. Make push to your forked repository in new remote branch ```bugfix```
13. Send pull-request from your remote branch ```bugfix``` to ```master``` branch of the original repository
