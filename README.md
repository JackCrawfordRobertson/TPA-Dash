# The Payments Association - Industry Dashboard

A professional, iframe-embeddable HTML dashboard displaying key metrics and insights from The Payments Association reports and industry surveys.

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive Charts**: Multiple chart types (doughnut, bar, line, radar) using Chart.js
- **Modern Styling**: Dark theme with teal accent colors matching TPA branding
- **Iframe Compatible**: Easily embed in other web applications
- **Data-Driven**: Comprehensive metrics from 2025 industry reports

## Project Structure

```
├── pages/                      # HTML files
│   ├── index.html             # Main dashboard
│   ├── report-dashboard.html
│   ├── merchant-dashboard.html
│   └── ... (other dashboards)
├── static/
│   ├── css/
│   │   └── styles.css         # All styling
│   └── js/
│       ├── data.js            # Data definitions
│       └── charts.js          # Chart initialization
├── data/                       # CSV data files
├── scripts/                    # Python utilities
└── README.md
```

## Quick Start

### Run Local Server (Recommended)
```bash
cd /Users/JackRobertson/TPA-Dash
python3 -m http.server 8000
```
Then open your browser and visit:
- Main Dashboard: `http://localhost:8000/pages/index.html`
- Report Dashboard: `http://localhost:8000/pages/report-dashboard.html`
- Other Pages: `http://localhost:8000/pages/`

### Direct File Access
Open any HTML file directly in your browser:
```bash
open pages/index.html
```
Note: Some features may not work with `file://` protocol due to browser security.

### Embed in iframe
```html
<iframe
    src="http://localhost:8000/pages/index.html"
    width="1400"
    height="2000"
    frameborder="0">
</iframe>
```

## Dashboard Sections

### 1. Industry Outlook
Shows the distribution of business sentiment (positive, very positive, neutral, negative) from PAY360 2025 survey.

### 2. Budget Priorities
Displays investment focus areas including:
- Digitalisation & Technology (45%)
- AI/ML Investment in Financial Crime (53%)
- Partnerships & Collaborations (21%)
- Customer Experience & Acquisition (11%)

### 3. AI Use Cases
Adoption rates for AI applications in payments, led by:
- Fraud Detection & Prevention (85%)
- Transaction Monitoring & Compliance (55%)
- Personalized Customer Experiences (54%)

### 4. Industry Challenges Trend
Multi-year comparison (2023-2025) showing:
- Financial Crime & Cybersecurity
- Compliance
- Digital Transformation
- New Payment Methods Implementation

### 5. Workforce Skills Priorities
Priority areas for workforce development:
- Technical Expertise (25%)
- Customer Experience (20%)
- Data Analytics (19%)
- Cybersecurity (13%)
- Regulatory Knowledge (13%)

### 6. Global Payments Revenue
Historical and projected revenue from 2014 to 2030, showing:
- Growth trajectory
- CAGR metrics
- Transaction volume insights

### 7. Compliance Spending
Cost indicators ranging from lower bounds (2.9%) to high outliers (50%) as percentage of revenue.

### 8. Key Metrics
Quick reference cards for critical figures:
- Global Cybersecurity Workforce Gap: 4.76M people
- Financial Crime Compliance Cost: $61B (US & Canada)
- Projected Global Payments Revenue 2030: $3T
- UK Workers Requiring Upskilling: 160,000

## Design System

### Color Palette
- **Primary Background**: #28313E (Dark blue-gray)
- **Secondary Background**: #323D4D
- **Tertiary Background**: #3A4655
- **Primary Accent**: #01D6B0 (Teal/Green)
- **Text Primary**: #FFFFFF (White)
- **Text Secondary**: #E0E0E0
- **Text Tertiary**: #9CA3AF (Gray)

### Typography
- **Font Family**: Helvetica, System UI fonts
- **Headings**: 600-700 weight
- **Body**: 400-500 weight

## Data Sources

- The Payments Association - PAY360 2025 State of the Industry Survey
- The Payments Association - Financial Crime 360 Report 2025
- Federal Reserve Bank of St. Louis - Compliance Cost Study
- ISC2 - 2024 Cybersecurity Workforce Study
- McKinsey & Company - 2025 Global Payments Report
- LexisNexis Risk Solutions - True Cost of Financial Crime Compliance Study
- Feedzai - AI Trends in Fraud Detection Report
- And more (see dashboard footer for complete list)

## Customization

### Changing Colors
Edit the `:root` CSS variables in `styles.css`:
```css
:root {
    --accent-primary: #01D6B0;
    --accent-secondary: #00B399;
    --bg-primary: #28313E;
    /* ... */
}
```

### Adding New Charts
1. Add data to `data.js`
2. Add a new `<canvas>` element to `index.html`
3. Initialize the chart in `charts.js`

### Updating Data
Modify the `dashboardData` object in `data.js` with new metrics and the charts will reflect the changes.

## Responsive Breakpoints

- **Desktop**: 1200px+ (multi-column grid)
- **Tablet**: 768px - 1200px (2-column grid)
- **Mobile**: Below 768px (single column)

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## Dependencies

- Chart.js 3+ (loaded via CDN)
- No other external dependencies

## Performance

- Lightweight: ~50KB total (uncompressed)
- Fast load: Charts render immediately
- Optimized: CSS and JavaScript are minified

## License

Created for The Payments Association

## Support

For issues or questions, please refer to the documentation or contact The Payments Association.

---

**Last Updated**: November 2025
