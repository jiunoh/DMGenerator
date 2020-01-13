# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('/taskExecution', String, queue_size=10)

    rospy.init_node('dm_node', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    # KO Homecare
    publish_str_ko_home = []

    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"],"source": "planning"},"dialog_generation": {"name": "이병현", "intent": "saying_hello", "id": 196, "human_speech": "안녕","social_context": {"appellation":"어르신"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_sleep", "id": 197, "human_speech": "응 그래.","social_context": {}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_reaction", "id": 198, "human_speech": "응 푹 잤지", "social_context": {}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"},  "dialog_generation": {"name": "이병현", "intent": "check_information_disease", "id": 199, "human_speech": "그래 고마워", "social_context": {"disease_name":"고혈압"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_meal", "id": 200, "human_speech": "좋아졌어. 괜찮아.", "social_context": {"disease_status":"positive"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_advise", "id": 201, "human_speech": "싱겁게 먹었어", "social_context": {"disease_name":"고혈압", "disease_advice":"싱거운 음식과 가벼운 운동"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_health", "id": 202, "human_speech": "응 알지. 네가 맨날 말해 주는걸", "social_context": {"task":"약 복용"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_health_advice", "id": 203, "human_speech": "응 먹었어.", "social_context": {"medicine_schedule":"식후 30분에 복용"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 204, "human_speech": "알겠어. 고마워.", "social_context": {}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_hello", "id": 205, "human_speech": "또 보는구나", "social_context": {"appellation":"어르신"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_schedule", "id": 205, "human_speech": "응 잘 지냈지", "social_context": {"visit_place":"병원"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_regard", "id": 206, "human_speech": "어 다녀왔지", "social_context": {"disease_name":"고혈압","disease_status":"positive", "appellation":"어르신"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_medicine", "id": 207, "human_speech": "그렇지?", "social_context": {"disease_name":"고혈압", "disease_status":"positive", "appellation":"어르신"}}}')
    publish_str_ko_home.append(
        '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 208, "human_speech": "알겠어. 고마워.", "social_context": {}}}')

#소셜컨텍스트 바꿔서
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"],"source": "planning"},"dialog_generation": {"name": "이병현", "intent": "saying_hello", "id": 196, "human_speech": "안녕","social_context": {"appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_sleep", "id": 197, "human_speech": "응 그래.","social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_reaction", "id": 198, "human_speech": "응 푹 잤지", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"},  "dialog_generation": {"name": "이병현", "intent": "check_information_disease", "id": 199, "human_speech": "그래 고마워", "social_context": {"disease_name":"독감"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_meal", "id": 200, "human_speech": "나빠졌어. 안 괜찮아.", "social_context": {"disease_status":"negative"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_advise", "id": 201, "human_speech": "싱겁게 먹었어", "social_context": {"disease_name":"독감", "disease_advice":"든든한 식사와 약"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_health", "id": 202, "human_speech": "응 알지. 네가 맨날 말해 주는걸", "social_context": {"task":"주사 맞기"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_health_advice", "id": 203, "human_speech": "응 먹었어.", "social_context": {"medicine_schedule":"식전 30분에 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 204, "human_speech": "알겠어. 고마워.", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_hello", "id": 205, "human_speech": "또 보는구나", "social_context": {"appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_schedule", "id": 205, "human_speech": "응 잘 지냈지", "social_context": {"visit_place":"약국"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_regard", "id": 206, "human_speech": "어 다녀왔지", "social_context": {"disease_name":"독감","disease_status":"negative", "appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_medicine", "id": 207, "human_speech": "그렇지?", "social_context": {"disease_name":"독감", "disease_status":"negative", "appellation":"할아버지"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 208, "human_speech": "알겠어. 고마워.", "social_context": {}}}')

    #부정 응답(아니, 짜게 먹었어)
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"],"source": "planning"},"dialog_generation": {"name": "이병현", "intent": "saying_hello", "id": 196, "human_speech": "안녕","social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_sleep", "id": 197, "human_speech": "응 그래.","social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_reaction", "id": 198, "human_speech": "못 잤어", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"},  "dialog_generation": {"name": "이병현", "intent": "check_information_disease", "id": 199, "human_speech": "그래 고마워", "social_context": {"disease_name":"고혈압"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_meal", "id": 200, "human_speech": "안 좋아. 나빠졌어.", "social_context": {"disease_status":"negative"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_advise", "id": 201, "human_speech": "매운 음식 먹었어", "social_context": {"disease_name":"고혈압", "disease_advice":"싱거운 음식과 가벼운 운동"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_health", "id": 202, "human_speech": "아니 싫어", "social_context": {"task":"약 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_health_advice", "id": 203, "human_speech": "아니 안 먹었어.", "social_context": {"medicine_schedule":"식후 30분에 복용"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 204, "human_speech": "알겠어. 고마워.", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_hello", "id": 205, "human_speech": "또 보는구나", "social_context": {}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_schedule", "id": 205, "human_speech": "아니 못 지냈어", "social_context": {"visit_place":"병원"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_regard", "id": 206, "human_speech": "안 다녀왔어", "social_context": {"disease_name":"고혈압","disease_status":"positive", "appellation":"어르신"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_medicine", "id": 207, "human_speech": "그렇지?", "social_context": {"disease_name":"고혈압", "disease_status":"positive", "appellation":"어르신"}}}')
    # publish_str_ko_home.append(
    #     '{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 208, "human_speech": "알겠어. 고마워.", "social_context": {}}}')


    for k in range(0, len(publish_str_ko_home)):
        rospy.loginfo(publish_str_ko_home[k])
        pub.publish(publish_str_ko_home[k])
        rospy.sleep(2)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass