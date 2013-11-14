REM-PX
======

A Sublime Text plugin that allows easy conversion of rem to px and px to rem.

## Installation
You can easily install the pluing through Will Bond's excellent Package Control (https://sublime.wbond.net/).
If you want to install this plugin manually for some reason, simply clone this repo into your packages directory (make sure not to put it in the user sub dir).

## Instructions

### Converting px to rem
1. Select a px value (e.g. '16px')
2. Hit ctrl+shift+r by default (cmd+shift+r on Mac OS) to convert the value to rem. (Can also be done by selecting 'Convert highlighted px to rem' under the tools menu)

### Converting rem to px
1. Select a rem value (e.g. '1rem')
2. Hit ctrl+shift+x by default (cmd+shift+x on Mac OS) to convert the value to px. (Can also be done by selecting 'Convert highlighted rem to px' under the tools menu)

## Supported Features
- Convert px values to rem
- Convert rem values to px
- Checks to make sure the value is a valid px unit to convert to rem and visa versa

## Notes
1. The default size of 1rem is 16px which can be changed in the user settings.
2. All values will remove trailing zero's (e.g. '1.500rem' would become '1.5rem').

## Examples (1rem = 16px)

### Example 1 (rem to px)
```css
font-size: 1rem
```

Will convert to:
```css
font-size: 16px
```

### Example 2 (px to rem)

```css
font-size: 16px
```

Will convert to:
```css
font-size: 1rem
```
