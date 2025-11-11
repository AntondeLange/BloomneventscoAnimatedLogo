# Bloom'n Events Co. - Interactive Logo Animation

![License](https://img.shields.io/badge/license-Proprietary-red)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)

An interactive, animated SVG logo for Bloom'n Events Co. featuring smooth GSAP animations, hover interactions, and intelligent label management.

## 🎨 Features

### Interactive Elements
- **Lily** - Continuous swaying animation on hover with "Our team" label
- **Daisy** - Continuous swaying animation on hover with "Our team" label
- **Dandelion** - Seeds spread out on hover with clickable navigation labels
- **Butterfly** - Lifts on hover, flies away with zigzag pattern on click

### Smart Interactions
- ✨ Only one label visible at a time (no overlaps)
- 🎯 Labels follow elements during animations
- 🌊 Smooth fade in/out transitions
- 📱 Touch-friendly for mobile devices
- ⚡ Optimized performance (60fps animations)

### Navigation
Dandelion seeds link to:
- **Events** → `/events`
- **Workshops** → `/workshops`
- **Displays** → `/displays`
- **Capabilities** → `/capabilities`

## 🚀 Quick Start

### View Demo
Open `index.html` in a modern web browser.

### For Production
Use `app_cleaned.js` - the optimized, production-ready version:
```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="app_cleaned.js"></script>
```

### For Development
Use `app.js` if you need debug logging.

## 📁 Project Structure

```
BloomnLogoAnimation/
├── index.html                    # Main HTML file
├── styles.css                    # Styles and animations
├── app_cleaned.js               # Production-ready (76KB)
├── app.js                       # Development version with logging (83KB)
├── app.js.backup               # Original backup
├── assets/                      # SVG components
│   ├── lilly.svg
│   ├── daisey.svg
│   ├── dandilionwseeds.svg
│   ├── dandilionwoseeds.svg
│   ├── dandilionseeds1-4.svg
│   ├── butterflywingsclosed.svg
│   └── logotext.svg
└── docs/                        # Documentation
    ├── CLEANUP_SUMMARY.md
    ├── CONFIGURATION_GUIDE.md
    ├── DEPLOYMENT_CHECKLIST.md
    └── README_PRODUCTION.md
```

## 📖 Documentation

- **[CLEANUP_SUMMARY.md](./CLEANUP_SUMMARY.md)** - Detailed list of code improvements
- **[CONFIGURATION_GUIDE.md](./CONFIGURATION_GUIDE.md)** - How to adjust animations and settings
- **[DEPLOYMENT_CHECKLIST.md](./DEPLOYMENT_CHECKLIST.md)** - Step-by-step deployment guide
- **[README_PRODUCTION.md](./README_PRODUCTION.md)** - Complete production documentation

## ⚙️ Configuration

All animation parameters are centralized in the `CONFIG` object:

```javascript
const CONFIG = {
  ANIMATION: {
    GUST_DURATION: 1.6,              // Lily/daisy sway duration
    BUTTERFLY_FLIGHT_DURATION: 12.0, // Butterfly flight time
    SEED_DRIFT_DURATION: 3.0,        // Seed float-away time
    SEED_AUTO_HIDE_DELAY: 3000,      // Seeds auto-hide delay
    // ... more settings
  },
  POSITIONS: {
    BUTTERFLY_LABEL_OFFSET_Y: 50,    // Label positioning
    SEED_LABEL_OFFSET_X: 40,         // Seed label spacing
    // ... more settings
  }
};
```

See [CONFIGURATION_GUIDE.md](./CONFIGURATION_GUIDE.md) for detailed adjustment instructions.

## 🎯 Code Quality

### Production Standards
- ✅ No console.log statements
- ✅ No unused functions
- ✅ DRY principles applied
- ✅ Centralized configuration
- ✅ Helper functions for common operations
- ✅ No linter errors

### Performance
- **File Size**: 76KB (8.4% smaller than original)
- **Lines Removed**: 124 lines of debug/unused code
- **Optimizations**: Eliminated code duplication, centralized config

### Maintainability
- All animation parameters in one `CONFIG` object
- Clear, descriptive function names
- Consistent code patterns
- Comprehensive documentation

## 🌐 Browser Compatibility

Tested and working on:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ iOS Safari
- ✅ Chrome Mobile

### Requirements
- Modern browser with ES6 support
- GSAP library (included via CDN)
- SVG support

## 🔧 Installation

### Clone Repository
```bash
git clone https://github.com/AntondeLange/BloomneventscoAnimatedLogo.git
cd BloomneventscoAnimatedLogo
```

### Open in Browser
```bash
open index.html
# or
python3 -m http.server 8000
# then visit http://localhost:8000
```

### Deploy to Production
```bash
# Use the cleaned version
cp app_cleaned.js app.js

# Or minify for even better performance
npm install -g terser
terser app_cleaned.js -o app.min.js --compress --mangle
```

## 🎨 Customization

### Change Navigation Routes
Edit the `seedPages` array in `createInteractiveOverlays()`:
```javascript
const seedPages = [
  { name: 'Events', route: '/your-events-page' },
  { name: 'Workshops', route: '/your-workshops-page' },
  // ... update as needed
];
```

### Adjust Animation Speed
Edit values in the `CONFIG` object:
```javascript
BUTTERFLY_FLIGHT_DURATION: 8.0,  // Faster (was 12.0)
SEED_DRIFT_DURATION: 2.0,        // Faster (was 3.0)
```

### Change Component Positions
Edit the `components` array in `loadSVGComponents()`:
```javascript
{ name: 'butterfly', x: 520, y: 425, scale: 1.2 }
```

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| File Size (Production) | 76 KB |
| Load Time | < 1 second |
| Animation FPS | 60 fps |
| Console Errors | 0 |
| Code Duplication | Minimal |

## 🤝 Contributing

This is a proprietary project for Bloom'n Events Co. For questions or issues, please contact the development team.

## 📝 License

© 2025 Bloom'n Events Co. All rights reserved.

## 👥 Credits

**Developer**: Anton de Lange  
**Company**: Bloom'n Events Co. Pty Ltd  
**Animation Library**: [GSAP](https://greensock.com/gsap/)

## 📞 Support

For technical support or questions:
- Review the [Configuration Guide](./CONFIGURATION_GUIDE.md)
- Check the [Deployment Checklist](./DEPLOYMENT_CHECKLIST.md)
- Refer to inline code comments

## 🎉 Version History

### v1.0 (November 11, 2025)
- ✅ Initial production release
- ✅ All interactive elements working
- ✅ Code cleaned and optimized
- ✅ Comprehensive documentation
- ✅ Ready for deployment

---

**Status**: ✅ Production Ready  
**Last Updated**: November 11, 2025  
**Repository**: [github.com/AntondeLange/BloomneventscoAnimatedLogo](https://github.com/AntondeLange/BloomneventscoAnimatedLogo)

