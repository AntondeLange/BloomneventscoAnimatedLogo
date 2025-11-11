# Configuration Guide

## Quick Reference for Adjusting Animations

All animation parameters are now centralized in the `CONFIG` object at the top of `app_cleaned.js`. This makes it easy to adjust timing, speeds, and positions without hunting through the code.

## Configuration Object

```javascript
const CONFIG = {
  ANIMATION: {
    GUST_DURATION: 1.6,              // How long lily/daisy sway takes (seconds)
    GUST_COOLDOWN_MS: 1000,          // Delay before sway can retrigger (milliseconds)
    BUTTERFLY_FLIGHT_DURATION: 12.0, // How long butterfly takes to fly across screen (seconds)
    BUTTERFLY_WAVE_AMPLITUDE: 50,    // Height of butterfly's up/down movement (pixels)
    BUTTERFLY_WAVE_FREQUENCY: 5,     // Number of zigzag cycles across screen
    SEED_DRIFT_DURATION: 3.0,        // How long seed floats away when clicked (seconds)
    SEED_AUTO_HIDE_DELAY: 3000,      // How long seeds stay visible after hover ends (milliseconds)
    LABEL_FADE_DURATION: 0.6,        // How long labels take to fade in/out (seconds)
    HOVER_DEBOUNCE_MS: 100           // Delay to prevent hover flicker (milliseconds)
  },
  POSITIONS: {
    DANDELION_HIT_PADDING: 5,              // Padding around dandelion hit area (pixels)
    BUTTERFLY_LABEL_OFFSET_Y: 50,          // Distance of "Contact Us" label above butterfly (pixels)
    SEED_LABEL_OFFSET_X: 40,               // Distance of seed labels to the right (pixels)
    SEED_LABEL_OFFSET_X_CAPABILITIES: 85   // Special offset for "Capabilities" label (pixels)
  }
};
```

## Common Adjustments

### Make Animations Faster
```javascript
BUTTERFLY_FLIGHT_DURATION: 8.0,  // Change from 12.0 to 8.0 (50% faster)
SEED_DRIFT_DURATION: 2.0,        // Change from 3.0 to 2.0
GUST_DURATION: 1.2,              // Change from 1.6 to 1.2
```

### Make Animations Slower
```javascript
BUTTERFLY_FLIGHT_DURATION: 16.0, // Change from 12.0 to 16.0 (33% slower)
SEED_DRIFT_DURATION: 4.0,        // Change from 3.0 to 4.0
GUST_DURATION: 2.0,              // Change from 1.6 to 2.0
```

### Adjust Butterfly Flight Pattern
```javascript
BUTTERFLY_WAVE_AMPLITUDE: 75,    // Larger number = more vertical movement
BUTTERFLY_WAVE_FREQUENCY: 8,     // Larger number = more zigzags
```

### Adjust Label Positions
```javascript
BUTTERFLY_LABEL_OFFSET_Y: 70,    // Move "Contact Us" label higher
SEED_LABEL_OFFSET_X: 50,         // Move seed labels further right
```

### Adjust Timing Delays
```javascript
SEED_AUTO_HIDE_DELAY: 5000,      // Seeds stay visible for 5 seconds instead of 3
GUST_COOLDOWN_MS: 500,           // Lily/daisy can retrigger faster
HOVER_DEBOUNCE_MS: 150,          // Increase if labels still flicker
```

## Component Positions

Component positions are defined in the `components` array in `loadSVGComponents()`:

```javascript
const components = [
  { name: 'lilly', svg: lillySvg, x: 98, y: 206, scale: 1.701 },
  { name: 'daisy', svg: daisySvg, x: 168, y: 305, scale: 1.25307 },
  { name: 'dandelion', svg: dandelionWithSeedsSvg, x: 142, y: 162, scale: 1.872585 },
  { name: 'butterflyClosed', svg: butterflyClosedSvg, x: 520, y: 425, scale: 1.2 },
  { name: 'brand', svg: textSvg, x: 100, y: 120, scale: 1.5 }
];
```

### Adjusting Component Positions
- `x`, `y`: Position in SVG coordinates
- `scale`: Size multiplier (1.0 = original size, 2.0 = double size)

## Navigation Routes

Routes are defined in the `seedPages` array in `createInteractiveOverlays()`:

```javascript
const seedPages = [
  { name: 'Events', route: '/events' },
  { name: 'Workshops', route: '/workshops' },
  { name: 'Displays', route: '/displays' },
  { name: 'Capabilities', route: '/capabilities' }
];
```

To change where seeds navigate to, simply update the `route` values.

## Tips

1. **Test incrementally**: Change one value at a time and test
2. **Keep backups**: The original file is saved as `app.js.backup`
3. **Browser cache**: Hard refresh (Cmd+Shift+R / Ctrl+Shift+R) to see changes
4. **Mobile testing**: Test on mobile devices as touch events may behave differently

## Troubleshooting

### Labels are flickering
- Increase `HOVER_DEBOUNCE_MS` to 150 or 200

### Animations feel sluggish
- Decrease duration values (BUTTERFLY_FLIGHT_DURATION, SEED_DRIFT_DURATION, GUST_DURATION)

### Butterfly moves too fast/slow
- Adjust `BUTTERFLY_FLIGHT_DURATION`
- Adjust `BUTTERFLY_WAVE_FREQUENCY` for more/fewer zigzags

### Seeds disappear too quickly
- Increase `SEED_AUTO_HIDE_DELAY` from 3000 to 5000 or more

### Dandelion triggers when hovering lily/daisy
- Increase `DANDELION_HIT_PADDING` (makes hit area smaller)
- Or decrease it (makes hit area larger)

