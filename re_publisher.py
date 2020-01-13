# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('/taskExecution', String, queue_size=10)

    rospy.init_node('dm_node', anonymous=True)
    rate = rospy.Rate(20)

    # KO Reception
    publish_str_ko = []
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"],"source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_welcome", "id": 178, "human_speech": "안녕","social_context": {"appellation":"어르신"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_disease", "id": 179, "human_speech": "음 먼저 고혈압 약이 필요해. 도와줄래?", "social_context": {"disease_name":"고혈압", "disease_status":"positive", "appellation":"어르신"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_pharmacy", "id": 180, "human_speech": "노력한게 결과를 이루니 좋구만", "social_context": {"opening_hour":"8시", "place":"약국", "treat":"처방전"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_disease_advice", "id": 181, "human_speech": "응, 독감예방접종을 하고 싶은데 알려줄래?", \
            "social_context": {"disease_name":"독감", "disease_description":"바이러스로 인해 생겨나는 전염성 호흡기 질환", "disease_symptom":"발열, 기침, 몸살, 금육통", "prevent":"예방 접종"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_reservation", "id": 182, "human_speech": "하하하 재밌네. 독감을 피하려면 어떻게 해야할지 알려줄수 있니?", "social_context": {"disease_name":"독감", "treat":"예방 접종"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_center_reservation", "id": 183, "human_speech": "그래 혹시 내일 시간이 어떻게 되니?", "social_context": {"available_time": "오전10시, 오후12시, 오후 3시 30분", "date":"내일"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "check_information_alarm", "id": 184, "human_speech": "그럼 3시 반에 예약해줘", "social_context": {"available_time": "10:00, 12:00, 15:30"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "transmit_information_reservation", "id": 185, "human_speech": "그래줄래?","social_context": {"date":"내일"}}} ')
    publish_str_ko.append('{"header": {"timestamp": "1563980674.262554407", "target": ["dialog"], "content": ["dialog_generation"], "source": "planning"}, "dialog_generation": {"name": "이병현", "intent": "saying_good_bye", "id": 186, "human_speech": "고맙구나", "social_context": {}}} ')

    for i in range(0, len(publish_str_ko)):
      rospy.loginfo(publish_str_ko[i])
      pub.publish(publish_str_ko[i])
      rospy.sleep(4)
      rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass