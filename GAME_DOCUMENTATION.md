# Word Morph Game Documentation

## Overview
This is a word-morphing game where players start with the word "HOUSE" and create new valid words by changing one letter at a time. The game tracks the chain of valid words and provides definitions for each word.

## Components Breakdown

### 1. HTML Structure & Styling


- Uses a modern, dark-themed UI with CSS variables for consistent styling
- Responsive design with mobile support
- Features gradient effects and smooth animations
- Contains three main sections: info box, game area, and stats

### 2. Game State Management


- Tracks current and previous words
- Maintains chain length (score)
- Stores discovered words to prevent duplicates

### 3. Core Game Mechanics

#### Letter Selection
- Players select one letter at a time
- Letter is validated against a dictionary
- If valid, it's added to the chain
- If invalid, an error message is displayed


- Allows players to click/tap letters to change them
- Uses a hidden mobile input for better mobile keyboard support

#### Word Validation


- Validates words using the Dictionary API
- Provides visual feedback (green for valid, red for invalid, orange for duplicates)
- Shows word definitions when valid
- Prevents duplicate words

### 4. UI Updates


- Renders letter boxes
- Updates chain length and possible words count
- Provides visual feedback for word validity

### 5. Mobile Support
- Hidden input field for mobile keyboard handling
- Maintains keyboard focus for smooth mobile experience
- Handles keyboard show/hide events

## Key Features
1. Real-time word validation
2. Word definitions display
3. Chain length tracking
4. Duplicate word prevention
5. Visual feedback for actions
6. Mobile-friendly design
7. Responsive layout

## Technical Implementation
- Uses vanilla JavaScript (no frameworks)
- Async/await for API calls
- Event delegation for letter selection
- CSS variables for theming
- Local state management
- DOM manipulation for UI updates

This game combines word puzzle mechanics with educational elements (definitions) while maintaining a modern, responsive user interface suitable for both desktop and mobile play.

