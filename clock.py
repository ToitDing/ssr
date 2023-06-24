import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Remaining Time: {remaining_time // 60:02d}:{remaining_time % 60:02d}", end="\r")
        time.sleep(1)
    
    print("Focus time is over!")

# 设置专注时间为25分钟
focus_timer(25)
