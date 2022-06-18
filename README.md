# CamBot 6D for Star Citizen

**Six degrees of freedom spline interpolation with opentrack UDP-over-network output.**

With CamBot 6D, can remotely control the in-game camera position and orientation in all six degrees of freedom. Simply set individual waypoints and the software will move the in-game camera along a smooth path at a predefined speed.

You can also use CamBot 6D to split the advanced camera controls of Star Citizen between two real-time operators. One operator will control the camera angle around its pivot directly at the gaming PC, while the other controls the relative camera position and orientation remotely from a second computer.

# Features

Currently broken

# Dokumentation

A full walkthough of how to use CamBot 6D is on my website:

https://www.lordskippy.com/software/virtual-camera-robot

# What you need

### Requirements:

- opentrack: https://github.com/opentrack/opentrack/releases
- Star Citizen: https://robertsspaceindustries.com/enlist?referral=STAR-F3GJ-MFBD

### Optional:

- 3Dconnexion SpaceMouse (Enterprise, Pro, or Compact) for full analog 6 axis control
- Microsoft Xbox Controller (Series X, Series S, or One) for analog 5 axis control (digital control for roll)
- Elgato Stream Deck with  [MQTT plugin](https://apps.elgato.com/plugins/com.bi0s.mqtt)

# Changelog

Initial pre-release.

# Builds

We are in early testing. Alpha builds for Windows are available here:  

https://github.com/gulbrillo/CamBot-6D/releases

# Run

Requires Python 3.10 or higher.

> python3.10.exe .\main.py

# Compile

Spec file is provided. This will create a one file executable `main.exe` in `./dist`. 
> python3.10.exe -m PyInstaller main.spec

The spec file can be created with
> python3.10.exe -m PyInstaller --noconsole --onefile --windowed --icon=icon.ico --add-data "./images;images" main.py

But you need to replace the `datas` line in `main.spec` with this:
> datas=[('./images', 'images'),('./icons', 'icons'),('./fonts', 'fonts')],

# Acknowledgements

This is an unofficial Star Citizen fansite, not affiliated with the Cloud Imperium group of companies. All content on this site not authored by its host or users are property of their respective owners.

User interface based on [Simple_PySide_Base](https://github.com/Wanderson-Magalhaes/Simple_PySide_Base) and [Render_Time_Calculator](https://github.com/Wanderson-Magalhaes/Render_Time_Calculator) by Wanderson M. Pimenta.
