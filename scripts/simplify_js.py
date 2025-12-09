#!/usr/bin/env python3
"""
Simplify the JavaScript in global-reach-growth.html
Remove all view-switching code and update references
"""

import re

html_file = '/Users/JackRobertson/TPA-Dash/pages/global-reach-growth.html'

# Read the file
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences
content = content.replace('paymentDataAbsolute', 'paymentData')
content = content.replace('getPaymentData()', 'paymentData')
content = content.replace("currentView === 'absolute'", 'true')
content = content.replace("currentView === 'percapita'", 'false')
content = content.replace('Transaction Value (2025)', 'Digital Payment Value (2025)')
content = content.replace('Transaction Intensity (2025)', 'Digital Payment Value (2025)')
content = content.replace('Payment Value', 'Digital Payment Value')
content = content.replace('sidebar-absolute', 'sidebar')
content = content.replace('sidebar-percapita', 'sidebar-hidden')

# Remove the updateHeaderDescription function (it's not needed anymore)
content = re.sub(r'    // Update header description based on view\s+function updateHeaderDescription\(\) \{[^}]+\}\s+', '', content, flags=re.DOTALL)

# Remove the switchView function
content = re.sub(r'    // Toggle view and refresh map\s+function switchView\([^)]+\) \{[^}]+\}\s+', '', content, flags=re.DOTALL)

# Remove the view toggle event listener
content = re.sub(r"    // Handle view toggle dropdown\s+document\.getElementById\('view-toggle'\)\.addEventListener\([^;]+\);\s+", '', content)

# Remove sidebar-percapita display toggle code
content = re.sub(r"        document\.getElementById\('sidebar-percapita'\)\.style\.display[^;]+;\s+", '', content)

# Write back
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Simplified JavaScript successfully!")
