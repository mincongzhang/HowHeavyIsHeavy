UnderGraFinalProject
====================

This repo contains the code for the research "The influence of amplifier settings on the perception of ’heaviness’ in guitar timbre".

Just Noticeable Difference pre-experiment is carried out using the software Reaper. The scripts for randomly generating test audios, and for generating final 1000 audios with different parameters are in the PythonScript folder.  (Reaper only support Python3.1 and above version)

Web Based Listening experiment is carried out via a website, designed in Django (Django web framework needs Python version under 3.0, e.g. Python2.6 or Python2.7). The website has a register system, requiring user to register and login, so that to randomly provides certain number of audios for comparing. The result is saved in question.db3.

Final data and analysis are in the MatlabScript folder.

<img src="https://github.com/mincongzhang/UnderGradFinalProject/raw/master/JND_4params.jpg" width="300"/>
<img src="https://github.com/mincongzhang/UnderGradFinalProject/raw/master/heaviness.jpg" width="300"/>


### new idea

use music scale to detect music genre
