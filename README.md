# CORRECT ME! [![GitHub Release](https://img.shields.io/github/v/release/farid-rajabi/correct-me)](https://github.com/farid-rajabi/correct-me/releases/latest)

[![GitHub License](https://img.shields.io/github/license/farid-rajabi/correct-me)](https://github.com/farid-rajabi/correct-me/blob/main/LICENSE)

This app is created to assist language learners with their writing issues, especially the spelling of words. It supports all the languages supported by Google Translate.

**Available for ![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black) and ![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white).**

## Screenshots

<p align="center">
<img src="./screenshots/1.png" alt="Screenshot 1" width="500"/>
</p>

<p align="center">
<img src="./screenshots/2.png" alt="Screenshot 2" width="500"/>
</p>

## Installation

Regardless of the method that you choose to install the app, [Python 3.x](https://www.python.org) should be installed on your system. (The latest stable version is preferable.)

You can decide whether to install it using [*Correct Me! Installer*](https://github.com/farid-rajabi/correct-me-installer) or do it [manually](#manual).

### Correct Me! Installer

1.  Download the [latest release of *Correct Me! Installer*](https://github.com/farid-rajabi/correct-me-installer/releases/latest).

2.  Extract it and put the directory wherever you want.

> [!NOTE]
> The installation requires internet connection.

> [!IMPORTANT]
> Read the [*Requirements* section of *Correct Me! Installer*](https://github.com/farid-rajabi/correct-me-installer) before proceeding to the next step.

3.  If you are on **Linux**:

    1.  Right click on *installer-linux.sh*, then click on *Run as a Program*.

    2.  Wait until the *Installation is completed* message is printed in the terminal.

    If you are on **Windows**:

    1.  Double click on *installer-windows.bat*.

    2.  Wait until the *Installation is completed* message is printed in the cmd/powershell.

> [!TIP]
> Do not ignore the log. In case a problem occurs, the solution will be printed for you.

### Manual

1.  The following Python packages are required:

    - [gTTS](https://pypi.org/project/gTTS)
    - [playsound](https://pypi.org/project/playsound)

    Use the following commands to download and install the packages:

    ```
    pip install gTTS
    pip install playsound
    ```

> [!TIP]
> If you are using Python 3.x, you might have *pip3* instead of *pip* depending on your OS.

> [!TIP]
> In case the installation of *playsound* goes wrong, take a look at the [*Troubleshoot* section](#troubleshoot).

2.  Download the [latest release of *Correct Me!*](https://github.com/farid-rajabi/correct-me/releases/latest). Extract it and put the directory wherever you want.

3.  If you are on **Linux**:

    1.  Open the app directory.

    2.  Open *CorrectMe.sh* with a text editor.

    3.  Change the line

        ```sh
        cd .
        ```

        to

        ```sh
        cd "/path/to/correct-me/dir"
        ```

        where `/path/to/correct-me/dir` is the absolute path of the *Correct Me!* root directory.

    4.  Create a shortcut to *CorrectMe.sh*.

    If you are on **Windows**:

    1.  Open the app folder.

    2.  Open *CorrectMe.bat* with a text editor.

    3.  Change the line

        ```bat
        CD .
        ```

        with

        ```bat
        CD "\path\to\correct-me\dir"
        ```

        where `\path\to\correct-me\dir` is the absolute path of the *Correct Me!* root folder.

    4.  Create a shortcut to *CorrectMe.bat*.

> [!WARNING]
> Like what you see above, double quotation marks should surround the path, avoiding any possible issues due to spaces in the path.

## How to Use

1.  Create a text file. (The extension is optional.)

2.  Write the words/phrases you want to practice their spelling in it.

2.  Run the program.

> [!NOTE]
> The app requires internet connection, UNLESS you have gone the file specified in step 1 AT LEAST ONCE AND HAVE NOT CHANGED IT.

3.  Read the Attention and Help banners before proceeding.

4.  Specify the text file by its location and the language.

5.  Write what you hear and then press *Enter*.

## Troubleshoot

### *playsound* Installation Failed

It is possible to encounter with the following error while trying to install *playsound* manually.

```
Collecting playsound
Downloading playsound-1.3.0.tar.gz (7.7 kB)
Installing build dependencies ... done 
Getting requirements to build wheel ... error
error: subprocess-exited-with-error
```

Do what follows to solve the problem:

1.  Run the following commands.

    ```
    pip install --upgrade wheel
    pip install setuptools
    ```

2.  Try `pip install playsound` again.

Thanks to [Christopher](https://stackoverflow.com/a/77231478/14265483).

## Test Results

| Version | Configurations | Result |
| --- | --- | --- |
| 1.3.1 | ![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04.4_LTS-E95420?logo=ubuntu) ![Python](https://img.shields.io/badge/Python-3.10.12-3776AB?logo=python) ![GNU Bash](https://img.shields.io/badge/GNU_Bash-5.1.16-4EAA25?logo=gnubash) ![gTTS](https://img.shields.io/badge/gTTS-2.5.1-blue) ![playsound](https://img.shields.io/badge/playsound-1.3.0-blue) | ![Result](https://img.shields.io/badge/Passed-green) |
