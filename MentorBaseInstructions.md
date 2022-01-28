Getting started as a Team Illusion Programmer

First, you need to set up a local repository for this project.  Each programming system has an interface of some kind that you can use, but they will all follow this general guide.

The first six steps will be done once.  The remaining steps are repeated every time you submit
a change to the code or documentation

First, log on with the account that has permission to collaborate on the project.  The team's
lead programmer has control of permissions.

Fork the project repository by clicking the Fork button in the upper right corner.  This will create the copy of the project where you will submit your changes.  Once you have done that, you will see that you have a copy of RapidReact tied to your own account.


Clone your fork to the machine where you are going to be working.  You can do this from the command line, from within your IDE, or using the GIT Desktop Client.

On my computer I opened up a terminal prompt and navigated to my Python workspace and then executed "git clone https://github.com/TeamIllusion/RapidReact.git"

This act copied the repository files from github to my computer and put it into my local workspace under a folder named RapidReact.  If you execute the command "git status," you should see that you are on branch main and that the branch is up to date with origin/main.

If you execute the command "git  remote -v" you should see that the remotes for the clone are set to your fork of the project on github.  You should see the URL of your fork next to the word "origin".

Now you are going to add the Team Illusion repository as an "upstream" remote.  The command to accomplish this is "git remote add upstream https://github.com/TeamIllusion/RapidReact.git"

After this command is executed, you should see that the remote is your clone and there is now an upstream repository from TeamIllusion.

You are going to want to create a new branch for your work. The team will have to decide on naming conventions, but you create a new branch using the "git checkout -b"

I created a branch named mentor to hold any contributions I might make.  The first commit I make to that branch will be this document.  

The cycle you will go through for handling changes is to make sure that your repository is up to date with the masters. You do this by pulling the latest changes from upstream into your local repository - the command is "git pull."

In practice, you will use a text editor or IDE to add new code and modify old code. Because you checked out a branch to start with, any edits you make will only affect that branch.

After you make a set of changes and test them, use git add -A to stage your changes and git commit -m "DESCRIPTION OF CHANGES" to commit them.

My first commit to the new repository will be git commit -m "Add basic instruction set to repository".

Once you have committed the changes, you upload them to your fork using git push.  I will be using "git push origin mentor".


