#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ opstsetup.py                 [Update: 2022-05-27 | 23:50 PM]  #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of PSociety™ by MyMeepSQL}              #
#                                                                           #
#  The SetupTool for ODST                                                   #
#                                                                           #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © PSociety™, 2022 All rights reserved     #
#---[Operating System]------------------------------------------------------#
#  Developed for linux                                                      #
#---[Licence]---------------------------------------------------------------#
#  GNU General Public License v3.0                                          #
#  -------------------------------                                          #
#                                                                           #
#  This program is free software; you can redistribute it and/or modify     #
#  it under the terms of the GNU General Public License as published by     #
#  the Free Software Foundation; either version 2 of the License, or        #
#  (at your option) any later version.                                      #
#                                                                           #
#  This program is distributed in the hope that it will be useful,          #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#  GNU General Public License for more details.                             #
#                                                                           #
#  You should have received a copy of the GNU General Public License along  #
#  with this program; if not, write to the Free Software Foundation, Inc.,  #
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.              #
#---------------------------------------------------------------------------#

# Import Section
import urllib.request
import os
import sys
sys.path.insert(0, '/usr/share/OmegaPSToolkit/functions')
from functions.system_colors import system_colors as sc
from functions.abort import *
from functions.not_linux import *
from functions.internet_check import *
from functions.versions.opst_commands_version import opstsetup_version, opstconsole_version
from setuptools import setup,find_packages
from time import sleep
####


# The SetupTool
try:
    if os.getuid() != 0:    # check if the user run OPST with root privilege
        permerror =f"""
{sc.R}[!]{sc.W}  OPSTSetup could be run as the {sc.R}root user{sc.W} or with the {sc.R}sudo command{sc.W}
     Re-run the opstsetup with {sc.R}sudo{sc.W} or with the {sc.R}root{sc.W} user 
     Run : {sc.B}sudo opstsetup install{sc.W}
"""
        sys.exit(permerror)
except AttributeError:
    not_linux()
except EOFError:
    abort()
except KeyboardInterrupt:
    abort()
