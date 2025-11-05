// Dashboard Data - The Payments Association Metrics 2025

const dashboardData = {
    // Industry Outlook
    outlook: {
        labels: ['Positive\nOutlook', 'Very Positive\nOutlook', 'Combined\nPositive/Neutral', 'Negative\nOutlook'],
        data: [55, 20, 75, 4],
        source: 'PAY360 2025 State of the Industry Survey'
    },

    // Budget Priorities
    budgetPriorities: {
        labels: [
            'Digitalisation &\nTechnology',
            'Partnerships &\nCollaborations',
            'Customer Experience\n& Acquisition',
            'AI/ML Investment\n(Financial Crime)'
        ],
        data: [45, 21, 11, 53],
        source: 'PAY360 2025 & Financial Crime 360'
    },

    // Budget Expectations
    budgetExpectations: {
        labels: ['Budget Increase\nExpected', 'Budget Decrease\nExpected'],
        data: [55, 9],
        source: 'PAY360 2025 State of the Industry Survey'
    },

    // AI Use Cases
    aiUseCases: {
        labels: [
            'Fraud Detection\n& Prevention',
            'Transaction Monitoring\n& Compliance',
            'Personalized\nCustomer Experiences',
            'Predictive Analytics\n(Customer Behavior)',
            'Dynamic Pricing\n& Offers',
            'Chatbot/Virtual\nAssistant'
        ],
        data: [85, 55, 54, 51, 45, 45],
        source: 'Senior Payment Professionals Survey'
    },

    // Industry Challenges (Time Series)
    challenges: {
        categories: [
            'Financial Crime\n& Cybersecurity',
            'Compliance',
            'Digital\nTransformation',
            'New Payment\nMethods'
        ],
        years: ['2023', '2024', '2025'],
        datasets: [
            {
                label: 'Financial Crime & Cybersecurity',
                data: [21, 28, 30],
                category: 0
            },
            {
                label: 'Compliance',
                data: [25, 18, 16],
                category: 1
            },
            {
                label: 'Digital Transformation',
                data: [14, 10, 13],
                category: 2
            },
            {
                label: 'New Payment Methods',
                data: [8, 9, 13],
                category: 3
            }
        ],
        source: 'PAY360 State of the Industry Survey'
    },

    // Workforce Skills Priorities
    workforceSkills: {
        labels: [
            'Technical\nExpertise',
            'Customer\nExperience',
            'Data\nAnalytics',
            'Cybersecurity',
            'Regulatory\nKnowledge'
        ],
        data: [25, 20, 19, 13, 13],
        source: 'PAY360 2025 State of the Industry Survey'
    },

    // Workforce Crisis Indicators
    workforceMetrics: {
        metrics: [
            {
                label: 'Global Cybersecurity Workforce Gap',
                value: 4763963,
                unit: 'People',
                year: 2024,
                source: 'ISC2'
            },
            {
                label: 'Cybersecurity Gap Increase',
                value: 19.1,
                unit: '% YoY',
                year: 2024,
                source: 'ISC2'
            },
            {
                label: 'Organizations with Staffing Shortage',
                value: 67,
                unit: '%',
                year: 2024,
                source: 'ISC2'
            },
            {
                label: 'UK Financial Services Job Applications Decline',
                value: 57,
                unit: '% YoY',
                year: 2025,
                source: 'TPA Payments Talent Report'
            },
            {
                label: 'UK Workers Requiring Upskilling',
                value: 160000,
                unit: 'Workers',
                year: 2025,
                source: 'TPA Payments Talent Report'
            },
            {
                label: 'UK Businesses Lacking Cybersecurity Skills',
                value: 637000,
                unit: 'Businesses',
                year: 2025,
                source: 'TPA Payments Talent Report'
            }
        ]
    },

    // Compliance Spending
    complianceCosts: {
        labels: [
            'Lower Bound\n(% non-interest)',
            'Upper Bound\n(% non-interest)',
            'Average\n(% revenue)',
            'Cross-Industry Avg\n(% revenue)',
            'High Outlier\n(% revenue)'
        ],
        data: [2.9, 8.7, 19, 25, 50],
        source: 'Federal Reserve, Model Office, Ascent RegTech, NorthRow'
    },

    // Global Payments Revenue
    globalRevenue: {
        years: [2014, 2019, 2020, 2021, 2022, 2023, 2024, 2030],
        data: [1.3, 1.8, 1.7, 1.9, 2.2, 2.4, 2.5, 3.0],
        projectedYear: 2024,
        source: 'McKinsey 2025 Global Payments Report',
        metrics: {
            cagr_2019_2024: '7%',
            projected_cagr_2024_2029: '4%',
            transaction_volume_2024: '3.6 Trillion Transactions',
            value_flows_2024: '$2 Quadrillion USD',
            roe_average_2024: '18.9%'
        }
    },

    // Large Financial Institution Metrics
    financialInstitutionMetrics: [
        {
            label: 'Large Banks Annual Compliance Cost',
            value: 200,
            unit: 'Million USD',
            year: 2025
        },
        {
            label: 'Financial Services Avg Compliance Cost',
            value: 30.9,
            unit: 'Million USD',
            year: 2025
        },
        {
            label: 'Financial Crime Compliance Cost (US & Canada)',
            value: 61,
            unit: 'Billion USD',
            year: 2024
        },
        {
            label: 'Financial Crime Compliance Cost Increase',
            value: 99,
            unit: '% of FIs',
            year: 2024
        },
        {
            label: 'Compliance IT Budget Allocation',
            value: 13.4,
            unit: '%',
            year: 2023
        },
        {
            label: 'Compliance IT Budget Allocation (2016 comparison)',
            value: 9.6,
            unit: '%',
            year: 2016
        }
    ],

    // AI Integration
    aiIntegration: {
        seniorProfessionalsView: 55,
        fraudDetectionAdoption: 90,
        source: 'Senior Professionals Survey & Feedzai AI Trends Report'
    },

    // ESG & Sustainability
    esg: {
        esgincreaseSince2023: {
            value: 75,
            unit: '% of Organizations',
            year: 2024,
            source: 'Berkeley Payment Solutions'
        },
        globalSustainableInvestment: {
            value: 30,
            unit: 'Trillion USD',
            year: 2021,
            source: 'Tranglo'
        },
        esgPaymentDeals: {
            value: 1.5,
            unit: 'Billion USD',
            year: 2021,
            source: 'Tranglo'
        }
    }
};

// Helper function to get chart colors
function getChartColors(count) {
    const colors = [
        '#01D6B0',  // Primary teal
        '#00B399',  // Darker teal
        '#008B7A',  // Even darker
        '#006B5F',  // Deep teal
        '#01F0C7',  // Light teal
        '#00B39F',  // Medium teal
        '#00A894',  // Another variant
        '#009A89'   // Another variant
    ];
    return colors.slice(0, count);
}

// Helper function to get neutral/contrast colors for specific charts
function getContrastColors(count) {
    const colors = [
        '#01D6B0',
        '#FF6B6B',
        '#4ECDC4',
        '#45B7D1',
        '#FFA07A',
        '#98D8C8'
    ];
    return colors.slice(0, count);
}
