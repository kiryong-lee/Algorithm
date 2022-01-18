
def solution(id_list, report, k):
    
    report = set(report)
    report_dict = dict()
    for r in report:
        user, malicious = r.split(' ')
        if malicious not in report_dict:
            report_dict[malicious] = 1
        else:
            report_dict[malicious] = report_dict[malicious] + 1

    user_len = len(id_list)
    answer = [0] * user_len
    for r in report:
        user, malicious = r.split(' ')
        if malicious in report_dict and report_dict[malicious] >= k:
            for i in range(user_len):
                if id_list[i] == user:
                    answer[i] += 1
                    break
    
    return answer
