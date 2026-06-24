# R-P-G (Raphael-Playing-Game) Manager

A small Python practice project created while refreshing Python fundamentals and learning object-oriented programming. The project was developed incrementally to explore classes, inheritance, JSON data storage, inventory systems, combat mechanics, and general software design principles.

## Features

- Create custom characters
- Save and load character data using JSON
- Interactive turn-based combat system
- Character status display
- Health and healing system
- Inventory system with item management
- Item usage and equipment mechanics
- Weapon swapping and equipment tracking
- Gold, rewards, and economy system
- Shop system for buying and selling items
- Town hub with training and exploration activities
- Training Grounds with configurable combat dummies
- Random enemy encounters
- Boss Rush endgame challenge
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
- Added reusable JSON-driven character loading utilities
- Extended save/load support to persist inventory and equipped items

### v0.5

- Reworked combat from an autobattler into an interactive turn-based system
- Added combat action menu (Attack, Use Item, Flee)
- Added gold currency system for characters
- Added enemy gold rewards on victory
- Added gold loss penalty on defeat
- Extended save/load support to persist character gold

### v1.0

- Added fully functional shop system
- Added item pricing and economy balancing
- Added item buying and selling mechanics
- Improved inventory navigation and usability
- Added Boss Rush challenge mode
- Added Bandit Leader final boss encounter
- Refined enemy rewards and progression pacing
- Improved combat and progression balancing through playtesting
- Added game completion and victory sequence
- Completed the core gameplay loop from character creation to final boss
