# AI for Professionals Training Program


Hello!

This repository contains all the training content that was covered during this
training program.

It is a mix of slides, source code, settings, scripts for installations, etc


## Setup Instructions

1. For most actions, API keys for common AI services would be needed. These were 
    already set for you in the lab machines. The two keys needed are:
    (please fill with appropriate values)
        OPENAI_API_KEY=sk-proj-xxx...
        ANTHROPIC_API_KEY=sk-ant-xxx..

2. For python based hands-on exercises, the Anaconda distribution needs to be 
    installed on your system: https://www.anaconda.com/download

3. Over and above the base anaconda distribution, some other packages are needed
    for generative and agentic use-cases. These are available to be installed 
    in scripts present in various place inside the `src/` folder. These are shell
    scripts that run on linux/unix systems. (Equivalent scripts for windows systems-
    batch or powershell- can easily be created by converting using ai services)

4. Wherever scripts are not present, a `requirements.txt` file is present. This is
    a standard file in the python world that indicates which packages and what
    versions of each are requirements for getting an application running well.
    The standard way of installing these dependencies on any platform is by using
    the following command on a command line/shell:
        `pip install -r requirements.txt`

5. Installation for the Worflow Automation AI solution (n8n) are non-trivial but are listed in an `n8n_lab_guide.html` document. A better option would be create a free account on https://n8n.io and try creating workflows there. It is same experience as the installed variant.

6. One specific topic that could not be covered during the program has been added
    in one folder: mcp. Please be advised that this is an advanced topic mainly
    focussed for techinicals and developers. The folder has its own installtion
    instructions in a `README.md` file.


Happy Learning!

Ashish Gulati
https://www.linkedin.com/in/ashishgulati/
