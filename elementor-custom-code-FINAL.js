// Universal iframe height adjuster for TPA dashboards
// Final version - no padding to prevent loops
window.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'dashboard-height') {
    const height = event.data.height;
    const dashboard = event.data.dashboard;

    console.log('Received height from dashboard:', dashboard, height + 'px');

    // Only process Industry Outlook and Merchant Dashboard
    // Map dashboard uses fixed height
    if (dashboard === 'industry-outlook' || dashboard === 'merchant-dashboard') {
      const iframes = document.querySelectorAll('iframe');
      iframes.forEach(function(iframe) {
        const src = iframe.src.toLowerCase();

        if (src.includes('industry_outlook_key_challenge') ||
            src.includes('merchant-dashboard')) {
          // Use exact height (no +20px padding to prevent mini-loops)
          iframe.style.height = height + 'px';
          console.log('Updated iframe height to:', height + 'px');
        }
      });
    }
  }
});
