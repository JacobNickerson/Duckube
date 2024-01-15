<!-- ABOUT THE PROJECT -->
## About The Project

Duckube

Duck-themed discord bot created using the Pycord library, intended for private use on the Sling Bingers minecraft server.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Written In

[![Python][Python-shield]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

All necessary libraries are included in requirements.txt; FFMPEG is also required for commands that play sounds in voice channels.

### Prerequisites

* requirements.txt
  ```sh
  pip -r requirements.txt
  ```
* [FFMPEG](https://ffmpeg.org/download.html)
  ```sh
  Download from: https://ffmpeg.org/download.html
  ```
* Discord Bot Token

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JacobNickerson/duckube
   ```
2. Install requirements.txt
   ```sh
   pip -r requirements.txt
   ```
3. Install [FFMPEG](https://ffmpeg.org/download.html) into the cloned repository
4. Discord Bot Token should be obtained from Discord application developer portal
5. Create a file named ".env" and enter the following variables:
   ```sh
   discord_token=bot_token_here
   discord_server_token=discord_guild_token_here
   ```
6. For functions made specifically for the Sling Bingers server (start_server, waypoint, etc.) the following variables are also written in .env:
   ```sh
   owner_token=server_admin_id_here
   rcon_password=minecraft_server_rcon_password_here
   directory=server_jar_location_here
   coords_channel_id=channel_id_for_overworld_coordinates_chat
   nether_channel_id=channel_id_for_nether_coordinates_chat
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

tbd

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Jacob Nickerson - jacobnickerson817@gmail.com

Project Link: [https://github.com/JacobNickerson/Duckube](https://github.com/JacobNickerson/Duckube)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/

