# FolderSync

FolderSync is a Python-based utility that synchronizes folders between multiple locations or devices to maintain consistency on Windows systems.

## Features

- Synchronizes files and directories from a source folder to a destination folder.
- Copies new and modified files from the source to the destination.
- Removes files and directories that are only present in the destination folder.
- Maintains consistency between folders across different locations or devices.

## Requirements

- Python 3.x
- Compatible with Windows operating systems

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the `foldersync.py` file.

## Usage

To run the FolderSync program, use the following command format in your terminal or command prompt:

```bash
python foldersync.py <source_folder> <destination_folder>
```

- `<source_folder>`: The path to the source folder you want to synchronize from.
- `<destination_folder>`: The path to the destination folder you want to synchronize to.

### Example

```bash
python foldersync.py "C:\Users\YourName\Documents\Source" "D:\Backup\Destination"
```

This command will synchronize the contents of the "Source" folder with the "Destination" folder.

## Note

- The program will ensure that the destination folder has the same files and directories as the source folder.
- Files and directories present only in the destination will be removed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.