import requests
import json
import time

def get_course_info(course_id):
    json_content = []
    for page in range(1,223):
        time.sleep(1)
        url = f'https://www.udemy.com/api-2.0/courses/{course_id}/reviews/?courseId={course_id}&page={page}&is_text_review=1&ordering=course_review_score__rank,-created&fields[course_review]=@default,response,content_html,created_formatted_with_time_since&fields[user]=@min,image_50x50,initials,public_display_name,tracking_id&fields[course_review_response]=@min,user,content_html,created_formatted_with_time_since/'
        response = requests.get(url)
        json_response = json.loads(response.text)
        content = parse_results(json_response)
        json_content.extend(content)
        print("Page:", page, " Status:", response.status_code)

    with open("course.json", "w") as outfile:
        json.dump(json_content, outfile)

def parse_results(json_data):
    results = json_data['results']
    row_list = []
    for result in results:
        review = result['content']
        rating = result['rating']
        row = {'review': review, 'rating': rating}
        row_list.append(row)
    return row_list

if __name__ == "__main__":
    get_course_info(1527300)
    
