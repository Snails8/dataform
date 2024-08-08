import os
import csv
from datetime import datetime, timedelta
import uuid
import random


############################
# sampleデータを生成するコード
############################
num_records = 100000
filepath = os.path.join('result', 'user_action.csv')

def generate_sample_data():
    headers = ['timestamp', 'user_id', 'session_id', 'page_url', 'event_type']
  
    pages = ['/home', '/products', '/about', '/contact', '/cart', '/checkout']
    event_types = ['pageview', 'click', 'scroll', 'purchase']
    device_types = ['desktop', 'mobile', 'tablet']
    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
    num_users = 1000
    user_ids = [str(uuid.uuid4()) for _ in range(num_users)]
    
    with open(filepath, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(headers)
        
        start_date = datetime.now() - timedelta(days=30)
        sessions = {}
        
        for _ in range(num_records):
            timestamp = start_date + timedelta(seconds=random.randint(0, 30*24*60*60))
            user_id = random.choice(user_ids) 
            page_url = random.choice(pages)
            event_type = random.choice(event_types)
            device_type = random.choice(device_types)
            browser = random.choice(browsers)
            # 分析用にsession_idを生成(新規、30分経過で新規)
            if user_id in sessions:
                last_activity, session_id = sessions[user_id]
                if (timestamp - last_activity) > timedelta(minutes=30):
                    session_id = str(uuid.uuid4())
            else:
                session_id = str(uuid.uuid4())
            sessions[user_id] = (timestamp, session_id)
            
            writer.writerow([timestamp, user_id, session_id, page_url, event_type, device_type, browser])


if __name__ == '__main__':
    data = generate_sample_data()
    print('Data saved.')

