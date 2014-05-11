An experiment with messaging and chatting.

Usage:
===========

    + Dependencies:

        ++ PyQt5.

        ++  Python3.

        ++ [restAssured](https://github.com/odeke-em/restAssured).

    + Firing it up:

        ++ With the [restAssured](https://github.com/odeke-em/restAssured) server

          fired up on your machine and accessible over
          ip, goto src/.
            
        ++ Run: python3 Workflow.py -h

                Usage: Workflow.py [options]

                Options:

                    -h, --help            show this help message and exit

                    -i IP, --ip=IP        IP on which the server is accessible

                    -p PORT, --port=PORT  IP address db connects to

                    -s, --secure          Set to False to use http instead of https


            eg python3 Workflow.py -i 192.168.1.106 -s False -p 8000
