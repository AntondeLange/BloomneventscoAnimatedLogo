# Deployment Checklist

## Pre-Deployment

### 1. File Preparation
- [ ] Use `app_cleaned.js` (not `app.js` with debug logs)
- [ ] Verify all SVG assets are in `assets/` folder
- [ ] Check `index.html` references correct script file
- [ ] Ensure GSAP CDN link is present and working

### 2. Configuration Review
- [ ] Navigation routes in `seedPages` array point to correct URLs
- [ ] Animation timings are appropriate for your use case
- [ ] Component positions look good on target screen sizes
- [ ] Label offsets are correct

### 3. Testing
- [ ] Test on desktop Chrome
- [ ] Test on desktop Firefox
- [ ] Test on desktop Safari
- [ ] Test on mobile iOS Safari
- [ ] Test on mobile Chrome
- [ ] Test all interactive elements:
  - [ ] Lily hover and sway
  - [ ] Daisy hover and sway
  - [ ] Dandelion seed spread
  - [ ] All 4 seed labels appear
  - [ ] Seed click animation
  - [ ] Butterfly hover lift
  - [ ] Butterfly click fly-away
  - [ ] Label management (no overlaps)
- [ ] Verify navigation works for all routes
- [ ] Check browser console for errors

### 4. Performance Check
- [ ] Page loads in < 2 seconds
- [ ] Animations are smooth (60fps)
- [ ] No memory leaks (check DevTools)
- [ ] Assets load efficiently

## Deployment Options

### Option A: Replace Existing File
```bash
# Backup current production file
cp app.js app.js.old

# Deploy cleaned version
cp app_cleaned.js app.js
```

### Option B: New Filename
```html
<!-- Update HTML to reference new file -->
<script src="app_cleaned.js"></script>
```

### Option C: Minified Version
```bash
# Install terser if needed
npm install -g terser

# Minify for production
terser app_cleaned.js -o app.min.js --compress --mangle

# Update HTML
<script src="app.min.js"></script>
```

## Post-Deployment

### 1. Immediate Checks (within 5 minutes)
- [ ] Page loads without errors
- [ ] All SVG elements visible
- [ ] Hover interactions work
- [ ] Click interactions work
- [ ] Navigation routes work
- [ ] No console errors

### 2. Cross-Browser Testing (within 1 hour)
- [ ] Test on Chrome
- [ ] Test on Firefox
- [ ] Test on Safari
- [ ] Test on Edge
- [ ] Test on mobile devices

### 3. User Testing (within 24 hours)
- [ ] Get feedback from 3-5 users
- [ ] Check analytics for errors
- [ ] Monitor performance metrics
- [ ] Verify navigation tracking

### 4. Performance Monitoring
- [ ] Check page load times
- [ ] Monitor error rates
- [ ] Track user interactions
- [ ] Verify conversion rates

## Rollback Plan

If issues arise:

### Quick Rollback
```bash
# Restore previous version
cp app.js.old app.js
```

### Identify Issue
1. Check browser console for errors
2. Review recent changes in `CLEANUP_SUMMARY.md`
3. Compare with `app.js.backup` if needed
4. Test specific failing component

### Fix and Redeploy
1. Fix issue in `app_cleaned.js`
2. Test locally
3. Run through checklist again
4. Redeploy

## Integration with Main Website

### If Embedding in Existing Site

#### Before Integration
- [ ] Test in isolation first
- [ ] Check for CSS conflicts
- [ ] Verify no JavaScript conflicts
- [ ] Test z-index layering
- [ ] Ensure navigation doesn't conflict with site router

#### During Integration
- [ ] Add to staging environment first
- [ ] Test all site navigation
- [ ] Verify logo doesn't break responsive design
- [ ] Check mobile menu interactions
- [ ] Test keyboard navigation
- [ ] Verify accessibility (screen readers)

#### After Integration
- [ ] Full site regression testing
- [ ] Check all pages load correctly
- [ ] Verify SEO isn't impacted
- [ ] Monitor site performance
- [ ] Check analytics integration

## Optimization Checklist (Optional)

### For High-Traffic Sites
- [ ] Enable gzip compression
- [ ] Use CDN for assets
- [ ] Implement lazy loading
- [ ] Add service worker for caching
- [ ] Optimize SVG files further
- [ ] Consider WebP for raster images
- [ ] Implement resource hints (preload, prefetch)

### For Best Performance
- [ ] Minify JavaScript
- [ ] Minify CSS
- [ ] Optimize SVG viewBox sizes
- [ ] Remove unused CSS
- [ ] Defer non-critical JavaScript
- [ ] Use font-display: swap for custom fonts

## Maintenance Schedule

### Weekly
- [ ] Check error logs
- [ ] Monitor performance metrics
- [ ] Review user feedback

### Monthly
- [ ] Update GSAP if new version available
- [ ] Review and optimize based on usage data
- [ ] Check for browser compatibility issues

### Quarterly
- [ ] Full code review
- [ ] Performance audit
- [ ] Accessibility audit
- [ ] Update documentation

## Emergency Contacts

**Developer**: [Your Name/Team]  
**Backup**: [Backup Contact]  
**Hosting**: [Hosting Provider Support]

## Documentation Links

- [CLEANUP_SUMMARY.md](./CLEANUP_SUMMARY.md) - What was changed
- [CONFIGURATION_GUIDE.md](./CONFIGURATION_GUIDE.md) - How to adjust settings
- [README_PRODUCTION.md](./README_PRODUCTION.md) - Full documentation

## Sign-Off

- [ ] Developer tested and approved
- [ ] QA tested and approved
- [ ] Stakeholder reviewed and approved
- [ ] Backup plan in place
- [ ] Monitoring configured
- [ ] Documentation updated

**Deployed By**: ________________  
**Date**: ________________  
**Version**: 1.0  
**Status**: ✅ Ready for Production

