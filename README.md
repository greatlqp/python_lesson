Create a new repository on the command line

echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/greatlqp/test.git
git push -u origin master