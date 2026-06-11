import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def run_dashboard():
    print("=" * 60)
    print(" QUESTION 19: MINI DATA ANALYSIS DASHBOARD ")
    print("=" * 60)

    # 1. Create a rich synthetic dataset
    np.random.seed(42)
    n_records = 200
    
    study_hours = np.random.uniform(5, 35, n_records)
    attendance = np.clip(np.random.normal(85, 10, n_records), 50, 100)
    
    # GPA depends on study hours and attendance + some noise
    gpa = 1.5 + (study_hours * 0.05) + (attendance * 0.01) + np.random.normal(0, 0.2, n_records)
    gpa = np.clip(gpa, 0.0, 4.0)
    
    # Exam Score depends strongly on study hours + noise
    exam_score = 30 + (study_hours * 1.5) + (attendance * 0.2) + np.random.normal(0, 5, n_records)
    exam_score = np.clip(exam_score, 0, 100)
    
    df = pd.DataFrame({
        'Study_Hours': study_hours,
        'Attendance_Rate': attendance,
        'GPA': gpa,
        'Exam_Score': exam_score
    })
    
    print(f"Generated academic dataset with {n_records} student records and 4 features.")

    # 2. Calculate summary statistics
    summary_stats = df.describe().transpose()

    # 3. Calculate correlation matrix
    corr_matrix = df.corr()

    # 4. Generate combined visualization (2x2 grid)
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    
    # Top-Left: GPA Distribution Histogram
    sns.histplot(df['GPA'], bins=20, kde=True, ax=axes[0, 0], color='#4CAF50')
    axes[0, 0].set_title('Distribution of student GPAs', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('GPA (Out of 4.0)')
    axes[0, 0].set_ylabel('Student Count')
    
    # Top-Right: Study Hours vs Exam Score Scatter
    sns.scatterplot(data=df, x='Study_Hours', y='Exam_Score', ax=axes[0, 1], color='#E91E63', alpha=0.7)
    sns.regplot(data=df, x='Study_Hours', y='Exam_Score', scatter=False, ax=axes[0, 1], color='#2196F3')
    axes[0, 1].set_title('Study Hours vs Exam Score (with Trendline)', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Study Hours / Week')
    axes[0, 1].set_ylabel('Exam Score (%)')
    
    # Bottom-Left: Attendance vs GPA Scatter
    sns.scatterplot(data=df, x='Attendance_Rate', y='GPA', ax=axes[1, 0], color='#9C27B0', alpha=0.7)
    sns.regplot(data=df, x='Attendance_Rate', y='GPA', scatter=False, ax=axes[1, 0], color='#FF9800')
    axes[1, 0].set_title('Attendance Rate vs GPA (with Trendline)', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Attendance Rate (%)')
    axes[1, 0].set_ylabel('GPA')
    
    # Bottom-Right: Correlation Heatmap
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool)) # Half mask for clean look
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".3f", 
                linewidths=.5, ax=axes[1, 1], cbar_kws={"shrink": .8})
    axes[1, 1].set_title('Correlation Matrix Heatmap', fontsize=12, fontweight='bold')

    plt.suptitle("Student Academic Performance Dashboard Analysis", fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    
    # Convert plot to Base64 bytes to embed in HTML directly
    tmp_buffer = BytesIO()
    plt.savefig(tmp_buffer, format='png', dpi=150)
    tmp_buffer.seek(0)
    base64_image = base64.b64encode(tmp_buffer.read()).decode('utf-8')
    plt.close()

    # Save the plot physically too
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q19_dashboard_plots.png"))
    with open(plot_path, "wb") as f:
        f.write(base64.b64decode(base64_image))

    # 5. Generate beautiful HTML Dashboard File
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini Data Analysis Dashboard</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --border-color: rgba(255, 255, 255, 0.1);
            --text-color: #f1f5f9;
            --text-muted: #94a3b8;
            --primary: #3b82f6;
            --secondary: #10b981;
        }}
        body {{
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 30px;
        }}
        .container {{
            max-width: 1300px;
            margin: 0 auto;
        }}
        header {{
            margin-bottom: 30px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 15px;
        }}
        h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 700;
            background: linear-gradient(to right, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        p.subtitle {{
            color: var(--text-muted);
            margin: 5px 0 0 0;
            font-size: 14px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
        }}
        @media(min-width: 900px) {{
            .grid {{
                grid-template-columns: 1.2fr 2fr;
            }}
        }}
        .card {{
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }}
        .card h2 {{
            margin-top: 0;
            font-size: 18px;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 8px;
            margin-bottom: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}
        th, td {{
            padding: 10px 12px;
            text-align: left;
        }}
        th {{
            color: var(--text-muted);
            font-weight: 600;
            border-bottom: 1px solid var(--border-color);
        }}
        td {{
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }}
        tr:hover td {{
            background-color: rgba(255, 255, 255, 0.02);
        }}
        .metric-name {{
            font-weight: bold;
            color: var(--primary);
        }}
        .chart-img {{
            width: 100%;
            height: auto;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Student Performance Analysis Dashboard</h1>
            <p class="subtitle">Exploratory Data Insights on study hours, attendance, GPA, and exam scores (Dataset size: {n_records} profiles)</p>
        </header>
        
        <div class="grid">
            <!-- Left Side: Summary Statistics & Correlation Values -->
            <div style="display: flex; flex-direction: column; gap: 30px;">
                <div class="card">
                    <h2>Summary Statistics</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Metric</th>
                                <th>Mean</th>
                                <th>Std Dev</th>
                                <th>Min</th>
                                <th>Max</th>
                            </tr>
                        </thead>
                        <tbody>
                            {"".join(f"<tr><td class='metric-name'>{row}</td><td>{summary_stats.loc[row, 'mean']:.3f}</td><td>{summary_stats.loc[row, 'std']:.3f}</td><td>{summary_stats.loc[row, 'min']:.3f}</td><td>{summary_stats.loc[row, 'max']:.3f}</td></tr>" for row in summary_stats.index)}
                        </tbody>
                    </table>
                </div>

                <div class="card">
                    <h2>Correlation Matrix</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Feature</th>
                                <th>Study Hours</th>
                                <th>Attendance</th>
                                <th>GPA</th>
                                <th>Exam Score</th>
                            </tr>
                        </thead>
                        <tbody>
                            {"".join(f"<tr><td class='metric-name'>{row}</td><td>{corr_matrix.loc[row, 'Study_Hours']:.3f}</td><td>{corr_matrix.loc[row, 'Attendance_Rate']:.3f}</td><td>{corr_matrix.loc[row, 'GPA']:.3f}</td><td>{corr_matrix.loc[row, 'Exam_Score']:.3f}</td></tr>" for row in corr_matrix.index)}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Right Side: Charts -->
            <div class="card">
                <h2>Visual Analysis Panels</h2>
                <img class="chart-img" src="data:image/png;base64,{base64_image}" alt="Dashboard Analysis Charts">
            </div>
        </div>
    </div>
</body>
</html>
"""
    dashboard_path = os.path.abspath("dashboard.html")
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Console output summary
    print("\nSUMMARY STATISTICS (CONSOLE):")
    print("-" * 60)
    print(df.describe().round(4))
    print("\nCORRELATION MATRIX (CONSOLE):")
    print("-" * 60)
    print(corr_matrix.round(4))
    print("-" * 60)
    print(f"\nDashboard HTML file successfully generated:")
    print(f"-> [dashboard.html](file:///{dashboard_path.replace(os.sep, '/')})")
    print(f"-> Combined chart saved to [q19_dashboard_plots.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_dashboard()
