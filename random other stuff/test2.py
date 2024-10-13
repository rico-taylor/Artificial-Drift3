from datetime import datetime

def sort_tuples_by_date(tuples_list):
    # Define a function to convert date from DD-MM-YYYY to a sortable format
    def convert_date(date_str):
        return datetime.strptime(date_str, "%d-%m-%Y")

    # Sort the list using the converted date for comparison
    sorted_list = sorted(tuples_list, key=lambda x: convert_date(x[0]), reverse=True)
    
    return sorted_list

# Example usage
date_username_tuples = [
    ('06-10-2023', 'user1'),
    ('05-10-2024', 'user2'),
    ('04-10-2024', 'user3'),
    ('01-10-2024', 'user4'),
    ('10-09-2024', 'user5'),
]

sorted_tuples = sort_tuples_by_date(date_username_tuples)
print(sorted_tuples)