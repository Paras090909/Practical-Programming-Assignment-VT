import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Adjust path to find stats_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part_a")))
import stats_utils

def generate_student_dataset():
    """Generate a synthetic student performance dataset."""
    np.random.seed(101)
    n_students = 150
    
    first_names = ["John", "Mary", "David", "Emma", "James", "Olivia", "Daniel", "Sophia", "Robert", "Isabella", 
                   "Michael", "Charlotte", "William", "Amelia", "Richard", "Mia", "Joseph", "Harper", "Thomas", "Evelyn"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
                  "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White"]
                  
    names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(n_students)]
    
    # Study habits
    study_hours = np.random.uniform(4, 30, n_students)
    attendance = np.clip(np.random.normal(87, 8, n_students), 60, 100)
    
    # Subject Scores out of 100
    math_scores = np.clip(35 + (study_hours * 1.8) + (attendance * 0.25) + np.random.normal(0, 4, n_students), 0, 100)
    science_scores = np.clip(40 + (study_hours * 1.5) + (attendance * 0.3) + np.random.normal(0, 5, n_students), 0, 100)
    english_scores = np.clip(50 + (study_hours * 0.8) + (attendance * 0.35) + np.random.normal(0, 4, n_students), 0, 100)
    history_scores = np.clip(45 + (study_hours * 0.9) + (attendance * 0.4) + np.random.normal(0, 5, n_students), 0, 100)
    
    df = pd.DataFrame({
        'StudentID': [f"STU{1000+i}" for i in range(n_students)],
        'Name': names,
        'Study_Hours': np.round(study_hours, 1),
        'Attendance': np.round(attendance, 1),
        'Math': np.round(math_scores, 1),
        'Science': np.round(science_scores, 1),
        'English': np.round(english_scores, 1),
        'History': np.round(history_scores, 1)
    })
    
    df.to_csv("student_performance.csv", index=False)
    return df

def run_student_eda():
    print("=" * 60)
    print(" QUESTION 20: STUDENT PERFORMANCE EDA ")
    print("=" * 60)

    # 1. Load / Generate Dataset
    csv_file = "student_performance.csv"
    if not os.path.exists(csv_file):
        print("Dataset file student_performance.csv not found. Generating a new synthetic dataset...")
        df = generate_student_dataset()
    else:
        print("Loading existing student_performance.csv dataset...")
        df = pd.read_csv(csv_file)
        
    print(f"Dataset loaded. Number of Student Records: {len(df)}")
    
    # 2. Perform calculations
    subjects = ['Math', 'Science', 'English', 'History']
    
    # Calculate overall average for each student
    df['Overall_Average'] = df[subjects].mean(axis=1)

    # Subject-wise statistics
    subj_means = df[subjects].mean()
    subj_max = df[subjects].max()
    subj_min = df[subjects].min()

    # Identify top performers and struggling students
    top_student = df.loc[df['Overall_Average'].idxmax()]
    struggling_student = df.loc[df['Overall_Average'].idxmin()]

    # Print Summary statistics
    headers = ["Subject", "Average Score", "Highest Score", "Lowest Score"]
    rows = []
    for s in subjects:
        rows.append([s, f"{subj_means[s]:.2f}", f"{subj_max[s]:.1f}", f"{subj_min[s]:.1f}"])
    stats_utils.print_table(headers, rows, title="Subject-wise Score Summary")

    print("\nOVERALL TRENDS & INSIGHTS:")
    print("-" * 60)
    print(f"- Overall Class Average Marks: {df['Overall_Average'].mean():.2f}%")
    print(f"- Top Student: {top_student['Name']} ({top_student['StudentID']}) with {top_student['Overall_Average']:.2f}% avg")
    print(f"- Lowest Scoring Student: {struggling_student['Name']} ({struggling_student['StudentID']}) with {struggling_student['Overall_Average']:.2f}% avg")
    
    # Calculate Correlation between study hours, attendance and overall score
    study_corr = df['Study_Hours'].corr(df['Overall_Average'])
    attend_corr = df['Attendance'].corr(df['Overall_Average'])
    print(f"- Study Hours correlation with Overall Average: {study_corr:.4f} (Strong positive relationship)")
    print(f"- Attendance correlation with Overall Average: {attend_corr:.4f} (Moderate positive relationship)")
    print("-" * 60)

    # 3. Create visual charts
    os.makedirs("output_plots", exist_ok=True)
    plot_path = os.path.abspath(os.path.join("output_plots", "q20_student_eda_insights.png"))

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Plot 1: Subject-wise Performance comparison (Mean, Max, Min)
    x = np.arange(len(subjects))
    width = 0.25
    axes[0, 0].bar(x - width, subj_min, width, label='Minimum Score', color='#E57373')
    axes[0, 0].bar(x, subj_means, width, label='Average Score', color='#64B5F6')
    axes[0, 0].bar(x + width, subj_max, width, label='Maximum Score', color='#81C784')
    axes[0, 0].set_title('Subject Score Comparison (Mean vs. Min vs. Max)', fontsize=12, fontweight='bold')
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(subjects)
    axes[0, 0].set_ylabel('Score (%)')
    axes[0, 0].set_ylim(0, 110)
    axes[0, 0].legend()

    # Plot 2: Distribution of student averages
    sns.histplot(df['Overall_Average'], kde=True, color='#9C27B0', ax=axes[0, 1], bins=15)
    axes[0, 1].set_title('Distribution of Student Overall Averages', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Overall Average Score (%)')
    axes[0, 1].set_ylabel('Student Count')

    # Plot 3: Study Hours vs. Overall Average Score
    sns.scatterplot(data=df, x='Study_Hours', y='Overall_Average', hue='Attendance', 
                    palette='viridis', size='Attendance', sizes=(20, 100), ax=axes[1, 0])
    sns.regplot(data=df, x='Study_Hours', y='Overall_Average', scatter=False, ax=axes[1, 0], color='red')
    axes[1, 0].set_title('Study Hours vs. Overall Average (Sized by Attendance)', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Weekly Study Hours')
    axes[1, 0].set_ylabel('Overall Average (%)')

    # Plot 4: Boxplot of subject distributions
    sns.boxplot(data=df[subjects], ax=axes[1, 1], palette='Set2')
    axes[1, 1].set_title('Subject Score Distributions (Boxplot)', fontsize=12, fontweight='bold')
    axes[1, 1].set_ylabel('Score (%)')

    plt.suptitle("Exploratory Data Analysis (EDA) of Student Academic Performance", fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    print(f"\nStudent Performance dataset CSV saved to: [student_performance.csv](file:///{os.path.abspath(csv_file).replace(os.sep, '/')})")
    print(f"EDA Insights visual report saved to: [q20_student_eda_insights.png](file:///{plot_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    run_student_eda()
