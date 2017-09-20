#!/bin/bash

# check out the repository
git clone git@github.com:JamesSaxon/test.git 
cd test
git lg

# what's the status?
cat shopping_list1.md 

# I'm going to fix this
git checkout -b junk
echo "* ice cream"       >> shopping_list1.md 
echo "* cranberry juice" >> shopping_list1.md 

vi shopping_list.md   # delete bananas
cat shopping_list1.md # much better

git add shopping_list.md 
git commit -m "outstanding additions to a health lifestyle"
git lg

git checkout master
git pull
git lg # oh no, she's changed something!

# what has happened?
cat shopping_list.md 

# ok, my changes are safe
git checkout junk
cat shopping_list.md

# there are two branches now
git branch

# let's go back to the master branch and clean this up.
git checkout master

# not a smooth merge
git merge junk

# follow the instructions; clean up the merge
vi shopping_list.md 

# and commit it 
git add shopping_list.md 
git commit -m "compromise is healthy"

git lg # looks good!
git push # send it back to the server!

# get rid of the old branch
git branch -d junk

# looks good!
git lg
