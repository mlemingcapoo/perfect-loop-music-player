# Perfect Loop Music Player

## Overview
This project is an audio/music player built in Python that can:
- Scan all available songs in a specified directory.
- Create and manage playlists with various playback options.
- Support looping modes, including custom loop points for precise track looping.

## Features
1. **Directory Scanner**
   - Automatically scans a folder to identify and load all audio files.
   - Extracts metadata like title, artist, and duration.

2. **Playlist Management**
   - Create and manage playlists dynamically.
   - Supports "Loop All" (entire playlist), "Loop One" (a single track), and custom looping points within a track.

3. **Custom Loop Points**
   - Define start and end points within a track to create seamless loops.

4. **Audio Playback**
   - Play, pause, stop, and seek functionality.
   - Displays current playback position and metadata.

## Requirements
- Python 3.9+
- Libraries:
  - `pygame` (for audio playback)
  - `mutagen` (for metadata extraction)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd music_player
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Build the executable:
    ```bash
   pyinstaller main.spec
   ```
3. Follow the prompts to:
   - Load a directory of songs.
   - Manage playlists.
   - Set playback and loop preferences.

## Next Steps
- Implement additional features, such as shuffling or saving playlists.

## Passion
- This project is made because I wanted to have a music player that loops through my favorite part of a song. It helped me focus more on working, so I hope it helps you focus too!

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

