// Chart Configuration and Initialization

// Default Chart.js options
Chart.defaults.font.family = "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif";
Chart.defaults.color = '#E0E0E0';
Chart.defaults.borderColor = '#4A5668';

// Custom color scheme
const chartColors = {
    primary: '#01D6B0',
    secondary: '#00B399',
    tertiary: '#008B7A',
    quaternary: '#006B5F',
    light: '#01F0C7',
    variants: ['#01D6B0', '#00wB399', '#008B7A', '#006B5F', '#01F0C7', '#00B39F', '#00A894', '#009A89'],
    accent: '#00B399',
    text: '#FFFFFF',
    textSecondary: '#E0E0E0',
    border: '#4A5668'
};

// Utility function for gradient backgrounds
function createGradient(ctx, color) {
    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, color + '40');
    gradient.addColorStop(1, color + '05');
    return gradient;
}

// 1. Industry Outlook Chart (Pie)
const outlookCtx = document.getElementById('outlookChart');
if (outlookCtx) {
    new Chart(outlookCtx, {
        type: 'doughnut',
        data: {
            labels: dashboardData.outlook.labels,
            datasets: [{
                data: dashboardData.outlook.data,
                backgroundColor: [
                    chartColors.primary,
                    chartColors.secondary,
                    chartColors.light,
                    '#4A5668'
                ],
                borderColor: '#28313E',
                borderWidth: 2,
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: { size: 12, weight: '500' },
                        color: chartColors.textSecondary
                    }
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.parsed + '%';
                        }
                    }
                }
            }
        }
    });
}

// 2. Budget Priorities Chart (Horizontal Bar)
const budgetCtx = document.getElementById('budgetChart');
if (budgetCtx) {
    new Chart(budgetCtx, {
        type: 'bar',
        data: {
            labels: dashboardData.budgetPriorities.labels,
            datasets: [{
                label: 'Priority Level (%)',
                data: dashboardData.budgetPriorities.data,
                backgroundColor: [
                    chartColors.primary,
                    chartColors.secondary,
                    chartColors.tertiary,
                    chartColors.light
                ],
                borderRadius: 6,
                borderSkipped: false,
                borderWidth: 0
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return context.parsed.x + '%';
                        }
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    max: 60,
                    grid: {
                        color: '#3A4655',
                        drawBorder: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11 },
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11, weight: '500' }
                    }
                }
            }
        }
    });
}

// 3. AI Use Cases Chart (Horizontal Bar)
const aiCtx = document.getElementById('aiChart');
if (aiCtx) {
    new Chart(aiCtx, {
        type: 'bar',
        data: {
            labels: dashboardData.aiUseCases.labels,
            datasets: [{
                label: 'Adoption Rate (%)',
                data: dashboardData.aiUseCases.data,
                backgroundColor: chartColors.variants.slice(0, 6),
                borderRadius: 6,
                borderSkipped: false,
                borderWidth: 0
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return context.parsed.x + '%';
                        }
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    max: 100,
                    grid: {
                        color: '#3A4655',
                        drawBorder: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11 },
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 10, weight: '500' }
                    }
                }
            }
        }
    });
}

// 4. Industry Challenges Trend Chart (Line)
const challengesCtx = document.getElementById('challengesChart');
if (challengesCtx) {
    const challengesDatasets = dashboardData.challenges.datasets.map((dataset, index) => ({
        label: dataset.label,
        data: dataset.data,
        borderColor: chartColors.variants[index],
        backgroundColor: chartColors.variants[index] + '10',
        borderWidth: 3,
        pointBackgroundColor: chartColors.variants[index],
        pointBorderColor: '#28313E',
        pointBorderWidth: 2,
        pointRadius: 5,
        pointHoverRadius: 7,
        fill: false,
        tension: 0.4
    }));

    new Chart(challengesCtx, {
        type: 'line',
        data: {
            labels: dashboardData.challenges.years,
            datasets: challengesDatasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: { size: 11, weight: '500' },
                        color: chartColors.textSecondary
                    }
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y + '%';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 35,
                    grid: {
                        color: '#3A4655',
                        drawBorder: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11 },
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11, weight: '500' }
                    }
                }
            }
        }
    });
}

// 5. Workforce Skills Chart (Polar)
const workforceCtx = document.getElementById('workforceChart');
if (workforceCtx) {
    new Chart(workforceCtx, {
        type: 'radar',
        data: {
            labels: dashboardData.workforceSkills.labels,
            datasets: [{
                label: 'Priority (%)',
                data: dashboardData.workforceSkills.data,
                borderColor: chartColors.primary,
                backgroundColor: chartColors.primary + '20',
                pointBackgroundColor: chartColors.primary,
                pointBorderColor: '#28313E',
                pointBorderWidth: 2,
                pointRadius: 5,
                pointHoverRadius: 7,
                borderWidth: 3,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return context.parsed.r + '%';
                        }
                    }
                }
            },
            scales: {
                r: {
                    beginAtZero: true,
                    max: 30,
                    grid: {
                        color: '#3A4655'
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 10 },
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    pointLabels: {
                        color: chartColors.textSecondary,
                        font: { size: 11, weight: '500' }
                    }
                }
            }
        }
    });
}

// 6. Global Payments Revenue Chart (Line)
const revenueCtx = document.getElementById('revenueChart');
if (revenueCtx) {
    new Chart(revenueCtx, {
        type: 'line',
        data: {
            labels: dashboardData.globalRevenue.years,
            datasets: [{
                label: 'Revenue (Trillion USD)',
                data: dashboardData.globalRevenue.data,
                borderColor: chartColors.primary,
                backgroundColor: chartColors.primary + '15',
                pointBackgroundColor: chartColors.primary,
                pointBorderColor: '#28313E',
                pointBorderWidth: 2,
                pointRadius: 6,
                pointHoverRadius: 8,
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                segment: {
                    borderDash: (ctx) => {
                        // Make 2030 projection dashed
                        if (ctx.p0DataIndex === dashboardData.globalRevenue.years.length - 2) {
                            return [5, 5];
                        }
                        return [];
                    }
                }
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return '$' + context.parsed.y + 'T';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 3.2,
                    grid: {
                        color: '#3A4655',
                        drawBorder: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11 },
                        callback: function(value) {
                            return '$' + value + 'T';
                        }
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11, weight: '500' }
                    }
                }
            }
        }
    });
}

// 7. Compliance Spending Chart (Bar)
const complianceCtx = document.getElementById('complianceChart');
if (complianceCtx) {
    new Chart(complianceCtx, {
        type: 'bar',
        data: {
            labels: dashboardData.complianceCosts.labels,
            datasets: [{
                label: 'Spending Rate (%)',
                data: dashboardData.complianceCosts.data,
                backgroundColor: [
                    chartColors.primary,
                    chartColors.secondary,
                    chartColors.tertiary,
                    chartColors.light,
                    '#00B399'
                ],
                borderRadius: 6,
                borderSkipped: false,
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: '#323D4D',
                    padding: 12,
                    titleColor: chartColors.text,
                    bodyColor: chartColors.textSecondary,
                    borderColor: chartColors.primary,
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return context.parsed.y + '%';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 55,
                    grid: {
                        color: '#3A4655',
                        drawBorder: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 11 },
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: chartColors.textSecondary,
                        font: { size: 10, weight: '500' }
                    }
                }
            }
        }
    });
}

console.log('Charts initialized successfully');
