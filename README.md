# R-P-G (Raphael-Playing-Game) Manager

A small Python practice project created while refreshing Python fundamentals and learning object-oriented programming. The project is being developed incrementally to explore classes, inheritance, JSON data storage, inventory systems, and general software design principles.

## Features

- Create custom characters
- Save and load character data using JSON
- Turn-based combat system
- Character status display
- Health and healing system
- Inventory system with item management
- Item usage and equipment mechanics
- Gold and reward system
- Object-oriented item hierarchy using inheritance
- Town hub with training and exploration activities
- Random enemy encounters loaded from JSON
- Input validation with exception handling
- Interactive CLI menus

## Version History

### v0.1

- Implemented Character class
- Added combat system
- Added character creation
- Added health restoration and max health
- Added interactive CLI menu

### v0.2

- Added JSON save and load functionality
- Added character persistence between sessions
- Added inventory system
- Added item management (add, remove, view)
- Added Item class and template items
- Improved validation and error handling
- Added save option to the main menu
- Refactored character creation and loading logic

### v0.3

- Refactored inventory into a dedicated Inventory class
- Added Item inheritance hierarchy
- Implemented Potion and Sword item subclasses
- Added item usage functionality
- Added item database for dynamic item creation
- Added interactive inventory menu
- Refactored menu system into the Game class
- Reorganized project structure into source and data directories
- Improved code modularity and separation of responsibilities

### v0.3.5

- Implemented weapon equipment system
- Added weapon swapping functionality
- Prevented infinite attack stacking from repeated weapon use
- Added equipped weapon tracking for characters
- Improved inventory item selection using inventory slot IDs
- Added support for selecting items by both name and slot number
- Fixed duplicate-item selection and removal issues
- Fixed weapon swapping when inventory is at maximum capacity
- Improved item usage flow and success/failure handling
- Stabilized inventory and equipment edge cases

### v0.4

- Added Town of Gloosgaw hub area
- Added Training Grounds with configurable combat dummies
- Added Forest exploration with random enemy encounters
- Added JSON-based enemy system (Goblin, Wolf, Bandit)
- Refactored combat into a reusable fight sequence
- Added reusable JSON-driven character loading utilities
- Extended save/load support to persist inventory and equipped items

### v0.5

- Reworked combat from an autobattler into an interactive turn-based system
- Added combat action menu (Attack, Use Item, Flee)
- Added gold currency system for characters
- Added enemy gold rewards on victory
- Added gold loss penalty on defeat
- Extended save/load support to persist character gold
