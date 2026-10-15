# 1. Create a list of unverified server tasks
unverified_tasks = ['backup_nas', 'update_lms', 'clean_logs']
confirmed_tasks = []

# 2. THE CORE MECHANIC: Loop runs AS LONG AS the list has items inside it

while unverified_tasks:
    # .pop() slices the absolute last item off the list and hands it to us
    current_task = unverified_tasks.pop()

    print(f"Verifying infrastructure task: {current_task}")

    # Move the item into our secondary "confirmed" container
    confirmed_tasks.append(current_task)

    # 3. Print tthe final results to see the move completed
    print("\n--- All tasks safely verified ---")
    print("Confirmed list:", confirmed_tasks)
    print("Original unverified list is now:", unverified_tasks)