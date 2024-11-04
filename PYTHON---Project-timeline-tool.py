import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def get_project_tasks():
    """
    Collect task information for the project timeline.
    """
    tasks = []
    num_tasks = int(input("Enter the number of tasks in your project: "))
    
    for i in range(num_tasks):
        print(f"\nTask {i + 1}:")
        name = input("Task name: ")
        start_date = input("Start date (YYYY-MM-DD): ")
        duration = int(input("Duration (in days): "))
        
        # Calculate end date
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = start_dt + timedelta(days=duration)
        
        tasks.append({
            "name": name,
            "start": start_dt,
            "end": end_dt
        })
    
    return tasks

def plot_timeline(tasks):
    """
    Plot a timeline (Gantt chart) for the project tasks.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot each task
    for i, task in enumerate(tasks):
        ax.barh(task['name'], task['end'] - task['start'], left=task['start'], color='skyblue')
    
    # Format date and axis
    ax.set_xlabel("Date")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    fig.autofmt_xdate()  # Rotate date labels
    plt.title("Project Timeline")
    
    # Show plot
    plt.tight_layout()
    plt.show()

# Main Function to Run the Project Timeline Tool
if __name__ == "__main__":
    tasks = get_project_tasks()
    plot_timeline(tasks)
