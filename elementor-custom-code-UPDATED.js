window.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'dashboard-height') {
    const height = event.data.height;
    const dashboard = event.data.dashboard;

    console.log('Received height from dashboard:', dashboard, height + 'px');

    if (dashboard === 'industry-outlook' || dashboard === 'merchant-dashboard') {
      const iframes = document.querySelectorAll('iframe');
      iframes.forEach(function(iframe) {
        const src = iframe.src.toLowerCase();

        if (src.includes('industry_outlook_key_challenge') ||
            src.includes('merchant-dashboard')) {
          iframe.style.height = (height + 20) + 'px';
          console.log('Updated iframe height to:', (height + 20) + 'px');
        }
      });
    }
  }
});