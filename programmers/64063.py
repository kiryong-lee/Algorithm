
def solution(k, room_number):
    room_dict = dict()
    answer = []
    for room in room_number:
        if room not in room_dict:
            room_dict[room] = room + 1
            answer.append(room)
        else:
            update_list = []
            while room in room_dict:
                update_list.append(room)
                room = room_dict[room]

            for update in update_list:
                room_dict[update] = room + 1
            room_dict[room] = room + 1
            
            answer.append(room)
        
    return answer
