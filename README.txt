PRIVATE FOLDER. NEVER upload this folder to GitHub.

1. Put your masked image exports in private/images (hero.png, canvas.png, vsm.png, personas.png, journey.png, impact.png).
   Use 1x exports or JPG to keep file sizes small.
2. From inside private, run:  python3 embed-images.py
3. From the main site folder (the one holding index.html), run:
   npx staticrypt private/case-study.html -d . --short --remember false --template-title "Case study" --template-instructions "Enter the password I shared with you." --template-color-primary "#2b44ff" --template-color-secondary "#f5f6f9"
   It asks you for the password. Choose a long passphrase of 4 or more random words.
4. Upload only index.html, the new case-study.html (the encrypted one), and resume.pdf to GitHub.