else:
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            long_description = fh.read()
        print()
        print(f"{sc.GR}{sc.D} _______ ______ _______ _______ _______         __               {sc.W}{sc.G}  OPSTSetup {sc.D}{opstsetup_version}")
        print(f"{sc.GR}{sc.D}|       |   __ \     __|_     _|     __|.-----.|  |_.--.--.-----.{sc.G}{sc.D}  Coded by MyMeepSQL for © PSociety™")
        print(f"{sc.GR}{sc.D}|   -   |    __/__     | |   | |__     ||  -__||   _|  |  |  _  |{sc.W}{sc.D}  A massive penetration testing toolkit")         # Font = Chunky from https://www.coolgenerator.com/ascii-text-generator
        print(f"{sc.GR}{sc.D}|_______|___|  |_______| |___| |_______||_____||____|_____|   __|{sc.C}{sc.D}  https://github.com/MyMeepSQL/OmegaPSToolkit{sc.W}")
        print(f"{sc.GR}{sc.D}  + -------- !* Welcome to the OPSTSetup. *! -------- +   |__|{sc.W}")
        print()
        print(f"{sc.G}[-]{sc.W}  Checking for internet connexion...")
        print()
        if internet_check() == True:
            print(f"+ -- --=[  Internet status.......... {sc.G}Connected{sc.W}.                                                                             ]")
            pass
        else:
            print(f"{sc.R}[!]{sc.W}   Internet status.......... {sc.R}Not connected{sc.W}.                                            ]")
            print(f"{sc.R}[*]{sc.W}   No Internet connexion found, please check you are connected to Internet and retry.  ]")
            sys.exit()
        print(f"+ -- --=[  {sc.underscore}The tool will:{sc.W}                                                                                                   ]")
        print(f"        [    ...Install {sc.G}Colored{sc.W}, {sc.G}Progress{sc.W}, {sc.G}psutil{sc.W}, {sc.G}GPUtil{sc.W}, {sc.G}tabulate{sc.W}, {sc.G}requests{sc.W}, {sc.G}py-cpuinfo{sc.W} and {sc.G}requests{sc.W} PIP3 modules         ]")
        print(f"                that OmegaPSToolkit must have and make a {sc.G}OmegaPSToolkit package{sc.W}.                                            ]")
        print()
        yn = str(input(f"{sc.C}[?]{sc.W}  Do you want to continue? [Y/n] "))
        if yn == 'y' or yn == 'Y' or not yn:
            pass
        else:
            abort()
        try:
            print()
            print(f"{sc.G}{sc.D}--------------------------------------------------------------------------------------{sc.W}")
            print()
            print(f"{sc.G}[-]{sc.W}  Installing all {sc.G}PIP3{sc.W} packages and make a {sc.G}OmegaPSToolkit package{sc.W}...")
            print()
            sleep(0.5)
            setup(classifiers=[
                    "Copyright                          :: Copyright © 2021-2022 , Thomas Pellissier aka MyMeepSQL from © PSociety™. All rights reserved.",
                    "Author name                        :: Thomas Pellissier",
                    "Developed for                      :: Linux",
                    "Development Status                 :: 2 - In Development",
                    "Natural Language                   :: English",
                    "Environment                        :: Terminal",
                    "Intended Audience                  :: Developers, Sec.",
                    "Programming Language               :: Python :: 3.8",
                    "Programming Language compatible    :: Python :: 3.1-3.x.x",
                    "Other Programming Language         :: Bash (Linux)",
                ],
                name='OmegaPSToolkit',
                description='A massive penetration testing toolkit',
                long_description = long_description,
                url='https://github.com/MyMeepSQL/OmegaPSToolkit',
                author='MyMeepSQL',
                author_email='thomas.pellissier@outlook.com',
                license='GNU-GPL-3.0',
                version=opstconsole_version,
                python_requires='>=3.1.0',
                packages=find_packages(),
                zip_safe=False,
                include_package_data=True,
                install_requires=[
                    'progress','colored','psutil','GPUtil','tabulate','requests','py-cpuinfo','requests','psutil','GPUtil'
                ],
            )
            print()
            print(f"{sc.G}[+]{sc.W}  Instalation complete.")
            sleep(1)
            print()
            print(f"{sc.G}{sc.D}--------------------------------------------------------------------------------------{sc.W}")
            print()
            yn = str(input(f"{sc.C}[?]{sc.W}  Do you want to reload your terminal (just in case) ? [Y/n] "))
            if yn == 'y' or yn == 'Y' or not yn:
                print()
                print(f"{sc.G}{sc.D}---------------------{sc.W}")
                print(f"{sc.G}[-]{sc.W}  Reloading...")
                print(f"{sc.G}{sc.D}---------------------{sc.W}")
                sleep(0.5)
                os.system("reset")
                print()
                print(f"{sc.G}{sc.D}-----------------------------------------------------------------------------------------------------------------------------------------{sc.W}")
                print()
                print(f"{sc.C}[OK]{sc.W}  All pip and {sc.G}OmegaPSToolkit{sc.W} PIP modules was succefully {sc.G}installed{sc.W}. Now you can run OPSTConsole with '{sc.B}sudo opstconsole{sc.W}'.")
                print()
                print(f"{sc.G}{sc.D}-----------------------------------------------------------------------------------------------------------------------------------------{sc.W}")
                print()
                sys.exit()
            else:
                print()
                print(f"{sc.G}{sc.D}--------------------{sc.W}")
                print(f"{sc.B}{sc.D}[+]{sc.W}  Answer: {sc.R}No{sc.W}.")
                print(f"{sc.G}{sc.D}--------------------{sc.W}")
                print()
                print(f"{sc.G}{sc.D}-----------------------------------------------------------------------------------------------------------------------------------------{sc.W}")
                print()
                print(f"{sc.C}[OK]{sc.W}  All pip and {sc.G}OmegaPSToolkit{sc.W} PIP modules was succefully {sc.G}installed{sc.W}. Now you can run OPSTConsole with '{sc.B}sudo opstconsole{sc.W}'.")
                print()
                print(f"{sc.G}{sc.D}-----------------------------------------------------------------------------------------------------------------------------------------{sc.W}")
                print()
                sys.exit()
        except EOFError:
            abort()
        except KeyboardInterrupt:
            abort()
    except EOFError:
        abort()
    except KeyboardInterrupt:
        abort()
####