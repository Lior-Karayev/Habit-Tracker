import json
import os
import datetime
import streamlit as st

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_habit(data):
    habit = input("Enter habit name: ")
    if habit not in data:
        data[habit] = {"Streak": 0, "last_done": None}
        print(f"Habit '{habit}' added.")
    else:
        print(f"Habit '{habit}' already exists.")
    return data

def update_habit(data, habit):
    if habit in data:
        date = datetime.datetime.strptime(data[habit]["last_done"], '%Y-%m-%d') if data[habit]["last_done"] else None
        if date is not None and datetime.datetime.now().date() == date.date():
            print(f"Habit '{habit}' already marked as done today.")
        elif date is None or datetime.datetime.now() > date - datetime.timedelta(days=1):
            data[habit]["Streak"] = 1
        else:
            data[habit]["Streak"] += 1

        data[habit]["last_done"] = datetime.date.today().isoformat()
        print(f"[{habit}] - Current Streak: {data[habit]['Streak']}")
    else:
        print(f"Habit '{habit}' does not exist.")
    return data

def view_progress(data):
    if not data:
        print("No habits to show.")
        return
    for habit, details in data.items():
        last_done = details["last_done"] if details["last_done"] else "Never"
        print(f"Habit: {habit}, Streak: {details['Streak']}, Last Done: {last_done}")

def ensure_habit(data, habit):
    if habit not in data:
        data[habit] = {"Streak": 0, "last_done": None}
    return data

def main():
    st.set_page_config(page_title="Habit Tracker", page_icon="✅")
    st.title("✅ Habit Tracker")

    data = load_data()

    with st.sidebar:
        st.header("Add New Habit")
        new_habit = st.text_input("Habit Name", "")
        if st.button("Add Habit"):
            if new_habit.strip():
                ensure_habit(data, new_habit)
                save_data(data)
                st.success(f"Habit '{new_habit.strip()}' added.")
            
    st.subheader("Your habits")
    if not data:
        st.info("No habits added yet. Use the sidebar to add a new habit.")
    else:
        for habit, info in data.items():
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.write(f"**{habit}**")
            with col2:
                st.write(f"Streak: {info['Streak']}")
            with col3:
                st.write(f"Last Done: {info['last_done']}")
                
            is_done_today = info['last_done'] == datetime.date.today().isoformat()

            if st.button(f"Mark '{habit}' as done", key=f"done_{habit}", disabled=is_done_today):
                data = update_habit(data, habit)
                save_data(data)
                st.success(f"Habit '{habit}' marked as done.")
                st.rerun()

    st.divider()
    if st.button("Export JSON"):
        st.download_button(
            label="Download Data as JSON",
            data=json.dumps(data, indent=2),
            file_name='data.json',
        )

if __name__ == "__main__":
    main()