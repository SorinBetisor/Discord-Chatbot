# Discord Bot with Prefix Management and Role Assignment

This project is a Python-based Discord bot built with `discord.py`. The bot features dynamic prefix management, cog-based modularity for commands, and automatic role assignment for new members. It includes several owner-specific commands for loading, unloading, and reloading bot extensions.

## Features

- **Dynamic Prefix Management**: Each server (guild) can have its own custom command prefix, which is stored and retrieved from a JSON file.
- **Cog-based Commands**: Commands are organized into cogs, allowing for modularity and easy management.
- **Automatic Role Assignment**: Automatically assigns a predefined role ("Member") to users who join the server.
- **Error Handling**: Provides feedback for command errors, including missing arguments, invalid commands, and permission issues.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `discord.py` library (`pip install discord.py`)
- `numpy` library (`pip install numpy`)

### Setup
   ```bash
   git clone https://github.com/yourusername/discord-bot.git
   pip install discord.py numpy

    Create a prefixes.json file in the root directory to store server-specific prefixes. Example content:
    {
    "server_id": "!"
    }
```

###Owner commands
```bash
!load <extension_name>
!unload <extension_name>
!reload <extension_name>
```

###Handling Errors
Common error cases are handled gracefully:

CommandNotFound: Notifies the user when an invalid command is used.
MissingRequiredArgument: Prompts the user to provide the required argument.
MissingPermissions: Alerts the user if they don't have the required permissions.

###Contributing
Feel free to fork the repository, submit issues, and make pull requests to improve this bot. Contributions are welcome!
