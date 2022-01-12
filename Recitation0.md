# Recitation 0: Demo Github Classroom

Please follow the directions below EXACTLY to complete this recitation successfully.

1. If you have not done so, head over to https://github.com and sign up for an account.  Please **USE YOUR DESU EMAIL ACCOUNT** when signing up for the account.<p/>
2. At this point, you should have a recent version of Python installed.
3. You will next need to accept the assignment in Github classroom and link it to your Github account.  Click on <a href="https://classroom.github.com/a/XLR34Otw">https://classroom.github.com/a/XLR34Otw</a>.  <p/>
5. Find your name in the list and select it.  IT IS IMPORTANT THAT YOU SELECT YOUR NAME FROM THE LIST!!!!!<p/>
6. Accept the assignment and wait a minute before refreshing the page.  You should now have a link to your own private repository that contains the assignment.<p/>
7. Click the link shown on the page.  Should you need the link in the future, simply click on the exercise link provided above to come back to this page.<p><image src="./images/step7.png" height="300"><p/>
8. You should now see your private repository with a green Code button on the top right as shown in the image below.<p><image src="./images/step8.png" height="300"></p>
9. You will now need to create a Github authentication token to be used in PyCharm.  Click on your avatar on the top right of the screen.  You should see a drop-down menu as shown in the image below.   Select  Settings. <p/><image src="./images/step9.png" height="300"></p>
10. On the Settings page, click on the Developer Setting menu item on the left as shown below.<p/><image src="./images/step9.png" height="300"></p>
11. On the next page, select the Personal Access Tokens as shown in the image below.<p/><image src="./images/step11.png"></p>
12. Then click on the Generate new token button on the top right as shown in the image below.<p/><image src="./images/step12.png"></p>
13. Enter the word PyCharm in the Note textbox and select the repo, workflow, gist, and read:org checkboxes as shown in the image below.  Also, for the expiration, select custom and enter December 31, 2021.  This will make your token valid for the entire course.<p/><image src="./images/step13.png"></p><p><image src="./images/step13-2.png" width="430px"style="margin-left:115px;"></p>
14. Click the green Generate Token button at the bottom of the screen.
15. Copy the token by clicking on the copy button as indicated in the image below.  You should store the token somewhere because you will not be able to recover it.  If you should forget it, you will need to regenerate a new token.<p/><image src="./images/step15.png"></p>
16. Now, open up PyCharm and click on Customize and then All Settings as shown in the  image below.<p/><image src="./images/step16.png" height="300"></p>
17. Expand the Version Control item on the left of the window and select Github.  Then click on the + as shown in the image below.<p/><image src="./images/step17.png" height="300"></p>
18. Select the Login with Token and paste your token in the Token textbox and click the Add Account button as shown in the image below.<p/><image src="./images/step17.png" height="300"></p>
19.  Now, go back to the assignment you accepted and click on the link so that you are in the repo for Demo Github Classroom.
20. Click the green code button and then copy the URL by clicking on the copy button as indicated in the image below.<p/><image src="./images/step20.png" height="250"></p>
21. Open up PyCharm and use the Get from VCS button to clone the repository.<p/><image src="./images/step21.png" height="300"></p>
22. Paste the assignment repository URL in the URL field and make sure to select the directory in which the assignment will sit.  Pycharm will add the name of repo to the Directory path.  If it does not, please add the name of the assignment directory.  For example, if the directory is <span style="color:blue;">C:\Users\JohnSmith\Documents</span>, make sure to add the name of the assignment.  In my case, this should be changed to <span style="color:blue;">C:\Users\JohnSmith\Documents\demo-github-classroom-rasamny</span>  <p></p><strong>Click the link to download and install Git, if asked.</strong><p><span style="color:red;"><strong>WARNING:</strong>  If you do not add a folder name, Pycharm will put all the project files in the Documents folder</span>.</p><p/><image src="./images/step22.png"></p>
23. Press the Clone button.  PyCharm will create the folder for you and place the assignment code in the folder you specified.
24. Your workspace should now look like the image shown below.<p/><image src="./images/step24.png"></p>
25. Now, to run and test the provided Python code, you will need to create a run configuration. Click on the run configuration button as shown in the image below.<p/><image src="./images/step25.png" height="400"></p>
26. Select Add New Configuration and then select Python from the menu as shown in the image below.<p/><image src="./images/step26.png" height="300"></p>
27. Give the configuration a name, for example <strong>Demo Test</strong>, and click on the folder at the right of the text box for <strong>Scirpt Path</strong>.  Select the *main.py* file.<p/><image src="./images/step27.png" height="300"></p>
28. Now press the green play button and notice that the test will fail.<p/><image src="./images/step28.png" height="350"></p>
29. Open the file demo.py and replace the pass line with the following code as shown in the figure below. Now run the test again by clicking on the green play button.  You should now see that the test succeeded!<p/><image src="./images/step29.png" height="350"></p>

30. Now that the tests have all passed, you now need to commit the changes you made and push the changes to your repository on Github. Select the Commit tab as  shown in the image below. <p/><image src="./images/step30.png" height="350"></p>
31. Select all the files that have changed and type a message in th text box as shown in the image, the message should summarize the work done at that point, and click commit and push button.<p/><image src="./images/step31.png" height="400"></p>
32. Click on the push button in the next window to complete the submission.<p/><image src="./images/step32.png" height="300"></p>
33. You should see a message that the files were pushed successfuly.  You can verify by looking at the Git log.  Click the Git tab on the bottom left as shown in the image below.<p/><image src="./images/step33.png" height="250"></p>
34. Go back to your repo on Github and make sure that you see a check mark indicating that everything passed.  You may need to reload the page to see any changes.  See image below. <p/><image src="./images/step34.png" height="200"></p>

### Congraulations!  You now have completed your first recitation!
src="./images/